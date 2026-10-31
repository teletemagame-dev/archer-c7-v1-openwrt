
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

00092ec4 <WAR_PCI_WRITE32>:
   92ec4:	27bdffd0 	addiu	sp,sp,-48
   92ec8:	3c020000 	lui	v0,0x0
			92ec8: R_MIPS_HI16	war1
   92ecc:	afb50028 	sw	s5,40(sp)
   92ed0:	00c0a821 	move	s5,a2
   92ed4:	afb30020 	sw	s3,32(sp)
   92ed8:	00809821 	move	s3,a0
   92edc:	afb2001c 	sw	s2,28(sp)
   92ee0:	afbf002c 	sw	ra,44(sp)
   92ee4:	afb40024 	sw	s4,36(sp)
   92ee8:	afb10018 	sw	s1,24(sp)
   92eec:	afb00014 	sw	s0,20(sp)
   92ef0:	8c430000 	lw	v1,0(v0)
			92ef0: R_MIPS_LO16	war1
   92ef4:	10600021 	beqz	v1,92f7c <WAR_PCI_WRITE32+0xb8>
   92ef8:	00a09021 	move	s2,a1
   92efc:	41746000 	di	s4
   92f00:	32940001 	andi	s4,s4,0x1
   92f04:	000000c0 	ehb
   92f08:	24b10004 	addiu	s1,a1,4
   92f0c:	3c100000 	lui	s0,0x0
			92f0c: R_MIPS_HI16	ioread32
   92f10:	00918821 	addu	s1,a0,s1
   92f14:	26100000 	addiu	s0,s0,0
			92f14: R_MIPS_LO16	ioread32
   92f18:	0200f809 	jalr	s0
   92f1c:	02202021 	move	a0,s1
   92f20:	0200f809 	jalr	s0
   92f24:	02202021 	move	a0,s1
   92f28:	0200f809 	jalr	s0
   92f2c:	02202021 	move	a0,s1
   92f30:	3c020000 	lui	v0,0x0
			92f30: R_MIPS_HI16	iowrite32
   92f34:	02722821 	addu	a1,s3,s2
   92f38:	24420000 	addiu	v0,v0,0
			92f38: R_MIPS_LO16	iowrite32
   92f3c:	0040f809 	jalr	v0
   92f40:	02a02021 	move	a0,s5
   92f44:	02801821 	move	v1,s4
   92f48:	10600002 	beqz	v1,92f54 <WAR_PCI_WRITE32+0x90>
   92f4c:	41606000 	di
   92f50:	41606020 	ei
   92f54:	000000c0 	ehb
   92f58:	8fbf002c 	lw	ra,44(sp)
   92f5c:	8fb50028 	lw	s5,40(sp)
   92f60:	8fb40024 	lw	s4,36(sp)
   92f64:	8fb30020 	lw	s3,32(sp)
   92f68:	8fb2001c 	lw	s2,28(sp)
   92f6c:	8fb10018 	lw	s1,24(sp)
   92f70:	8fb00014 	lw	s0,20(sp)
   92f74:	03e00008 	jr	ra
   92f78:	27bd0030 	addiu	sp,sp,48
   92f7c:	3c190000 	lui	t9,0x0
			92f7c: R_MIPS_HI16	iowrite32
   92f80:	8fbf002c 	lw	ra,44(sp)
   92f84:	00852821 	addu	a1,a0,a1
   92f88:	8fb50028 	lw	s5,40(sp)
   92f8c:	8fb40024 	lw	s4,36(sp)
   92f90:	27390000 	addiu	t9,t9,0
			92f90: R_MIPS_LO16	iowrite32
   92f94:	8fb30020 	lw	s3,32(sp)
   92f98:	00c02021 	move	a0,a2
   92f9c:	8fb2001c 	lw	s2,28(sp)
   92fa0:	8fb10018 	lw	s1,24(sp)
   92fa4:	8fb00014 	lw	s0,20(sp)
   92fa8:	03200008 	jr	t9
   92fac:	27bd0030 	addiu	sp,sp,48

/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

000a41f8 <ath_pci_device_reset>:
   a41f8:	27bdffd0 	addiu	sp,sp,-48
   a41fc:	afb50024 	sw	s5,36(sp)
   a4200:	3c150000 	lui	s5,0x0
			a4200: R_MIPS_HI16	ath_hostdef
   a4204:	afbf002c 	sw	ra,44(sp)
   a4208:	afb60028 	sw	s6,40(sp)
   a420c:	afb40020 	sw	s4,32(sp)
   a4210:	afb3001c 	sw	s3,28(sp)
   a4214:	afb20018 	sw	s2,24(sp)
   a4218:	afb10014 	sw	s1,20(sp)
   a421c:	afb00010 	sw	s0,16(sp)
   a4220:	8c910000 	lw	s1,0(a0)
   a4224:	8ea40000 	lw	a0,0(s5)
			a4224: R_MIPS_LO16	ath_hostdef
   a4228:	8c820094 	lw	v0,148(a0)
   a422c:	10400046 	beqz	v0,a4348 <ath_pci_device_reset+0x150>
   a4230:	8fbf002c 	lw	ra,44(sp)
   a4234:	12200044 	beqz	s1,a4348 <ath_pci_device_reset+0x150>
   a4238:	3c020000 	lui	v0,0x0
			a4238: R_MIPS_HI16	iowrite32
   a423c:	8c8300a0 	lw	v1,160(a0)
   a4240:	8c8500a8 	lw	a1,168(a0)
   a4244:	00008021 	move	s0,zero
   a4248:	8c8400ac 	lw	a0,172(a0)
   a424c:	24560000 	addiu	s6,v0,0
			a424c: R_MIPS_LO16	iowrite32
   a4250:	2414000a 	li	s4,10
   a4254:	00a32821 	addu	a1,a1,v1
   a4258:	02c0f809 	jalr	s6
   a425c:	02252821 	addu	a1,s1,a1
   a4260:	3c020000 	lui	v0,0x0
			a4260: R_MIPS_HI16	ath_pci_targ_is_awake
   a4264:	3c030000 	lui	v1,0x0
			a4264: R_MIPS_HI16	__udelay
   a4268:	24520000 	addiu	s2,v0,0
			a4268: R_MIPS_LO16	ath_pci_targ_is_awake
   a426c:	24730000 	addiu	s3,v1,0
			a426c: R_MIPS_LO16	__udelay
   a4270:	0240f809 	jalr	s2
   a4274:	02202021 	move	a0,s1
   a4278:	26100001 	addiu	s0,s0,1
   a427c:	14400005 	bnez	v0,a4294 <ath_pci_device_reset+0x9c>
   a4280:	240403e8 	li	a0,1000
   a4284:	0260f809 	jalr	s3
   a4288:	00000000 	nop
   a428c:	1614fff8 	bne	s0,s4,a4270 <ath_pci_device_reset+0x78>
   a4290:	00000000 	nop
   a4294:	8ea20000 	lw	v0,0(s5)
			a4294: R_MIPS_LO16	ath_hostdef
   a4298:	8c4300a0 	lw	v1,160(v0)
   a429c:	8c440094 	lw	a0,148(v0)
   a42a0:	00832021 	addu	a0,a0,v1
   a42a4:	3c030000 	lui	v1,0x0
			a42a4: R_MIPS_HI16	ioread32
   a42a8:	24630000 	addiu	v1,v1,0
			a42a8: R_MIPS_LO16	ioread32
   a42ac:	0060f809 	jalr	v1
   a42b0:	02242021 	addu	a0,s1,a0
   a42b4:	8ea60000 	lw	a2,0(s5)
			a42b4: R_MIPS_LO16	ath_hostdef
   a42b8:	34500001 	ori	s0,v0,0x1
   a42bc:	02002021 	move	a0,s0
   a42c0:	8cc200a0 	lw	v0,160(a2)
   a42c4:	8cc50094 	lw	a1,148(a2)
   a42c8:	00a22821 	addu	a1,a1,v0
   a42cc:	02c0f809 	jalr	s6
   a42d0:	02252821 	addu	a1,s1,a1
   a42d4:	0260f809 	jalr	s3
   a42d8:	24040bb8 	li	a0,3000
   a42dc:	2404fffe 	li	a0,-2
   a42e0:	8ea30000 	lw	v1,0(s5)
			a42e0: R_MIPS_LO16	ath_hostdef
   a42e4:	02042024 	and	a0,s0,a0
   a42e8:	8c6200a0 	lw	v0,160(v1)
   a42ec:	8c650094 	lw	a1,148(v1)
   a42f0:	00a22821 	addu	a1,a1,v0
   a42f4:	02c0f809 	jalr	s6
   a42f8:	02252821 	addu	a1,s1,a1
   a42fc:	0260f809 	jalr	s3
   a4300:	24040bb8 	li	a0,3000
   a4304:	02c0c821 	move	t9,s6
   a4308:	8ea20000 	lw	v0,0(s5)
			a4308: R_MIPS_LO16	ath_hostdef
   a430c:	8fbf002c 	lw	ra,44(sp)
   a4310:	8fb60028 	lw	s6,40(sp)
   a4314:	8fb50024 	lw	s5,36(sp)
   a4318:	8c4500a8 	lw	a1,168(v0)
   a431c:	8c4300a0 	lw	v1,160(v0)
   a4320:	8c4400a4 	lw	a0,164(v0)
   a4324:	8fb40020 	lw	s4,32(sp)
   a4328:	00a32821 	addu	a1,a1,v1
   a432c:	8fb3001c 	lw	s3,28(sp)
   a4330:	8fb20018 	lw	s2,24(sp)
   a4334:	02252821 	addu	a1,s1,a1
   a4338:	8fb00010 	lw	s0,16(sp)
   a433c:	8fb10014 	lw	s1,20(sp)
   a4340:	03200008 	jr	t9
   a4344:	27bd0030 	addiu	sp,sp,48
   a4348:	8fb60028 	lw	s6,40(sp)
   a434c:	8fb50024 	lw	s5,36(sp)
   a4350:	8fb40020 	lw	s4,32(sp)
   a4354:	8fb3001c 	lw	s3,28(sp)
   a4358:	8fb20018 	lw	s2,24(sp)
   a435c:	8fb10014 	lw	s1,20(sp)
   a4360:	8fb00010 	lw	s0,16(sp)
   a4364:	03e00008 	jr	ra
   a4368:	27bd0030 	addiu	sp,sp,48
