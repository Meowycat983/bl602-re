void agc_config(void)

{
  uint uVar1;
  
  uVar1 = read_volatile_4(DAT_44c0b390);
  write_volatile_4(DAT_44c0b390,uVar1 & 0xfffeffff);
  uVar1 = read_volatile_4(DAT_44c0b390);
  write_volatile_4(DAT_44c0b390,uVar1 & 0xfffffbff);
  uVar1 = read_volatile_4(DAT_44c0b3a4);
  write_volatile_4(DAT_44c0b3a4,uVar1 & 0xffffff00);
  uVar1 = read_volatile_4(DAT_44c0b3a4);
  write_volatile_4(DAT_44c0b3a4,uVar1 & 0xffff00ff);
  uVar1 = read_volatile_4(DAT_44c0b394);
  write_volatile_4(DAT_44c0b394,uVar1 & 0xff00ffff | 0xf80000);
  uVar1 = read_volatile_4(DAT_44c0b398);
  write_volatile_4(DAT_44c0b398,uVar1 & 0xffff00ff | 0x9e00);
  uVar1 = read_volatile_4(DAT_44c0b3c4);
  write_volatile_4(DAT_44c0b3c4,uVar1 & 0xffffff00 | 0xce);
  uVar1 = read_volatile_4(DAT_44c0b364);
  write_volatile_4(DAT_44c0b364,uVar1 & 0xe0ffffff | 0x8000000);
  uVar1 = read_volatile_4(DAT_44c0b364);
  write_volatile_4(DAT_44c0b364,uVar1 & 0xffc0ffff | 0x3c0000);
  uVar1 = read_volatile_4(DAT_44c0b364);
  write_volatile_4(DAT_44c0b364,uVar1 & 0xffffc0ff | 0x3800);
  uVar1 = read_volatile_4(DAT_44c0b364);
  write_volatile_4(DAT_44c0b364,uVar1 & 0xffffffc0 | 0x39);
  uVar1 = read_volatile_4(DAT_44c0b368);
  write_volatile_4(DAT_44c0b368,uVar1 & 0xffc00fff | 0x70000);
  uVar1 = read_volatile_4(DAT_44c0b368);
  write_volatile_4(DAT_44c0b368,uVar1 & 0xfffffc00 | 0x70);
  uVar1 = read_volatile_4(DAT_44c0b36c);
  write_volatile_4(DAT_44c0b36c,uVar1 & 0xffffff00 | 0x12);
  uVar1 = read_volatile_4(DAT_44c0b36c);
  write_volatile_4(DAT_44c0b36c,uVar1 & 0xfffff8ff | 0x500);
  uVar1 = read_volatile_4(DAT_44c0b36c);
  write_volatile_4(DAT_44c0b36c,uVar1 & 0xff00ffff | 0x280000);
  uVar1 = read_volatile_4(DAT_44c0b36c);
  write_volatile_4(DAT_44c0b36c,uVar1 & 0xf8ffffff | 0x7000000);
  uVar1 = read_volatile_4(DAT_44c0b370);
  write_volatile_4(DAT_44c0b370,uVar1 & 0xff80ffff | 0x580000);
  uVar1 = read_volatile_4(DAT_44c0b3c0);
  write_volatile_4(DAT_44c0b3c0,uVar1 & 0xffffff | 0x18000000);
  uVar1 = read_volatile_4(DAT_44c0b380);
  write_volatile_4(DAT_44c0b380,uVar1 & 0xfff03fff | 0xf8000);
  uVar1 = read_volatile_4(DAT_44c0b380);
  write_volatile_4(DAT_44c0b380,uVar1 & 0xfc0fffff | 0x3700000);
  uVar1 = read_volatile_4(DAT_44c0b380);
  write_volatile_4(DAT_44c0b380,uVar1 & 0x3ffffff | 0x4000000);
  uVar1 = read_volatile_4(DAT_44c0b380);
  write_volatile_4(DAT_44c0b380,uVar1 & 0xffffdfff);
  uVar1 = read_volatile_4(DAT_44c0b380);
  write_volatile_4(DAT_44c0b380,uVar1 & 0xffffe3ff | 0x400);
  uVar1 = read_volatile_4(DAT_44c0b384);
  write_volatile_4(DAT_44c0b384,uVar1 & 0x3ffffff | 0xe4000000);
  uVar1 = read_volatile_4(DAT_44c0b384);
  write_volatile_4(DAT_44c0b384,uVar1 & 0xfc0fffff | 0x3700000);
  uVar1 = read_volatile_4(DAT_44c0b384);
  write_volatile_4(DAT_44c0b384,uVar1 & 0xfff03fff | 0x50000);
  uVar1 = read_volatile_4(DAT_44c0b384);
  write_volatile_4(DAT_44c0b384,uVar1 & 0xffffdfff);
  uVar1 = read_volatile_4(DAT_44c0b384);
  write_volatile_4(DAT_44c0b384,uVar1 & 0xffffe3ff | 0x800);
  uVar1 = read_volatile_4(DAT_44c0b388);
  write_volatile_4(DAT_44c0b388,uVar1 & 0x3ffffff | 0x3c000000);
  uVar1 = read_volatile_4(DAT_44c0b388);
  write_volatile_4(DAT_44c0b388,uVar1 & 0xfc0fffff | 0x1700000);
  uVar1 = read_volatile_4(DAT_44c0b388);
  write_volatile_4(DAT_44c0b388,uVar1 & 0xfff03fff | 0xa8000);
  uVar1 = read_volatile_4(DAT_44c0b388);
  write_volatile_4(DAT_44c0b388,uVar1 & 0xffffdfff);
  uVar1 = read_volatile_4(DAT_44c0b388);
  write_volatile_4(DAT_44c0b388,uVar1 & 0xffffe3ff | 0x1400);
  uVar1 = read_volatile_4(DAT_44c0b38c);
  write_volatile_4(DAT_44c0b38c,uVar1 & 0x3ffffff | 0x64000000);
  uVar1 = read_volatile_4(DAT_44c0b38c);
  write_volatile_4(DAT_44c0b38c,uVar1 & 0xfc0fffff);
  uVar1 = read_volatile_4(DAT_44c0b38c);
  write_volatile_4(DAT_44c0b38c,uVar1 & 0xfff03fff | 0x38000);
  uVar1 = read_volatile_4(DAT_44c0b38c);
  write_volatile_4(DAT_44c0b38c,uVar1 & 0xffffe3ff | 0x800);
  uVar1 = read_volatile_4(DAT_44c0c830);
  write_volatile_4(DAT_44c0c830,uVar1 & 0x3ffffff | 0xfc000000);
  uVar1 = read_volatile_4(DAT_44c0c830);
  write_volatile_4(DAT_44c0c830,uVar1 & 0xfc0fffff | 0x100000);
  uVar1 = read_volatile_4(DAT_44c0c830);
  write_volatile_4(DAT_44c0c830,uVar1 & 0xfff03fff | 0xd8000);
  uVar1 = read_volatile_4(DAT_44c0c830);
  write_volatile_4(DAT_44c0c830,uVar1 & 0xffffe3ff | 0x1400);
  uVar1 = read_volatile_4(DAT_44c0c814);
  write_volatile_4(DAT_44c0c814,uVar1 & 0xfffffffc);
  uVar1 = read_volatile_4(DAT_44c0c814);
  write_volatile_4(DAT_44c0c814,uVar1 & 0xffffffc3 | 8);
  uVar1 = read_volatile_4(DAT_44c0c814);
  write_volatile_4(DAT_44c0c814,uVar1 & 0xffffffc3 | 8);
  uVar1 = read_volatile_4(DAT_44c0c040);
  write_volatile_4(DAT_44c0c040,uVar1 & 0xfe0fffff | 0xc00000);
  uVar1 = read_volatile_4(DAT_44c0c040);
  write_volatile_4(DAT_44c0c040,uVar1 & 0xfff07fff | 0x18000);
  uVar1 = read_volatile_4(DAT_44c0c044);
  write_volatile_4(DAT_44c0c044,uVar1 & 0xffff00ff | 0x800);
  uVar1 = read_volatile_4(DAT_44c0c044);
  write_volatile_4(DAT_44c0c044,uVar1 & 0xffffff00);
  phy_config_rxgain(0);
  uVar1 = read_volatile_4(DAT_44c0b3a0);
  write_volatile_4(DAT_44c0b3a0,uVar1 & 0xffffff00 | 0x9e);
  uVar1 = read_volatile_4(DAT_44c0b3c0);
  write_volatile_4(DAT_44c0b3c0,uVar1 & 0xffffff00 | 0xa4);
  uVar1 = read_volatile_4(DAT_44c0b3c0);
  write_volatile_4(DAT_44c0b3c0,uVar1 & 0xffff00ff | 0xa300);
  uVar1 = read_volatile_4(DAT_44c0c82c);
  write_volatile_4(DAT_44c0c82c,uVar1 & 0xffffff00 | 0xb5);
  uVar1 = read_volatile_4(DAT_44c0c82c);
  write_volatile_4(DAT_44c0c82c,uVar1 | 0x100);
  uVar1 = read_volatile_4(DAT_44c0c82c);
  write_volatile_4(DAT_44c0c82c,uVar1 & 0xfffff7ff | 0x800);
  uVar1 = read_volatile_4(DAT_44c0c838);
  write_volatile_4(DAT_44c0c838,uVar1 & 0x7fffffff | 0x80000000);
  uVar1 = read_volatile_4(DAT_44c0c838);
  write_volatile_4(DAT_44c0c838,uVar1 & 0xfff80000 | 0x100);
  uVar1 = read_volatile_4(DAT_44c0c83c);
  write_volatile_4(DAT_44c0c83c,uVar1 & 0x7fffffff | 0x80000000);
  uVar1 = read_volatile_4(DAT_44c0c83c);
  write_volatile_4(DAT_44c0c83c,uVar1 & 0xfff00000 | 0x17c);
  uVar1 = read_volatile_4(DAT_44c0c840);
  write_volatile_4(DAT_44c0c840,uVar1 & 0x7fffffff | 0x80000000);
  uVar1 = read_volatile_4(DAT_44c0c840);
  write_volatile_4(DAT_44c0c840,uVar1 & 0xffc00000 | 0x100);
  uVar1 = read_volatile_4(DAT_44c0c82c);
  write_volatile_4(DAT_44c0c82c,uVar1 & 0xff007fff | 0x200000);
  gp = (code *)((int)SFlash_Cache_Hit_Count_Get + 6);
  return;
}