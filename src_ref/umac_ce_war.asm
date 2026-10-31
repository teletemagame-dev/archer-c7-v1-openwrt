
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

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
   9304c:	3c020000 	lui	v0,0x0
			9304c: R_MIPS_HI16	WAR_PCI_WRITE32
   93050:	8e840000 	lw	a0,0(s4)
   93054:	2665003c 	addiu	a1,s3,60
   93058:	24420000 	addiu	v0,v0,0
			93058: R_MIPS_LO16	WAR_PCI_WRITE32
   9305c:	0040f809 	jalr	v0
   93060:	02c03021 	move	a2,s6
   93064:	00002021 	move	a0,zero
   93068:	0220f809 	jalr	s1
   9306c:	02402821 	move	a1,s2
   93070:	02a01021 	move	v0,s5
   93074:	10400002 	beqz	v0,93080 <WAR_CE_SRC_RING_WRITE_IDX_SET+0xd0>
   93078:	41606000 	di
   9307c:	41606020 	ei
   93080:	000000c0 	ehb
   93084:	8fbf002c 	lw	ra,44(sp)
   93088:	8fb60028 	lw	s6,40(sp)
   9308c:	8fb50024 	lw	s5,36(sp)
   93090:	8fb40020 	lw	s4,32(sp)
   93094:	8fb3001c 	lw	s3,28(sp)
   93098:	8fb20018 	lw	s2,24(sp)
   9309c:	8fb10014 	lw	s1,20(sp)
   930a0:	8fb00010 	lw	s0,16(sp)
   930a4:	03e00008 	jr	ra
   930a8:	27bd0030 	addiu	sp,sp,48
   930ac:	3c190000 	lui	t9,0x0
			930ac: R_MIPS_HI16	WAR_PCI_WRITE32
   930b0:	8c840000 	lw	a0,0(a0)
   930b4:	8fbf002c 	lw	ra,44(sp)
   930b8:	24a5003c 	addiu	a1,a1,60
   930bc:	8fb60028 	lw	s6,40(sp)
   930c0:	27390000 	addiu	t9,t9,0
			930c0: R_MIPS_LO16	WAR_PCI_WRITE32
   930c4:	8fb50024 	lw	s5,36(sp)
   930c8:	8fb40020 	lw	s4,32(sp)
   930cc:	8fb3001c 	lw	s3,28(sp)
   930d0:	8fb20018 	lw	s2,24(sp)
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
