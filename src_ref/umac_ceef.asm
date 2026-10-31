   92ec0:	aca20094 	sw	v0,148(a1)

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
--
   92fac:	27bd0030 	addiu	sp,sp,48

00092fb0 <WAR_CE_SRC_RING_WRITE_IDX_SET>:
   92fb0:	27bdffd0 	addiu	sp,sp,-48
   92fb4:	3c020000 	lui	v0,0x0
			92fb4: R_MIPS_HI16	war1
   92fb8:	afb60028 	sw	s6,40(sp)
   92fbc:	00c0b021 	move	s6,a2
   92fc0:	afb40020 	sw	s4,32(sp)
   92fc4:	0080a021 	move	s4,a0
   92fc8:	afb3001c 	sw	s3,28(sp)
   92fcc:	afbf002c 	sw	ra,44(sp)
   92fd0:	afb50024 	sw	s5,36(sp)
   92fd4:	afb20018 	sw	s2,24(sp)
   92fd8:	afb10014 	sw	s1,20(sp)
   92fdc:	afb00010 	sw	s0,16(sp)
   92fe0:	8c430000 	lw	v1,0(v0)
			92fe0: R_MIPS_LO16	war1
   92fe4:	10600031 	beqz	v1,930ac <WAR_CE_SRC_RING_WRITE_IDX_SET+0xfc>
   92fe8:	00a09821 	move	s3,a1
   92fec:	3c020000 	lui	v0,0x0
			92fec: R_MIPS_HI16	war1_allow_sleep
   92ff0:	8c850000 	lw	a1,0(a0)
   92ff4:	26640050 	addiu	a0,s3,80
   92ff8:	8c430000 	lw	v1,0(v0)
			92ff8: R_MIPS_LO16	war1_allow_sleep
   92ffc:	14600005 	bnez	v1,93014 <WAR_CE_SRC_RING_WRITE_IDX_SET+0x64>
   93000:	00a49021 	addu	s2,a1,a0
   93004:	3c020005 	lui	v0,0x5
   93008:	34428400 	ori	v0,v0,0x8400
   9300c:	12620035 	beq	s3,v0,930e4 <WAR_CE_SRC_RING_WRITE_IDX_SET+0x134>
   93010:	3c190000 	lui	t9,0x0
			93010: R_MIPS_HI16	iowrite32
   93014:	41756000 	di	s5
   93018:	32b50001 	andi	s5,s5,0x1
   9301c:	000000c0 	ehb
   93020:	3c110000 	lui	s1,0x0
			93020: R_MIPS_HI16	iowrite32
   93024:	3c100000 	lui	s0,0x0
			93024: R_MIPS_HI16	ioread32
   93028:	26310000 	addiu	s1,s1,0
			93028: R_MIPS_LO16	iowrite32
   9302c:	24040001 	li	a0,1
   93030:	02402821 	move	a1,s2
   93034:	0220f809 	jalr	s1
   93038:	26100000 	addiu	s0,s0,0
			93038: R_MIPS_LO16	ioread32
   9303c:	0200f809 	jalr	s0
   93040:	02402021 	move	a0,s2
   93044:	0200f809 	jalr	s0
   93048:	02402021 	move	a0,s2
--
   930d4:	8fb10014 	lw	s1,20(sp)
   930d8:	8fb00010 	lw	s0,16(sp)
   930dc:	03200008 	jr	t9
   930e0:	27bd0030 	addiu	sp,sp,48
   930e4:	8fbf002c 	lw	ra,44(sp)
   930e8:	3c04ceef 	lui	a0,0xceef
   930ec:	8fb60028 	lw	s6,40(sp)
   930f0:	02402821 	move	a1,s2
   930f4:	8fb50024 	lw	s5,36(sp)
   930f8:	8fb40020 	lw	s4,32(sp)
   930fc:	27390000 	addiu	t9,t9,0
			930fc: R_MIPS_LO16	iowrite32
   93100:	8fb3001c 	lw	s3,28(sp)
   93104:	00c42025 	or	a0,a2,a0
   93108:	8fb20018 	lw	s2,24(sp)
   9310c:	8fb10014 	lw	s1,20(sp)
   93110:	8fb00010 	lw	s0,16(sp)
   93114:	03200008 	jr	t9
   93118:	27bd0030 	addiu	sp,sp,48

0009311c <ol_ath_diag_user_agent_fini>:
   9311c:	3c190000 	lui	t9,0x0
			9311c: R_MIPS_HI16	ath_sysfs_diag_fini
   93120:	27390000 	addiu	t9,t9,0
			93120: R_MIPS_LO16	ath_sysfs_diag_fini
   93124:	03200008 	jr	t9
   93128:	00000000 	nop

0009312c <ol_ath_diag_user_agent_init>:
   9312c:	3c190000 	lui	t9,0x0
			9312c: R_MIPS_HI16	ath_sysfs_diag_init
