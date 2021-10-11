#!/usr/bin/env python3
from argparse import ArgumentParser
from collections import OrderedDict
from pathlib import Path
from struct import Struct
from tempfile import TemporaryDirectory
from typing import Optional, List, Dict, Tuple, Union, OrderedDict as TOrderedDict, TypeVar

from elftools.dwarf.die import DIE
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

from odiff.c import HeaderFile, CType, CStruct, CUnion, CEnum, CVariable, CFunction, CPointer, CArray, CConst, \
    CVolatile, CFunctionPtr, CVoid, CPrimitive, CEllipsis, CTypedef
from odiff.html import HTML_HEADER, HTML_FOOTER, make_diff_table
from odiff.lib import LIBRARIES
from odiff.paths import VENDOR_PATH_PREFIX, REPO_ROOT
from odiff.utils import get_or_create, remove_prefixes

CFLAGS = [
    '-march=rv32imfc',
    '-mabi=ilp32f',
    '-gdwarf',
    '-Os',
    '-std=gnu99',
    '-ffunction-sections',
    '-fdata-sections',
    '-fstrict-volatile-bitfields',
    '-fshort-enums',
    '-ffreestanding',
    '-fno-strict-aliasing',

    # Silence please
    '-Wno-deprecated-declarations',

    # BL602 headers want this
    '-DARCH_RISCV'
]


def die_get_name(die: DIE) -> Optional[str]:
    return die.attributes['DW_AT_name'].value.decode() if 'DW_AT_name' in die.attributes else None


def die_get_at_type(die: DIE) -> CType:
    try:
        return die_to_ctype(die.cu.get_DIE_from_refaddr(die.attributes['DW_AT_type'].value))
    except KeyError:
        return CVoid


def die_to_funclike_args(die: DIE) -> Tuple[CType, List[Tuple[CType, Optional[str]]]]:
    if die.tag not in ('DW_TAG_subroutine_type', 'DW_TAG_subprogram'):
        raise ValueError(f"Wrong DIE tag {die.tag} for a function/funcptr")
    return_type = die_get_at_type(die)
    args: List[Tuple[CType, Optional[str]]] = []
    for arg_die in die.iter_children():
        arg_die: DIE
        if arg_die.tag == 'DW_TAG_formal_parameter':
            arg_name: Optional[str] = arg_die.attributes['DW_AT_name'].value.decode() \
                if 'DW_AT_name' in die.attributes else None
            args.append((
                die_to_ctype(die.cu.get_DIE_from_refaddr(arg_die.attributes['DW_AT_type'].value)), arg_name))
        elif arg_die.tag == 'DW_TAG_unspecified_parameters':
            args.append((CEllipsis, None))
        elif arg_die.tag in ('DW_TAG_variable', 'DW_TAG_inlined_subroutine', 'DW_TAG_lexical_block',
                             'DW_TAG_subprogram', 'DW_TAG_label') \
                or arg_die.tag.startswith('DW_TAG_GNU') or arg_die.tag.endswith('_type'):
            pass  # Skip
        else:
            raise TypeError(f"What is a {arg_die.tag} function DIE child?")
    return return_type, args


def die_to_func(die: DIE) -> CFunction:
    if die.tag != 'DW_TAG_subprogram':
        raise ValueError(f"Wrong DIE tag {die.tag} for a function")
    return_type, args = die_to_funclike_args(die)
    return CFunction(die=die, name=die_get_name(die), return_type=return_type, args=args)


CT = TypeVar('CT')


def cache_ctype(ctype: CT) -> CT:
    ctype.die.cu.ctype_cache[ctype.die.offset] = ctype
    return ctype


def die_to_ctype(die: DIE) -> CType:
    if not hasattr(die.cu, 'ctype_cache'):
        die.cu.ctype_cache = {}
    try:
        return die.cu.ctype_cache[die.offset]
    except KeyError:
        pass

    if die.tag == 'DW_TAG_pointer_type':
        of = die_get_at_type(die)
        # DW_TAG_subroutine_type is already turned into a function pointer, so bypass the first level of indirection
        if 'DW_AT_type' in die.attributes:
            of_die: DIE = die.cu.get_DIE_from_refaddr(die.attributes['DW_AT_type'].value)
            if of_die.tag == 'DW_TAG_subroutine_type':
                return of
        return cache_ctype(CPointer(die=die, of=of))
    elif die.tag == 'DW_TAG_array_type':
        array_length: Optional[int] = None
        for child_die in die.iter_children():
            if child_die.tag == 'DW_TAG_subrange_type' and 'DW_AT_upper_bound' in child_die.attributes:
                array_length = child_die.attributes['DW_AT_upper_bound'].value + 1
        return cache_ctype(CArray(die=die, of=die_get_at_type(die), length=array_length))
    elif die.tag == 'DW_TAG_structure_type':
        members: TOrderedDict[str, CType] = OrderedDict()
        member_offsets: Dict[str, int] = {}
        struct = cache_ctype(CStruct(die=die, name=die_get_name(die), members=members, member_offsets=member_offsets))
        for memb_die in die.iter_children():
            if memb_die.tag == 'DW_TAG_member':
                memb_name = die_get_name(memb_die)
                members[memb_name] = die_get_at_type(memb_die)
                member_offsets[memb_name] = memb_die.attributes['DW_AT_data_member_location'].value
        return struct
    elif die.tag == 'DW_TAG_union_type':
        members: TOrderedDict[str, CType] = OrderedDict()
        union = cache_ctype(CUnion(die=die, name=die_get_name(die), members=members))
        for memb_die in die.iter_children():
            if memb_die.tag == 'DW_TAG_member':
                members[die_get_name(memb_die)] = die_get_at_type(memb_die)
        return union
    elif die.tag == 'DW_TAG_enumeration_type':
        members: TOrderedDict[str, int] = OrderedDict()
        enum = cache_ctype(CEnum(die=die, name=die_get_name(die), members=members))
        for memb_die in die.iter_children():
            if memb_die.tag == 'DW_TAG_enumerator':
                members[die_get_name(memb_die)] = memb_die.attributes['DW_AT_const_value'].value
        return enum
    elif die.tag in ('DW_TAG_const_type', 'DW_TAG_volatile_type'):
        of = die_get_at_type(die)
        if isinstance(of, CArray):
            return of  # A cv array is an array of cv, and its element types are already cv-qualified
        if die.tag == 'DW_TAG_const_type':
            return cache_ctype(CConst(die=die, of=of))
        else:
            return cache_ctype(CVolatile(die=die, of=of))
    elif die.tag == 'DW_TAG_subroutine_type':
        return_type, args = die_to_funclike_args(die)
        return cache_ctype(CFunctionPtr(die=die, return_type=return_type, args=args))
    elif die.tag == 'DW_TAG_base_type':
        name = die.attributes['DW_AT_name'].value.decode()
        if name == '_Bool':
            name = 'bool'
        return cache_ctype(CPrimitive(die=die, name=name))
    elif die.tag == 'DW_TAG_typedef':
        return cache_ctype(CTypedef(die=die, name=die.attributes['DW_AT_name'].value.decode(), of=die_get_at_type(die)))
    else:
        raise TypeError(f"What is a type {die.tag}?")


ELF_SYM_STRUCT = Struct('<I8xB')
STB_LOCAL = 0
STT_OBJECT = 1
STT_FUNC = 2


def is_static(symtab: SymbolTableSection, name: str) -> Tuple[bool, bool]:
    if not hasattr(symtab, '_static_cache'):
        static = {}
        entsize = symtab['sh_entsize']
        symtab.stream.seek(symtab['sh_offset'])
        buf = symtab.stream.read(entsize * symtab.num_symbols())
        for pos in range(0, len(buf), entsize):
            st_name, st_info = ELF_SYM_STRUCT.unpack(buf[pos:pos + ELF_SYM_STRUCT.size])
            if (st_info & 0xF) in (STT_FUNC, STT_OBJECT):
                static[symtab.stringtable.get_string(st_name)] = (st_info >> 4) == STB_LOCAL
        symtab._static_cache = static
    try:
        # noinspection PyProtectedMember
        return True, symtab._static_cache[name]
    except KeyError:
        return False, False


class Context:
    def __init__(self, name: str):
        self.name = name
        self.funcs: Dict[str, Tuple[CFunction, bool]] = {}

    def func(self, func_name: str) -> Optional[CFunction]:
        try:
            return self.funcs[func_name][0]
        except KeyError:
            return None

    def decl_func(self, func: CFunction):
        self.funcs[func.name] = (func, False)

    def def_func(self, funcdef: CFunction, inline: bool):
        if funcdef.name not in self.funcs:
            self.funcs[funcdef.name] = (funcdef, True)
            return
        f, defined = self.funcs[funcdef.name]
        if defined:
            if inline:
                return
            raise ValueError(f"ODR violation: function {funcdef.name} is defined twice in context {self.name}")
        f.return_type = funcdef.return_type
        f.args = funcdef.args


def die_to_ctype_or_func(ctx: Context, die: DIE, symtab: SymbolTableSection) -> Union[CType, CFunction]:
    if die.tag != 'DW_TAG_subprogram':
        return die_to_ctype(die)
    func_name = die_get_name(die)
    in_obj, static = is_static(symtab, func_name)
    if static:
        return_type, args = die_to_funclike_args(die)
        return CFunction(die=die, name=func_name, return_type=return_type, args=args, static=True)
    if in_obj:
        return_type, args = die_to_funclike_args(die)
        cfunc = CFunction(die=die, name=func_name, return_type=return_type, args=args, static=False)
        ctx.def_func(cfunc, 'DW_AT_inline' in die.attributes)
        return cfunc
    if (cfunc := ctx.func(func_name)) is not None:
        return cfunc
    return_type, args = die_to_funclike_args(die)
    cfunc = CFunction(die=die, name=func_name, return_type=return_type, args=args, static=False)
    ctx.decl_func(cfunc)
    return cfunc


def process_file(filename: Path, header_files: Dict[str, HeaderFile], ctx: Context):
    with open(filename, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        dwarf = elf.get_dwarf_info()
        try:
            cu = next(dwarf.iter_CUs())
        except StopIteration:
            return
        lp = dwarf.line_program_for_CU(cu)
        include_directories: List[str] = [x.decode() for x in lp.header.include_directory]
        file_entries: List[HeaderFile] = [
            get_or_create(
                header_files,
                remove_prefixes(
                    f'{include_directories[x.dir_index - 1]}/{x.name.decode()}',
                    [VENDOR_PATH_PREFIX, f'{REPO_ROOT}/'])
                if x.dir_index != 0 else x.name.decode(),
                lambda path: HeaderFile(path)
            )
            for x in lp['file_entry']
        ]
        cu_die: DIE = cu.get_top_DIE()
        for die in cu_die.iter_children():
            die: DIE
            if not 'DW_AT_decl_file' in die.attributes:
                continue
            decl_file = file_entries[die.attributes['DW_AT_decl_file'].value - 1]
            decl_line = die.attributes['DW_AT_decl_line'].value
            name: Optional[str] = die_get_name(die)
            if die.tag == 'DW_TAG_variable':
                if 'DW_AT_specification' in die.attributes:
                    var_spec_die = cu.get_DIE_from_refaddr(die.attributes['DW_AT_specification'].value)
                    name = die_get_name(var_spec_die)
                    assert name is not None
                    entry = CVariable(
                        die=die, type=die_get_at_type(var_spec_die), name=name,
                        extern='DW_AT_external' in die.attributes, static=False)
                else:
                    _, static = is_static(symtab, name)
                    entry = CVariable(
                        die=die, type=die_get_at_type(die), name=name,
                        extern='DW_AT_external' in die.attributes, static=static)
            else:
                if name is None:
                    continue
                entry = die_to_ctype_or_func(ctx, die, symtab)
            decl_file.defs[name] = entry
            decl_file.def_lines[name] = decl_line


def main():
    parser = ArgumentParser(description="Generate HTML diffs between symbols in header files")
    parser.add_argument('-o', '--output', type=str, default='report.html', help="Output file name")
    parser.add_argument(dest='patterns', type=str, nargs='*', help="Glob-like pattern(s) of files to build")
    args = parser.parse_args()
    html = open(args.output, 'w')
    html.write(HTML_HEADER)
    from odiff.riscvreloc import patch_elftools_relocs
    patch_elftools_relocs()
    patterns: List[str] = args.patterns
    vendor_header_files: Dict[str, HeaderFile] = {}
    for lib in LIBRARIES:
        vendor_lib_ctx = Context('vendor_' + lib.name)
        for vendorobj_path in lib.get_vendorobj_paths(patterns):
            print(f"Collecting vendor {lib.name}/{vendorobj_path.name}")
            process_file(vendorobj_path, vendor_header_files, vendor_lib_ctx)
    # print("\n".join(f"=========== {k}\n{v}" for k, v in vendor_header_files.items()))
    re_header_files: Dict[str, HeaderFile] = {}
    with TemporaryDirectory(prefix='headerdiff') as tmpdir:
        for lib in LIBRARIES:
            re_lib_ctx = Context('re_' + lib.name)
            for vendorobj_path in lib.get_vendorobj_paths(patterns):
                _, result, reobj_path = lib.build_obj(Path(tmpdir), vendorobj_path, CFLAGS)
                if result.returncode != 0:
                    print(f"{vendorobj_path.name} failed to build: {result.stderr.decode()}")
                    continue
                print(f"Collecting reverse-engineered {lib.name}/{vendorobj_path.name}")
                process_file(reobj_path, re_header_files, re_lib_ctx)
    for vhdr_name, vhdr in sorted(vendor_header_files.items(), key=lambda x: x[0]):
        if not vhdr_name.startswith('components/'):
            continue
        rehdr = re_header_files.get(vhdr_name, None)
        html.write(f'<article class="hdr"><h1>{vhdr_name}</h1>')
        if rehdr is None:
            html.write('Not there!')
            html.write(f'<pre><code>{vhdr.to_source()}</code></pre>')
        else:
            html.write(f'<pre><code>{vhdr.to_source()}</code></pre>')
            original_a = [(vhdr.def_lines[k], k, v) for k, v in vhdr.sorted_defs]
            original_b = [(rehdr.def_lines[k], k, v) for k, v in rehdr.sorted_defs]
            content, similarity = make_diff_table(
                original_a,
                original_b,
                [x[1] for x in original_a],
                [x[1] for x in original_b],
                get_offset=lambda x: str(x[0]),
                get_text=lambda x: f'{x[1]}: {x[2]}'
            )
            html.write(content)
        html.write('</article>')
    html.write(HTML_FOOTER)


if __name__ == '__main__':
    main()
