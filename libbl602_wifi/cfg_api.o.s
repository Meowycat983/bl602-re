
cfg_api.o:     file format elf32-littleriscv


Disassembly of section .text.cfg_api_element_dump:

00000000 <cfg_api_element_dump>:
   0:	15fd                	addi	a1,a1,-1

00000002 <.LVL1>:
   2:	0ff5f593          	andi	a1,a1,255
   6:	479d                	li	a5,7
   8:	1ab7e063          	bltu	a5,a1,1a8 <.L21>
   c:	000007b7          	lui	a5,0x0
  10:	00078793          	mv	a5,a5
  14:	058a                	slli	a1,a1,0x2
  16:	95be                	add	a1,a1,a5
  18:	419c                	lw	a5,0(a1)
  1a:	1141                	addi	sp,sp,-16
  1c:	c422                	sw	s0,8(sp)
  1e:	c606                	sw	ra,12(sp)
  20:	8432                	mv	s0,a2
  22:	8782                	jr	a5

00000024 <.L11>:
  24:	00054783          	lbu	a5,0(a0)
  28:	ef8d                	bnez	a5,62 <.L22>
  2a:	000006b7          	lui	a3,0x0
  2e:	00068693          	mv	a3,a3

00000032 <.L12>:
  32:	00000637          	lui	a2,0x0

00000036 <.LVL2>:
  36:	00060613          	mv	a2,a2
  3a:	45bd                	li	a1,15
  3c:	8522                	mv	a0,s0

0000003e <.LVL3>:
  3e:	00000097          	auipc	ra,0x0
  42:	000080e7          	jalr	ra # 3e <.LVL3>

00000046 <.LVL4>:
  46:	00055363          	bgez	a0,4c <.L13>
  4a:	4501                	li	a0,0

0000004c <.L13>:
  4c:	9522                	add	a0,a0,s0
  4e:	00050023          	sb	zero,0(a0)
  52:	00000537          	lui	a0,0x0
  56:	00050513          	mv	a0,a0

0000005a <.L1>:
  5a:	40b2                	lw	ra,12(sp)
  5c:	4422                	lw	s0,8(sp)
  5e:	0141                	addi	sp,sp,16
  60:	8082                	ret

00000062 <.L22>:
  62:	000006b7          	lui	a3,0x0
  66:	00068693          	mv	a3,a3
  6a:	b7e1                	j	32 <.L12>

0000006c <.L10>:
  6c:	00050683          	lb	a3,0(a0) # 0 <cfg_api_element_dump>
  70:	00000637          	lui	a2,0x0
  74:	00060613          	mv	a2,a2
  78:	45bd                	li	a1,15
  7a:	8522                	mv	a0,s0

0000007c <.LVL7>:
  7c:	00000097          	auipc	ra,0x0
  80:	000080e7          	jalr	ra # 7c <.LVL7>

00000084 <.LVL8>:
  84:	00055363          	bgez	a0,8a <.L14>
  88:	4501                	li	a0,0

0000008a <.L14>:
  8a:	9522                	add	a0,a0,s0
  8c:	00050023          	sb	zero,0(a0)
  90:	00000537          	lui	a0,0x0
  94:	00050513          	mv	a0,a0
  98:	b7c9                	j	5a <.L1>

0000009a <.L9>:
  9a:	00054683          	lbu	a3,0(a0) # 0 <cfg_api_element_dump>
  9e:	00000637          	lui	a2,0x0
  a2:	00060613          	mv	a2,a2
  a6:	45bd                	li	a1,15
  a8:	8522                	mv	a0,s0

000000aa <.LVL10>:
  aa:	00000097          	auipc	ra,0x0
  ae:	000080e7          	jalr	ra # aa <.LVL10>

000000b2 <.LVL11>:
  b2:	00055363          	bgez	a0,b8 <.L15>
  b6:	4501                	li	a0,0

000000b8 <.L15>:
  b8:	9522                	add	a0,a0,s0
  ba:	00050023          	sb	zero,0(a0)
  be:	00000537          	lui	a0,0x0
  c2:	00050513          	mv	a0,a0
  c6:	bf51                	j	5a <.L1>

000000c8 <.L8>:
  c8:	00051683          	lh	a3,0(a0) # 0 <cfg_api_element_dump>
  cc:	00000637          	lui	a2,0x0
  d0:	00060613          	mv	a2,a2
  d4:	45bd                	li	a1,15
  d6:	8522                	mv	a0,s0

000000d8 <.LVL13>:
  d8:	00000097          	auipc	ra,0x0
  dc:	000080e7          	jalr	ra # d8 <.LVL13>

000000e0 <.LVL14>:
  e0:	00055363          	bgez	a0,e6 <.L16>
  e4:	4501                	li	a0,0

000000e6 <.L16>:
  e6:	9522                	add	a0,a0,s0
  e8:	00050023          	sb	zero,0(a0)
  ec:	00000537          	lui	a0,0x0
  f0:	00050513          	mv	a0,a0
  f4:	b79d                	j	5a <.L1>

000000f6 <.L7>:
  f6:	00055683          	lhu	a3,0(a0) # 0 <cfg_api_element_dump>
  fa:	00000637          	lui	a2,0x0
  fe:	00060613          	mv	a2,a2
 102:	45bd                	li	a1,15
 104:	8522                	mv	a0,s0

00000106 <.LVL16>:
 106:	00000097          	auipc	ra,0x0
 10a:	000080e7          	jalr	ra # 106 <.LVL16>

0000010e <.LVL17>:
 10e:	00055363          	bgez	a0,114 <.L17>
 112:	4501                	li	a0,0

00000114 <.L17>:
 114:	9522                	add	a0,a0,s0
 116:	00050023          	sb	zero,0(a0)
 11a:	00000537          	lui	a0,0x0
 11e:	00050513          	mv	a0,a0
 122:	bf25                	j	5a <.L1>

00000124 <.L6>:
 124:	4114                	lw	a3,0(a0)
 126:	00000637          	lui	a2,0x0
 12a:	00060613          	mv	a2,a2
 12e:	45bd                	li	a1,15
 130:	8522                	mv	a0,s0

00000132 <.LVL19>:
 132:	00000097          	auipc	ra,0x0
 136:	000080e7          	jalr	ra # 132 <.LVL19>

0000013a <.LVL20>:
 13a:	00055363          	bgez	a0,140 <.L18>
 13e:	4501                	li	a0,0

00000140 <.L18>:
 140:	9522                	add	a0,a0,s0
 142:	00050023          	sb	zero,0(a0) # 0 <cfg_api_element_dump>
 146:	00000537          	lui	a0,0x0
 14a:	00050513          	mv	a0,a0
 14e:	b731                	j	5a <.L1>

00000150 <.L5>:
 150:	4114                	lw	a3,0(a0)
 152:	00000637          	lui	a2,0x0
 156:	00060613          	mv	a2,a2
 15a:	45bd                	li	a1,15
 15c:	8522                	mv	a0,s0

0000015e <.LVL22>:
 15e:	00000097          	auipc	ra,0x0
 162:	000080e7          	jalr	ra # 15e <.LVL22>

00000166 <.LVL23>:
 166:	00055363          	bgez	a0,16c <.L19>
 16a:	4501                	li	a0,0

0000016c <.L19>:
 16c:	9522                	add	a0,a0,s0
 16e:	00050023          	sb	zero,0(a0) # 0 <cfg_api_element_dump>
 172:	00000537          	lui	a0,0x0
 176:	00050513          	mv	a0,a0
 17a:	b5c5                	j	5a <.L1>

0000017c <.L3>:
 17c:	4114                	lw	a3,0(a0)
 17e:	00000637          	lui	a2,0x0
 182:	00060613          	mv	a2,a2
 186:	45bd                	li	a1,15
 188:	8522                	mv	a0,s0

0000018a <.LVL25>:
 18a:	00000097          	auipc	ra,0x0
 18e:	000080e7          	jalr	ra # 18a <.LVL25>

00000192 <.LVL26>:
 192:	00055363          	bgez	a0,198 <.L20>
 196:	4501                	li	a0,0

00000198 <.L20>:
 198:	942a                	add	s0,s0,a0

0000019a <.LVL27>:
 19a:	00000537          	lui	a0,0x0
 19e:	00040023          	sb	zero,0(s0)
 1a2:	00050513          	mv	a0,a0
 1a6:	bd55                	j	5a <.L1>

000001a8 <.L21>:
 1a8:	4501                	li	a0,0

000001aa <.LVL29>:
 1aa:	8082                	ret

Disassembly of section .text.cfg_api_element_general_set:

00000000 <cfg_api_element_general_set>:
   0:	1141                	addi	sp,sp,-16
   2:	c422                	sw	s0,8(sp)
   4:	c226                	sw	s1,4(sp)
   6:	c606                	sw	ra,12(sp)
   8:	842e                	mv	s0,a1
   a:	450c                	lw	a1,8(a0)

0000000c <.LVL31>:
   c:	84aa                	mv	s1,a0
   e:	00000537          	lui	a0,0x0

00000012 <.LVL32>:
  12:	00050513          	mv	a0,a0
  16:	00000097          	auipc	ra,0x0
  1a:	000080e7          	jalr	ra # 16 <.LVL32+0x4>

0000001e <.LVL33>:
  1e:	0064d783          	lhu	a5,6(s1)
  22:	4719                	li	a4,6
  24:	17fd                	addi	a5,a5,-1
  26:	07c2                	slli	a5,a5,0x10
  28:	83c1                	srli	a5,a5,0x10
  2a:	00f76f63          	bltu	a4,a5,48 <.L28>
  2e:	00000737          	lui	a4,0x0
  32:	00070713          	mv	a4,a4
  36:	078a                	slli	a5,a5,0x2
  38:	97ba                	add	a5,a5,a4
  3a:	4398                	lw	a4,0(a5)
  3c:	44dc                	lw	a5,12(s1)
  3e:	8702                	jr	a4

00000040 <.L35>:
  40:	00040703          	lb	a4,0(s0)

00000044 <.L38>:
  44:	00e78023          	sb	a4,0(a5) # 0 <cfg_api_element_general_set>

00000048 <.L28>:
  48:	40b2                	lw	ra,12(sp)
  4a:	4422                	lw	s0,8(sp)

0000004c <.LVL34>:
  4c:	4492                	lw	s1,4(sp)

0000004e <.LVL35>:
  4e:	4501                	li	a0,0
  50:	0141                	addi	sp,sp,16
  52:	8082                	ret

00000054 <.L34>:
  54:	00044703          	lbu	a4,0(s0)
  58:	b7f5                	j	44 <.L38>

0000005a <.L33>:
  5a:	00041703          	lh	a4,0(s0)

0000005e <.L39>:
  5e:	00e79023          	sh	a4,0(a5)
  62:	b7dd                	j	48 <.L28>

00000064 <.L32>:
  64:	00045703          	lhu	a4,0(s0)
  68:	bfdd                	j	5e <.L39>

0000006a <.L29>:
  6a:	4018                	lw	a4,0(s0)
  6c:	c398                	sw	a4,0(a5)
  6e:	bfe9                	j	48 <.L28>

Disassembly of section .text.cfg_api_element_general_get:

00000000 <cfg_api_element_general_get>:
   0:	4501                	li	a0,0

00000002 <.LVL38>:
   2:	8082                	ret

Disassembly of section .text.cfg_api_element_set:

00000000 <cfg_api_element_set>:
   0:	7179                	addi	sp,sp,-48
   2:	d422                	sw	s0,40(sp)
   4:	d226                	sw	s1,36(sp)
   6:	00000437          	lui	s0,0x0
   a:	000004b7          	lui	s1,0x0
   e:	d04a                	sw	s2,32(sp)
  10:	ce4e                	sw	s3,28(sp)
  12:	cc52                	sw	s4,24(sp)
  14:	ca56                	sw	s5,20(sp)
  16:	c85a                	sw	s6,16(sp)
  18:	c65e                	sw	s7,12(sp)
  1a:	d606                	sw	ra,44(sp)
  1c:	892a                	mv	s2,a0
  1e:	89ae                	mv	s3,a1
  20:	8a32                	mv	s4,a2
  22:	8ab6                	mv	s5,a3
  24:	8b3a                	mv	s6,a4
  26:	00040413          	mv	s0,s0
  2a:	00048493          	mv	s1,s1
  2e:	00000bb7          	lui	s7,0x0

00000032 <.L42>:
  32:	00946563          	bltu	s0,s1,3c <.L46>
  36:	00941e63          	bne	s0,s1,52 <.L47>
  3a:	a00d                	j	5c <.L45>

0000003c <.L46>:
  3c:	401c                	lw	a5,0(s0)
  3e:	05279463          	bne	a5,s2,86 <.L43>
  42:	00445783          	lhu	a5,4(s0) # 4 <cfg_api_element_set+0x4>
  46:	05379063          	bne	a5,s3,86 <.L43>
  4a:	00645703          	lhu	a4,6(s0)
  4e:	03471363          	bne	a4,s4,74 <.L44>

00000052 <.L47>:
  52:	481c                	lw	a5,16(s0)
  54:	865a                	mv	a2,s6
  56:	85d6                	mv	a1,s5
  58:	8522                	mv	a0,s0
  5a:	9782                	jalr	a5

0000005c <.L45>:
  5c:	50b2                	lw	ra,44(sp)
  5e:	5422                	lw	s0,40(sp)

00000060 <.LVL42>:
  60:	5492                	lw	s1,36(sp)
  62:	5902                	lw	s2,32(sp)

00000064 <.LVL43>:
  64:	49f2                	lw	s3,28(sp)

00000066 <.LVL44>:
  66:	4a62                	lw	s4,24(sp)

00000068 <.LVL45>:
  68:	4ad2                	lw	s5,20(sp)

0000006a <.LVL46>:
  6a:	4b42                	lw	s6,16(sp)

0000006c <.LVL47>:
  6c:	4bb2                	lw	s7,12(sp)
  6e:	4501                	li	a0,0
  70:	6145                	addi	sp,sp,48
  72:	8082                	ret

00000074 <.L44>:
  74:	86ce                	mv	a3,s3
  76:	864a                	mv	a2,s2
  78:	85d2                	mv	a1,s4
  7a:	000b8513          	mv	a0,s7
  7e:	00000097          	auipc	ra,0x0
  82:	000080e7          	jalr	ra # 7e <.L44+0xa>

00000086 <.L43>:
  86:	0471                	addi	s0,s0,28
  88:	b76d                	j	32 <.L42>
