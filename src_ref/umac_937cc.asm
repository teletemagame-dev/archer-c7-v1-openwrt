
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

000937cc <ol_transfer_bin_file>:
   937cc:	27bdffb8 	addiu	sp,sp,-72
   937d0:	2ca20005 	sltiu	v0,a1,5
   937d4:	afbe0040 	sw	s8,64(sp)
   937d8:	00c0f021 	move	s8,a2
   937dc:	afb7003c 	sw	s7,60(sp)
   937e0:	30f700ff 	andi	s7,a3,0xff
   937e4:	afb60038 	sw	s6,56(sp)
   937e8:	0080b021 	move	s6,a0
   937ec:	afb50034 	sw	s5,52(sp)
   937f0:	00a0a821 	move	s5,a1
   937f4:	afbf0044 	sw	ra,68(sp)
   937f8:	afb40030 	sw	s4,48(sp)
   937fc:	afb3002c 	sw	s3,44(sp)
   93800:	afb20028 	sw	s2,40(sp)
   93804:	afb10024 	sw	s1,36(sp)
   93808:	14400016 	bnez	v0,93864 <ol_transfer_bin_file+0x98>
   9380c:	afb00020 	sw	s0,32(sp)
   93810:	3c040000 	lui	a0,0x0
			93810: R_MIPS_HI16	$LC8
   93814:	24840000 	addiu	a0,a0,0
			93814: R_MIPS_LO16	$LC8
   93818:	3c050001 	lui	a1,0x1
			93818: R_MIPS_HI16	.rodata
   9381c:	3c030000 	lui	v1,0x0
			9381c: R_MIPS_HI16	printk
   93820:	24a5a8a0 	addiu	a1,a1,-22368
			93820: R_MIPS_LO16	.rodata
   93824:	24630000 	addiu	v1,v1,0
			93824: R_MIPS_LO16	printk
   93828:	0060f809 	jalr	v1
   9382c:	2410ffff 	li	s0,-1
   93830:	8fbf0044 	lw	ra,68(sp)
   93834:	02001021 	move	v0,s0
   93838:	8fbe0040 	lw	s8,64(sp)
   9383c:	8fb7003c 	lw	s7,60(sp)
   93840:	8fb60038 	lw	s6,56(sp)
   93844:	8fb50034 	lw	s5,52(sp)
   93848:	8fb40030 	lw	s4,48(sp)
   9384c:	8fb3002c 	lw	s3,44(sp)
   93850:	8fb20028 	lw	s2,40(sp)
   93854:	8fb10024 	lw	s1,36(sp)
   93858:	8fb00020 	lw	s0,32(sp)
   9385c:	03e00008 	jr	ra
   93860:	27bd0048 	addiu	sp,sp,72
   93864:	3c020001 	lui	v0,0x1
			93864: R_MIPS_HI16	.rodata
   93868:	00051880 	sll	v1,a1,0x2
   9386c:	2442a870 	addiu	v0,v0,-22416
			9386c: R_MIPS_LO16	.rodata
   93870:	7c43100a 	lwx	v0,v1(v0)
   93874:	00400008 	jr	v0
   93878:	00000000 	nop
   9387c:	3c023000 	lui	v0,0x3000
   93880:	8c833610 	lw	v1,13840(a0)
   93884:	34420623 	ori	v0,v0,0x623
   93888:	10620009 	beq	v1,v0,938b0 <ol_transfer_bin_file+0xe4>
   9388c:	3c044000 	lui	a0,0x4000
   93890:	3482002c 	ori	v0,a0,0x2c
   93894:	10620006 	beq	v1,v0,938b0 <ol_transfer_bin_file+0xe4>
   93898:	3482270f 	ori	v0,a0,0x270f
   9389c:	10620004 	beq	v1,v0,938b0 <ol_transfer_bin_file+0xe4>
   938a0:	3c024100 	lui	v0,0x4100
   938a4:	3442006b 	ori	v0,v0,0x6b
   938a8:	146201c7 	bne	v1,v0,93fc8 <ol_transfer_bin_file+0x7fc>
   938ac:	3c040000 	lui	a0,0x0
			938ac: R_MIPS_HI16	$LC9
   938b0:	3c040000 	lui	a0,0x0
			938b0: R_MIPS_HI16	$LC18
   938b4:	3c050001 	lui	a1,0x1
			938b4: R_MIPS_HI16	.rodata
   938b8:	3c030000 	lui	v1,0x0
			938b8: R_MIPS_HI16	printk
   938bc:	3c020000 	lui	v0,0x0
			938bc: R_MIPS_HI16	otp_bin
   938c0:	24840000 	addiu	a0,a0,0
			938c0: R_MIPS_LO16	$LC18
   938c4:	24a5a8a0 	addiu	a1,a1,-22368
			938c4: R_MIPS_LO16	.rodata
   938c8:	240605f7 	li	a2,1527
   938cc:	24070df4 	li	a3,3572
   938d0:	24630000 	addiu	v1,v1,0
			938d0: R_MIPS_LO16	printk
   938d4:	24100df1 	li	s0,3569
   938d8:	24120df4 	li	s2,3572
   938dc:	0060f809 	jalr	v1
   938e0:	24530000 	addiu	s3,v0,0
			938e0: R_MIPS_LO16	otp_bin
   938e4:	3c020000 	lui	v0,0x0
			938e4: R_MIPS_HI16	amalloc_private
   938e8:	00002021 	move	a0,zero
   938ec:	24540000 	addiu	s4,v0,0
			938ec: R_MIPS_LO16	amalloc_private
   938f0:	00003021 	move	a2,zero
   938f4:	0280f809 	jalr	s4
   938f8:	02402821 	move	a1,s2
   938fc:	00408821 	move	s1,v0
   93900:	00002821 	move	a1,zero
   93904:	08024e4a 	j	93928 <ol_transfer_bin_file+0x15c>
			93904: R_MIPS_26	.text
   93908:	00001821 	move	v1,zero
   9390c:	02232021 	addu	a0,s1,v1
   93910:	24a50001 	addiu	a1,a1,1
   93914:	90430000 	lbu	v1,0(v0)
   93918:	00b2102b 	sltu	v0,a1,s2
   9391c:	a0830000 	sb	v1,0(a0)
   93920:	1040000a 	beqz	v0,9394c <ol_transfer_bin_file+0x180>
   93924:	00a01821 	move	v1,a1
   93928:	0070102b 	sltu	v0,v1,s0
   9392c:	1440fff7 	bnez	v0,9390c <ol_transfer_bin_file+0x140>
   93930:	02631021 	addu	v0,s3,v1
   93934:	02231021 	addu	v0,s1,v1
   93938:	24a50001 	addiu	a1,a1,1
   9393c:	a0400000 	sb	zero,0(v0)
   93940:	00b2102b 	sltu	v0,a1,s2
   93944:	1440fff8 	bnez	v0,93928 <ol_transfer_bin_file+0x15c>
   93948:	00a01821 	move	v1,a1
   9394c:	00123082 	srl	a2,s2,0x2
   93950:	10c0000e 	beqz	a2,9398c <ol_transfer_bin_file+0x1c0>
   93954:	26a2fffd 	addiu	v0,s5,-3
   93958:	00002821 	move	a1,zero
   9395c:	08024e5b 	j	9396c <ol_transfer_bin_file+0x1a0>
			9395c: R_MIPS_26	.text
   93960:	02202021 	move	a0,s1
   93964:	24840004 	addiu	a0,a0,4
   93968:	26730004 	addiu	s3,s3,4
   9396c:	24a50001 	addiu	a1,a1,1
   93970:	8e620000 	lw	v0,0(s3)
   93974:	7c0210a0 	wsbh	v0,v0
   93978:	00221402 	ror	v0,v0,0x10
   9397c:	00a6182b 	sltu	v1,a1,a2
   93980:	1460fff8 	bnez	v1,93964 <ol_transfer_bin_file+0x198>
   93984:	ac820000 	sw	v0,0(a0)
   93988:	26a2fffd 	addiu	v0,s5,-3
   9398c:	2c500002 	sltiu	s0,v0,2
   93990:	16000074 	bnez	s0,93b64 <ol_transfer_bin_file+0x398>
   93994:	00000000 	nop
   93998:	00009821 	move	s3,zero
   9399c:	02403021 	move	a2,s2
   939a0:	16e0009d 	bnez	s7,93c18 <ol_transfer_bin_file+0x44c>
   939a4:	3c030000 	lui	v1,0x0
			939a4: R_MIPS_HI16	BMIFastDownload
   939a8:	120000a4 	beqz	s0,93c3c <ol_transfer_bin_file+0x470>
   939ac:	3c030000 	lui	v1,0x0
			939ac: R_MIPS_HI16	BMIWriteMemory
   939b0:	122000a2 	beqz	s1,93c3c <ol_transfer_bin_file+0x470>
   939b4:	00c03821 	move	a3,a2
   939b8:	8ec43654 	lw	a0,13908(s6)
   939bc:	afb60010 	sw	s6,16(sp)
   939c0:	24630000 	addiu	v1,v1,0
			939c0: R_MIPS_LO16	BMIWriteMemory
   939c4:	03c02821 	move	a1,s8
   939c8:	0060f809 	jalr	v1
   939cc:	02603021 	move	a2,s3
   939d0:	00408021 	move	s0,v0
   939d4:	12600005 	beqz	s3,939ec <ol_transfer_bin_file+0x220>
   939d8:	3c020000 	lui	v0,0x0
			939d8: R_MIPS_HI16	afree_private
   939dc:	00002021 	move	a0,zero
   939e0:	24420000 	addiu	v0,v0,0
			939e0: R_MIPS_LO16	afree_private
   939e4:	0040f809 	jalr	v0
   939e8:	02602821 	move	a1,s3
   939ec:	12200005 	beqz	s1,93a04 <ol_transfer_bin_file+0x238>
   939f0:	3c020000 	lui	v0,0x0
			939f0: R_MIPS_HI16	afree_private
   939f4:	00002021 	move	a0,zero
   939f8:	24420000 	addiu	v0,v0,0
			939f8: R_MIPS_LO16	afree_private
   939fc:	0040f809 	jalr	v0
   93a00:	02202821 	move	a1,s1
   93a04:	5200ff8b 	beqzl	s0,93834 <ol_transfer_bin_file+0x68>
   93a08:	8fbf0044 	lw	ra,68(sp)
   93a0c:	3c040000 	lui	a0,0x0
			93a0c: R_MIPS_HI16	$LC28
   93a10:	3c030000 	lui	v1,0x0
			93a10: R_MIPS_HI16	printk
   93a14:	24840000 	addiu	a0,a0,0
			93a14: R_MIPS_LO16	$LC28
   93a18:	2405068d 	li	a1,1677
   93a1c:	24630000 	addiu	v1,v1,0
			93a1c: R_MIPS_LO16	printk
   93a20:	0060f809 	jalr	v1
   93a24:	2410ffff 	li	s0,-1
   93a28:	08024e0d 	j	93834 <ol_transfer_bin_file+0x68>
			93a28: R_MIPS_26	.text
   93a2c:	8fbf0044 	lw	ra,68(sp)
   93a30:	3c020000 	lui	v0,0x0
			93a30: R_MIPS_HI16	testmode
   93a34:	8c430000 	lw	v1,0(v0)
			93a34: R_MIPS_LO16	testmode
   93a38:	106000d8 	beqz	v1,93d9c <ol_transfer_bin_file+0x5d0>
   93a3c:	3c023000 	lui	v0,0x3000
   93a40:	24020001 	li	v0,1
   93a44:	10620116 	beq	v1,v0,93ea0 <ol_transfer_bin_file+0x6d4>
   93a48:	3c023000 	lui	v0,0x3000
   93a4c:	24020003 	li	v0,3
   93a50:	52a20125 	beql	s5,v0,93ee8 <ol_transfer_bin_file+0x71c>
   93a54:	3c040000 	lui	a0,0x0
			93a54: R_MIPS_HI16	$LC19
   93a58:	24020001 	li	v0,1
   93a5c:	12a20080 	beq	s5,v0,93c60 <ol_transfer_bin_file+0x494>
   93a60:	24020004 	li	v0,4
   93a64:	12a2009d 	beq	s5,v0,93cdc <ol_transfer_bin_file+0x510>
   93a68:	3c020000 	lui	v0,0x0
			93a68: R_MIPS_HI16	amalloc_private
   93a6c:	00009021 	move	s2,zero
   93a70:	24540000 	addiu	s4,v0,0
			93a70: R_MIPS_LO16	amalloc_private
   93a74:	00002021 	move	a0,zero
   93a78:	00003021 	move	a2,zero
   93a7c:	0280f809 	jalr	s4
   93a80:	02402821 	move	a1,s2
   93a84:	1640ff9e 	bnez	s2,93900 <ol_transfer_bin_file+0x134>
   93a88:	00408821 	move	s1,v0
   93a8c:	08024e63 	j	9398c <ol_transfer_bin_file+0x1c0>
			93a8c: R_MIPS_26	.text
   93a90:	26a2fffd 	addiu	v0,s5,-3
   93a94:	3c023000 	lui	v0,0x3000
   93a98:	8c863610 	lw	a2,13840(a0)
   93a9c:	34420623 	ori	v0,v0,0x623
   93aa0:	10c20124 	beq	a2,v0,93f34 <ol_transfer_bin_file+0x768>
   93aa4:	3c034000 	lui	v1,0x4000
   93aa8:	3462002c 	ori	v0,v1,0x2c
   93aac:	50c20132 	beql	a2,v0,93f78 <ol_transfer_bin_file+0x7ac>
   93ab0:	3c040000 	lui	a0,0x0
			93ab0: R_MIPS_HI16	$LC13
   93ab4:	3462270f 	ori	v0,v1,0x270f
   93ab8:	50c2012d 	beql	a2,v0,93f70 <ol_transfer_bin_file+0x7a4>
   93abc:	3c040000 	lui	a0,0x0
			93abc: R_MIPS_HI16	$LC14
   93ac0:	3c024100 	lui	v0,0x4100
   93ac4:	3442006b 	ori	v0,v0,0x6b
   93ac8:	14c20126 	bne	a2,v0,93f64 <ol_transfer_bin_file+0x798>
   93acc:	3c050001 	lui	a1,0x1
			93acc: R_MIPS_HI16	.rodata
   93ad0:	3c040000 	lui	a0,0x0
			93ad0: R_MIPS_HI16	$LC15
   93ad4:	3c030000 	lui	v1,0x0
			93ad4: R_MIPS_HI16	printk
   93ad8:	24840000 	addiu	a0,a0,0
			93ad8: R_MIPS_LO16	$LC15
   93adc:	24630000 	addiu	v1,v1,0
			93adc: R_MIPS_LO16	printk
   93ae0:	0060f809 	jalr	v1
   93ae4:	24a5a8a0 	addiu	a1,a1,-22368
			93ae4: R_MIPS_LO16	.rodata
   93ae8:	08024e94 	j	93a50 <ol_transfer_bin_file+0x284>
			93ae8: R_MIPS_26	.text
   93aec:	24020003 	li	v0,3
   93af0:	3c024000 	lui	v0,0x4000
   93af4:	8c833610 	lw	v1,13840(a0)
   93af8:	3442002c 	ori	v0,v0,0x2c
   93afc:	1062ffd4 	beq	v1,v0,93a50 <ol_transfer_bin_file+0x284>
   93b00:	24020003 	li	v0,3
   93b04:	3c040000 	lui	a0,0x0
			93b04: R_MIPS_HI16	$LC17
   93b08:	08024ec6 	j	93b18 <ol_transfer_bin_file+0x34c>
			93b08: R_MIPS_26	.text
   93b0c:	24840000 	addiu	a0,a0,0
			93b0c: R_MIPS_LO16	$LC17
   93b10:	3c040000 	lui	a0,0x0
			93b10: R_MIPS_HI16	$LC11
   93b14:	24840000 	addiu	a0,a0,0
			93b14: R_MIPS_LO16	$LC11
   93b18:	3c050001 	lui	a1,0x1
			93b18: R_MIPS_HI16	.rodata
   93b1c:	3c030000 	lui	v1,0x0
			93b1c: R_MIPS_HI16	printk
   93b20:	24a5a8a0 	addiu	a1,a1,-22368
			93b20: R_MIPS_LO16	.rodata
   93b24:	24630000 	addiu	v1,v1,0
			93b24: R_MIPS_LO16	printk
   93b28:	0060f809 	jalr	v1
   93b2c:	00008021 	move	s0,zero
   93b30:	8fbf0044 	lw	ra,68(sp)
   93b34:	02001021 	move	v0,s0
   93b38:	8fbe0040 	lw	s8,64(sp)
   93b3c:	8fb7003c 	lw	s7,60(sp)
   93b40:	8fb60038 	lw	s6,56(sp)
   93b44:	8fb50034 	lw	s5,52(sp)
   93b48:	8fb40030 	lw	s4,48(sp)
   93b4c:	8fb3002c 	lw	s3,44(sp)
   93b50:	8fb20028 	lw	s2,40(sp)
   93b54:	8fb10024 	lw	s1,36(sp)
   93b58:	8fb00020 	lw	s0,32(sp)
   93b5c:	03e00008 	jr	ra
   93b60:	27bd0048 	addiu	sp,sp,72
   93b64:	1220ff8c 	beqz	s1,93998 <ol_transfer_bin_file+0x1cc>
   93b68:	00003021 	move	a2,zero
   93b6c:	00002021 	move	a0,zero
   93b70:	0280f809 	jalr	s4
   93b74:	02402821 	move	a1,s2
   93b78:	10400110 	beqz	v0,93fbc <ol_transfer_bin_file+0x7f0>
   93b7c:	00409821 	move	s3,v0
   93b80:	3c030000 	lui	v1,0x0
			93b80: R_MIPS_HI16	memcpy
   93b84:	00402021 	move	a0,v0
   93b88:	24630000 	addiu	v1,v1,0
			93b88: R_MIPS_LO16	memcpy
   93b8c:	02202821 	move	a1,s1
   93b90:	0060f809 	jalr	v1
   93b94:	02403021 	move	a2,s2
   93b98:	24020002 	li	v0,2
   93b9c:	8ec3360c 	lw	v1,13836(s6)
   93ba0:	106200bc 	beq	v1,v0,93e94 <ol_transfer_bin_file+0x6c8>
   93ba4:	8ec43654 	lw	a0,13908(s6)
   93ba8:	24020003 	li	v0,3
   93bac:	106200cb 	beq	v1,v0,93edc <ol_transfer_bin_file+0x710>
   93bb0:	24020005 	li	v0,5
   93bb4:	10620089 	beq	v1,v0,93ddc <ol_transfer_bin_file+0x610>
   93bb8:	24020006 	li	v0,6
   93bbc:	10620087 	beq	v1,v0,93ddc <ol_transfer_bin_file+0x610>
   93bc0:	24020007 	li	v0,7
   93bc4:	10620085 	beq	v1,v0,93ddc <ol_transfer_bin_file+0x610>
   93bc8:	24020008 	li	v0,8
   93bcc:	10620083 	beq	v1,v0,93ddc <ol_transfer_bin_file+0x610>
   93bd0:	24020009 	li	v0,9
   93bd4:	10620082 	beq	v1,v0,93de0 <ol_transfer_bin_file+0x614>
   93bd8:	3c020040 	lui	v0,0x40
   93bdc:	00002821 	move	a1,zero
   93be0:	3c030000 	lui	v1,0x0
			93be0: R_MIPS_HI16	BMIReadMemory
   93be4:	afb60010 	sw	s6,16(sp)
   93be8:	27a60018 	addiu	a2,sp,24
   93bec:	24630000 	addiu	v1,v1,0
			93bec: R_MIPS_LO16	BMIReadMemory
   93bf0:	0060f809 	jalr	v1
   93bf4:	24070004 	li	a3,4
   93bf8:	8fa50018 	lw	a1,24(sp)
   93bfc:	10a00003 	beqz	a1,93c0c <ol_transfer_bin_file+0x440>
