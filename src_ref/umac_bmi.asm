
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

000986e0 <BMILZData>:
   986e0:	27bdffb8 	addiu	sp,sp,-72
   986e4:	3c030000 	lui	v1,0x0
			986e4: R_MIPS_HI16	memset
   986e8:	afb50034 	sw	s5,52(sp)
   986ec:	24630000 	addiu	v1,v1,0
			986ec: R_MIPS_LO16	memset
   986f0:	afb00020 	sw	s0,32(sp)
   986f4:	00c0a821 	move	s5,a2
   986f8:	afbf0044 	sw	ra,68(sp)
   986fc:	00e08021 	move	s0,a3
   98700:	afbe0040 	sw	s8,64(sp)
   98704:	24060108 	li	a2,264
   98708:	afb7003c 	sw	s7,60(sp)
   9870c:	afb60038 	sw	s6,56(sp)
   98710:	afb40030 	sw	s4,48(sp)
   98714:	afb3002c 	sw	s3,44(sp)
   98718:	afb20028 	sw	s2,40(sp)
   9871c:	afb10024 	sw	s1,36(sp)
   98720:	8cf13634 	lw	s1,13876(a3)
   98724:	afa5004c 	sw	a1,76(sp)
   98728:	00002821 	move	a1,zero
   9872c:	afa40048 	sw	a0,72(sp)
   98730:	0060f809 	jalr	v1
   98734:	02202021 	move	a0,s1
   98738:	92043630 	lbu	a0,13872(s0)
   9873c:	1480004c 	bnez	a0,98870 <BMILZData+0x190>
   98740:	3c040000 	lui	a0,0x0
			98740: R_MIPS_HI16	$LC0
   98744:	12a0002b 	beqz	s5,987f4 <BMILZData+0x114>
   98748:	3c020000 	lui	v0,0x0
			98748: R_MIPS_HI16	memcpy
   9874c:	26340004 	addiu	s4,s1,4
   98750:	24520000 	addiu	s2,v0,0
			98750: R_MIPS_LO16	memcpy
   98754:	2402000e 	li	v0,14
   98758:	26330008 	addiu	s3,s1,8
   9875c:	27be0018 	addiu	s8,sp,24
   98760:	afa20018 	sw	v0,24(sp)
   98764:	27b7001c 	addiu	s7,sp,28
   98768:	241600f8 	li	s6,248
   9876c:	02a08021 	move	s0,s5
   98770:	2e0200f9 	sltiu	v0,s0,249
   98774:	02c01821 	move	v1,s6
   98778:	0202180b 	movn	v1,s0,v0
   9877c:	24060004 	li	a2,4
   98780:	02202021 	move	a0,s1
   98784:	03c02821 	move	a1,s8
   98788:	0240f809 	jalr	s2
   9878c:	afa3001c 	sw	v1,28(sp)
   98790:	24060004 	li	a2,4
   98794:	02802021 	move	a0,s4
   98798:	0240f809 	jalr	s2
   9879c:	02e02821 	move	a1,s7
   987a0:	02b02823 	subu	a1,s5,s0
   987a4:	8fa2004c 	lw	v0,76(sp)
   987a8:	02602021 	move	a0,s3
   987ac:	8fa6001c 	lw	a2,28(sp)
   987b0:	0240f809 	jalr	s2
   987b4:	00452821 	addu	a1,v0,a1
   987b8:	3c030000 	lui	v1,0x0
			987b8: R_MIPS_HI16	HIFExchangeBMIMsg
   987bc:	8fa6001c 	lw	a2,28(sp)
   987c0:	00003821 	move	a3,zero
   987c4:	8fa40048 	lw	a0,72(sp)
   987c8:	24630000 	addiu	v1,v1,0
			987c8: R_MIPS_LO16	HIFExchangeBMIMsg
   987cc:	02202821 	move	a1,s1
   987d0:	afa00010 	sw	zero,16(sp)
   987d4:	24c60008 	addiu	a2,a2,8
   987d8:	0060f809 	jalr	v1
   987dc:	afa00014 	sw	zero,20(sp)
   987e0:	14400011 	bnez	v0,98828 <BMILZData+0x148>
   987e4:	8fa2001c 	lw	v0,28(sp)
   987e8:	02028023 	subu	s0,s0,v0
   987ec:	1600ffe1 	bnez	s0,98774 <BMILZData+0x94>
   987f0:	2e0200f9 	sltiu	v0,s0,249
   987f4:	00001021 	move	v0,zero
   987f8:	8fbf0044 	lw	ra,68(sp)
   987fc:	8fbe0040 	lw	s8,64(sp)
   98800:	8fb7003c 	lw	s7,60(sp)
   98804:	8fb60038 	lw	s6,56(sp)
   98808:	8fb50034 	lw	s5,52(sp)
   9880c:	8fb40030 	lw	s4,48(sp)
   98810:	8fb3002c 	lw	s3,44(sp)
   98814:	8fb20028 	lw	s2,40(sp)
   98818:	8fb10024 	lw	s1,36(sp)
   9881c:	8fb00020 	lw	s0,32(sp)
   98820:	03e00008 	jr	ra
   98824:	27bd0048 	addiu	sp,sp,72
   98828:	3c040000 	lui	a0,0x0
			98828: R_MIPS_HI16	$LC5
   9882c:	3c030000 	lui	v1,0x0
			9882c: R_MIPS_HI16	printk
   98830:	24630000 	addiu	v1,v1,0
			98830: R_MIPS_LO16	printk
   98834:	0060f809 	jalr	v1
   98838:	24840000 	addiu	a0,a0,0
			98838: R_MIPS_LO16	$LC5
   9883c:	2402ffff 	li	v0,-1
   98840:	8fbf0044 	lw	ra,68(sp)
   98844:	8fbe0040 	lw	s8,64(sp)
   98848:	8fb7003c 	lw	s7,60(sp)
   9884c:	8fb60038 	lw	s6,56(sp)
   98850:	8fb50034 	lw	s5,52(sp)
   98854:	8fb40030 	lw	s4,48(sp)
   98858:	8fb3002c 	lw	s3,44(sp)
   9885c:	8fb20028 	lw	s2,40(sp)
   98860:	8fb10024 	lw	s1,36(sp)
   98864:	8fb00020 	lw	s0,32(sp)
   98868:	03e00008 	jr	ra
   9886c:	27bd0048 	addiu	sp,sp,72
   98870:	3c030000 	lui	v1,0x0
			98870: R_MIPS_HI16	printk
   98874:	24630000 	addiu	v1,v1,0
			98874: R_MIPS_LO16	printk
   98878:	0060f809 	jalr	v1
   9887c:	24840000 	addiu	a0,a0,0
			9887c: R_MIPS_LO16	$LC0
   98880:	080261fe 	j	987f8 <BMILZData+0x118>
			98880: R_MIPS_26	.text
   98884:	2402ffff 	li	v0,-1

00098888 <BMIFastDownload>:
   98888:	27bdffc8 	addiu	sp,sp,-56
   9888c:	3c020000 	lui	v0,0x0
			9888c: R_MIPS_HI16	BMILZStreamStart
   98890:	afb10020 	sw	s1,32(sp)
   98894:	afb30028 	sw	s3,40(sp)
   98898:	24530000 	addiu	s3,v0,0
			98898: R_MIPS_LO16	BMILZStreamStart
   9889c:	afb4002c 	sw	s4,44(sp)
   988a0:	00c0a021 	move	s4,a2
   988a4:	afb20024 	sw	s2,36(sp)
   988a8:	00809021 	move	s2,a0
   988ac:	afb0001c 	sw	s0,28(sp)
   988b0:	00e08021 	move	s0,a3
   988b4:	afbf0034 	sw	ra,52(sp)
   988b8:	afb50030 	sw	s5,48(sp)
   988bc:	afa00010 	sw	zero,16(sp)
   988c0:	8fb10048 	lw	s1,72(sp)
   988c4:	0260f809 	jalr	s3
   988c8:	02203021 	move	a2,s1
   988cc:	1040000b 	beqz	v0,988fc <BMIFastDownload+0x74>
   988d0:	2402fffc 	li	v0,-4
   988d4:	2402ffff 	li	v0,-1
   988d8:	8fbf0034 	lw	ra,52(sp)
   988dc:	8fb50030 	lw	s5,48(sp)
   988e0:	8fb4002c 	lw	s4,44(sp)
   988e4:	8fb30028 	lw	s3,40(sp)
   988e8:	8fb20024 	lw	s2,36(sp)
   988ec:	8fb10020 	lw	s1,32(sp)
   988f0:	8fb0001c 	lw	s0,28(sp)
   988f4:	03e00008 	jr	ra
   988f8:	27bd0038 	addiu	sp,sp,56
   988fc:	32150003 	andi	s5,s0,0x3
   98900:	16a00013 	bnez	s5,98950 <BMIFastDownload+0xc8>
   98904:	02028024 	and	s0,s0,v0
   98908:	3c020000 	lui	v0,0x0
			98908: R_MIPS_HI16	BMILZData
   9890c:	02802821 	move	a1,s4
   98910:	24540000 	addiu	s4,v0,0
			98910: R_MIPS_LO16	BMILZData
   98914:	02003021 	move	a2,s0
   98918:	02402021 	move	a0,s2
   9891c:	0280f809 	jalr	s4
   98920:	02203821 	move	a3,s1
   98924:	1440ffec 	bnez	v0,988d8 <BMIFastDownload+0x50>
   98928:	2402ffff 	li	v0,-1
   9892c:	16a00010 	bnez	s5,98970 <BMIFastDownload+0xe8>
   98930:	00002821 	move	a1,zero
   98934:	02402021 	move	a0,s2
   98938:	0260f809 	jalr	s3
   9893c:	02203021 	move	a2,s1
   98940:	1040ffe6 	beqz	v0,988dc <BMIFastDownload+0x54>
   98944:	8fbf0034 	lw	ra,52(sp)
   98948:	08026237 	j	988dc <BMIFastDownload+0x54>
			98948: R_MIPS_26	.text
   9894c:	2402ffff 	li	v0,-1
   98950:	3c030000 	lui	v1,0x0
			98950: R_MIPS_HI16	memcpy
   98954:	27a40010 	addiu	a0,sp,16
   98958:	02902821 	addu	a1,s4,s0
   9895c:	24630000 	addiu	v1,v1,0
			9895c: R_MIPS_LO16	memcpy
   98960:	0060f809 	jalr	v1
   98964:	02a03021 	move	a2,s5
   98968:	08026243 	j	9890c <BMIFastDownload+0x84>
			98968: R_MIPS_26	.text
   9896c:	3c020000 	lui	v0,0x0
			9896c: R_MIPS_HI16	BMILZData
   98970:	27a50010 	addiu	a1,sp,16
   98974:	24060004 	li	a2,4
   98978:	02402021 	move	a0,s2
   9897c:	0280f809 	jalr	s4
   98980:	02203821 	move	a3,s1
   98984:	1440ffd5 	bnez	v0,988dc <BMIFastDownload+0x54>
   98988:	8fbf0034 	lw	ra,52(sp)
   9898c:	0802624d 	j	98934 <BMIFastDownload+0xac>
			9898c: R_MIPS_26	.text
   98990:	00002821 	move	a1,zero

00098994 <BMIWriteSOCRegister>:
   98994:	27bdffd0 	addiu	sp,sp,-48
   98998:	3c030000 	lui	v1,0x0
			98998: R_MIPS_HI16	memset
   9899c:	afb20028 	sw	s2,40(sp)
   989a0:	24630000 	addiu	v1,v1,0
			989a0: R_MIPS_LO16	memset
   989a4:	afb00020 	sw	s0,32(sp)
   989a8:	00e08021 	move	s0,a3
   989ac:	afa50034 	sw	a1,52(sp)
   989b0:	00002821 	move	a1,zero
   989b4:	afa60038 	sw	a2,56(sp)
   989b8:	2406000c 	li	a2,12
   989bc:	afbf002c 	sw	ra,44(sp)
   989c0:	00809021 	move	s2,a0
   989c4:	afb10024 	sw	s1,36(sp)
   989c8:	8cf13634 	lw	s1,13876(a3)
   989cc:	0060f809 	jalr	v1
   989d0:	02202021 	move	a0,s1
   989d4:	92043630 	lbu	a0,13872(s0)
   989d8:	14800021 	bnez	a0,98a60 <BMIWriteSOCRegister+0xcc>
   989dc:	3c100000 	lui	s0,0x0
			989dc: R_MIPS_HI16	memcpy
   989e0:	24020007 	li	v0,7
   989e4:	26100000 	addiu	s0,s0,0
			989e4: R_MIPS_LO16	memcpy
   989e8:	27a50018 	addiu	a1,sp,24
   989ec:	afa20018 	sw	v0,24(sp)
   989f0:	24060004 	li	a2,4
   989f4:	0200f809 	jalr	s0
   989f8:	02202021 	move	a0,s1
   989fc:	26240004 	addiu	a0,s1,4
   98a00:	27a50034 	addiu	a1,sp,52
   98a04:	0200f809 	jalr	s0
   98a08:	24060004 	li	a2,4
   98a0c:	26240008 	addiu	a0,s1,8
   98a10:	27a50038 	addiu	a1,sp,56
   98a14:	0200f809 	jalr	s0
   98a18:	24060004 	li	a2,4
   98a1c:	3c030000 	lui	v1,0x0
			98a1c: R_MIPS_HI16	HIFExchangeBMIMsg
   98a20:	2406000c 	li	a2,12
   98a24:	afa00010 	sw	zero,16(sp)
   98a28:	00003821 	move	a3,zero
   98a2c:	afa00014 	sw	zero,20(sp)
   98a30:	24630000 	addiu	v1,v1,0
			98a30: R_MIPS_LO16	HIFExchangeBMIMsg
   98a34:	02402021 	move	a0,s2
   98a38:	0060f809 	jalr	v1
   98a3c:	02202821 	move	a1,s1
   98a40:	1440000e 	bnez	v0,98a7c <BMIWriteSOCRegister+0xe8>
   98a44:	3c040000 	lui	a0,0x0
			98a44: R_MIPS_HI16	$LC5
   98a48:	8fbf002c 	lw	ra,44(sp)
   98a4c:	8fb20028 	lw	s2,40(sp)
   98a50:	8fb10024 	lw	s1,36(sp)
   98a54:	8fb00020 	lw	s0,32(sp)
   98a58:	03e00008 	jr	ra
   98a5c:	27bd0030 	addiu	sp,sp,48
   98a60:	3c040000 	lui	a0,0x0
			98a60: R_MIPS_HI16	$LC0
   98a64:	3c030000 	lui	v1,0x0
			98a64: R_MIPS_HI16	printk
   98a68:	24630000 	addiu	v1,v1,0
			98a68: R_MIPS_LO16	printk
   98a6c:	0060f809 	jalr	v1
   98a70:	24840000 	addiu	a0,a0,0
			98a70: R_MIPS_LO16	$LC0
   98a74:	08026292 	j	98a48 <BMIWriteSOCRegister+0xb4>
			98a74: R_MIPS_26	.text
   98a78:	2402ffff 	li	v0,-1
   98a7c:	3c030000 	lui	v1,0x0
			98a7c: R_MIPS_HI16	printk
   98a80:	24630000 	addiu	v1,v1,0
			98a80: R_MIPS_LO16	printk
   98a84:	0060f809 	jalr	v1
   98a88:	24840000 	addiu	a0,a0,0
			98a88: R_MIPS_LO16	$LC5
   98a8c:	08026292 	j	98a48 <BMIWriteSOCRegister+0xb4>
			98a8c: R_MIPS_26	.text
   98a90:	2402ffff 	li	v0,-1

00098a94 <BMIReadSOCRegister>:
   98a94:	27bdffc0 	addiu	sp,sp,-64
   98a98:	afbf003c 	sw	ra,60(sp)
   98a9c:	afb50038 	sw	s5,56(sp)
   98aa0:	00c0a821 	move	s5,a2
   98aa4:	afb40034 	sw	s4,52(sp)
   98aa8:	24060008 	li	a2,8
   98aac:	afb10028 	sw	s1,40(sp)
   98ab0:	0080a021 	move	s4,a0
   98ab4:	afb00024 	sw	s0,36(sp)
   98ab8:	3c100000 	lui	s0,0x0
			98ab8: R_MIPS_HI16	memset
   98abc:	afa50044 	sw	a1,68(sp)
   98ac0:	00002821 	move	a1,zero
   98ac4:	afb30030 	sw	s3,48(sp)
   98ac8:	26100000 	addiu	s0,s0,0
			98ac8: R_MIPS_LO16	memset
   98acc:	afb2002c 	sw	s2,44(sp)
   98ad0:	00e08821 	move	s1,a3
   98ad4:	8cf23634 	lw	s2,13876(a3)
   98ad8:	8cf33640 	lw	s3,13888(a3)
   98adc:	0200f809 	jalr	s0
   98ae0:	02402021 	move	a0,s2
   98ae4:	00002821 	move	a1,zero
   98ae8:	24060008 	li	a2,8
   98aec:	0200f809 	jalr	s0
   98af0:	02602021 	move	a0,s3
   98af4:	92233630 	lbu	v1,13872(s1)
   98af8:	14600028 	bnez	v1,98b9c <BMIReadSOCRegister+0x108>
   98afc:	24060004 	li	a2,4
   98b00:	3c020000 	lui	v0,0x0
			98b00: R_MIPS_HI16	memcpy
   98b04:	27a50018 	addiu	a1,sp,24
   98b08:	24500000 	addiu	s0,v0,0
			98b08: R_MIPS_LO16	memcpy
   98b0c:	24020006 	li	v0,6
   98b10:	02402021 	move	a0,s2
   98b14:	0200f809 	jalr	s0
   98b18:	afa20018 	sw	v0,24(sp)
   98b1c:	26440004 	addiu	a0,s2,4
   98b20:	27a50044 	addiu	a1,sp,68
   98b24:	0200f809 	jalr	s0
   98b28:	24060004 	li	a2,4
   98b2c:	24030004 	li	v1,4
   98b30:	27a2001c 	addiu	v0,sp,28
   98b34:	afa3001c 	sw	v1,28(sp)
   98b38:	3c030000 	lui	v1,0x0
			98b38: R_MIPS_HI16	HIFExchangeBMIMsg
   98b3c:	afa20010 	sw	v0,16(sp)
   98b40:	240203e8 	li	v0,1000
   98b44:	24060008 	li	a2,8
   98b48:	24630000 	addiu	v1,v1,0
			98b48: R_MIPS_LO16	HIFExchangeBMIMsg
   98b4c:	afa20014 	sw	v0,20(sp)
   98b50:	02802021 	move	a0,s4
   98b54:	02402821 	move	a1,s2
   98b58:	0060f809 	jalr	v1
   98b5c:	02603821 	move	a3,s3
   98b60:	14400015 	bnez	v0,98bb8 <BMIReadSOCRegister+0x124>
   98b64:	24060004 	li	a2,4
   98b68:	02a02021 	move	a0,s5
   98b6c:	0200f809 	jalr	s0
   98b70:	02602821 	move	a1,s3
   98b74:	00001021 	move	v0,zero
   98b78:	8fbf003c 	lw	ra,60(sp)
   98b7c:	8fb50038 	lw	s5,56(sp)
   98b80:	8fb40034 	lw	s4,52(sp)
   98b84:	8fb30030 	lw	s3,48(sp)
   98b88:	8fb2002c 	lw	s2,44(sp)
   98b8c:	8fb10028 	lw	s1,40(sp)
   98b90:	8fb00024 	lw	s0,36(sp)
   98b94:	03e00008 	jr	ra
   98b98:	27bd0040 	addiu	sp,sp,64
   98b9c:	3c040000 	lui	a0,0x0
			98b9c: R_MIPS_HI16	$LC0
   98ba0:	3c030000 	lui	v1,0x0
			98ba0: R_MIPS_HI16	printk
   98ba4:	24630000 	addiu	v1,v1,0
			98ba4: R_MIPS_LO16	printk
   98ba8:	0060f809 	jalr	v1
   98bac:	24840000 	addiu	a0,a0,0
			98bac: R_MIPS_LO16	$LC0
   98bb0:	080262de 	j	98b78 <BMIReadSOCRegister+0xe4>
			98bb0: R_MIPS_26	.text
   98bb4:	2402ffff 	li	v0,-1
   98bb8:	3c040000 	lui	a0,0x0
			98bb8: R_MIPS_HI16	$LC6
   98bbc:	3c030000 	lui	v1,0x0
			98bbc: R_MIPS_HI16	printk
   98bc0:	24630000 	addiu	v1,v1,0
			98bc0: R_MIPS_LO16	printk
   98bc4:	0060f809 	jalr	v1
   98bc8:	24840000 	addiu	a0,a0,0
			98bc8: R_MIPS_LO16	$LC6
   98bcc:	080262de 	j	98b78 <BMIReadSOCRegister+0xe4>
			98bcc: R_MIPS_26	.text
   98bd0:	2402ffff 	li	v0,-1

00098bd4 <BMISetAppStart>:
   98bd4:	27bdffd0 	addiu	sp,sp,-48
   98bd8:	3c030000 	lui	v1,0x0
			98bd8: R_MIPS_HI16	memset
   98bdc:	afb20028 	sw	s2,40(sp)
   98be0:	24630000 	addiu	v1,v1,0
			98be0: R_MIPS_LO16	memset
   98be4:	afb00020 	sw	s0,32(sp)
   98be8:	00c08021 	move	s0,a2
   98bec:	afa50034 	sw	a1,52(sp)
   98bf0:	00002821 	move	a1,zero
   98bf4:	afbf002c 	sw	ra,44(sp)
   98bf8:	00809021 	move	s2,a0
   98bfc:	afb10024 	sw	s1,36(sp)
   98c00:	8cd13634 	lw	s1,13876(a2)
   98c04:	24060008 	li	a2,8
   98c08:	0060f809 	jalr	v1
   98c0c:	02202021 	move	a0,s1
   98c10:	92043630 	lbu	a0,13872(s0)
   98c14:	1480001d 	bnez	a0,98c8c <BMISetAppStart+0xb8>
   98c18:	3c100000 	lui	s0,0x0
			98c18: R_MIPS_HI16	memcpy
   98c1c:	24020005 	li	v0,5
   98c20:	27a50018 	addiu	a1,sp,24
   98c24:	26100000 	addiu	s0,s0,0
			98c24: R_MIPS_LO16	memcpy
   98c28:	afa20018 	sw	v0,24(sp)
   98c2c:	24060004 	li	a2,4
   98c30:	0200f809 	jalr	s0
   98c34:	02202021 	move	a0,s1
   98c38:	26240004 	addiu	a0,s1,4
   98c3c:	27a50034 	addiu	a1,sp,52
   98c40:	0200f809 	jalr	s0
   98c44:	24060004 	li	a2,4
   98c48:	3c030000 	lui	v1,0x0
			98c48: R_MIPS_HI16	HIFExchangeBMIMsg
   98c4c:	24060008 	li	a2,8
   98c50:	afa00010 	sw	zero,16(sp)
   98c54:	00003821 	move	a3,zero
   98c58:	afa00014 	sw	zero,20(sp)
   98c5c:	24630000 	addiu	v1,v1,0
			98c5c: R_MIPS_LO16	HIFExchangeBMIMsg
   98c60:	02402021 	move	a0,s2
   98c64:	0060f809 	jalr	v1
   98c68:	02202821 	move	a1,s1
   98c6c:	1440000e 	bnez	v0,98ca8 <BMISetAppStart+0xd4>
   98c70:	3c040000 	lui	a0,0x0
			98c70: R_MIPS_HI16	$LC5
   98c74:	8fbf002c 	lw	ra,44(sp)
   98c78:	8fb20028 	lw	s2,40(sp)
   98c7c:	8fb10024 	lw	s1,36(sp)
   98c80:	8fb00020 	lw	s0,32(sp)
   98c84:	03e00008 	jr	ra
   98c88:	27bd0030 	addiu	sp,sp,48
   98c8c:	3c040000 	lui	a0,0x0
			98c8c: R_MIPS_HI16	$LC0
   98c90:	3c030000 	lui	v1,0x0
			98c90: R_MIPS_HI16	printk
   98c94:	24630000 	addiu	v1,v1,0
			98c94: R_MIPS_LO16	printk
   98c98:	0060f809 	jalr	v1
   98c9c:	24840000 	addiu	a0,a0,0
			98c9c: R_MIPS_LO16	$LC0
   98ca0:	0802631d 	j	98c74 <BMISetAppStart+0xa0>
			98ca0: R_MIPS_26	.text
   98ca4:	2402ffff 	li	v0,-1
   98ca8:	3c030000 	lui	v1,0x0
			98ca8: R_MIPS_HI16	printk
   98cac:	24630000 	addiu	v1,v1,0
			98cac: R_MIPS_LO16	printk
   98cb0:	0060f809 	jalr	v1
   98cb4:	24840000 	addiu	a0,a0,0
			98cb4: R_MIPS_LO16	$LC5
   98cb8:	0802631d 	j	98c74 <BMISetAppStart+0xa0>
			98cb8: R_MIPS_26	.text
   98cbc:	2402ffff 	li	v0,-1

00098cc0 <BMIExecute>:
   98cc0:	27bdffc0 	addiu	sp,sp,-64
   98cc4:	afbf003c 	sw	ra,60(sp)
   98cc8:	afb50038 	sw	s5,56(sp)
   98ccc:	0080a821 	move	s5,a0
   98cd0:	afb40034 	sw	s4,52(sp)
   98cd4:	00c0a021 	move	s4,a2
   98cd8:	afb10028 	sw	s1,40(sp)
   98cdc:	2406000c 	li	a2,12
   98ce0:	afb00024 	sw	s0,36(sp)
   98ce4:	3c100000 	lui	s0,0x0
			98ce4: R_MIPS_HI16	memset
   98ce8:	afa50044 	sw	a1,68(sp)
   98cec:	00002821 	move	a1,zero
   98cf0:	afb30030 	sw	s3,48(sp)
   98cf4:	26100000 	addiu	s0,s0,0
			98cf4: R_MIPS_LO16	memset
   98cf8:	afb2002c 	sw	s2,44(sp)
   98cfc:	00e08821 	move	s1,a3
   98d00:	8cf23634 	lw	s2,13876(a3)
   98d04:	8cf33640 	lw	s3,13888(a3)
   98d08:	0200f809 	jalr	s0
   98d0c:	02402021 	move	a0,s2
   98d10:	00002821 	move	a1,zero
   98d14:	2406000c 	li	a2,12
   98d18:	0200f809 	jalr	s0
   98d1c:	02602021 	move	a0,s3
   98d20:	92233630 	lbu	v1,13872(s1)
   98d24:	1460002a 	bnez	v1,98dd0 <BMIExecute+0x110>
   98d28:	24100004 	li	s0,4
   98d2c:	3c020000 	lui	v0,0x0
			98d2c: R_MIPS_HI16	memcpy
   98d30:	24510000 	addiu	s1,v0,0
			98d30: R_MIPS_LO16	memcpy
   98d34:	27a50018 	addiu	a1,sp,24
   98d38:	afb00018 	sw	s0,24(sp)
   98d3c:	24060004 	li	a2,4
   98d40:	0220f809 	jalr	s1
   98d44:	02402021 	move	a0,s2
   98d48:	26440004 	addiu	a0,s2,4
   98d4c:	27a50044 	addiu	a1,sp,68
   98d50:	0220f809 	jalr	s1
   98d54:	24060004 	li	a2,4
   98d58:	26440008 	addiu	a0,s2,8
   98d5c:	24060004 	li	a2,4
   98d60:	0220f809 	jalr	s1
   98d64:	02802821 	move	a1,s4
   98d68:	3c030000 	lui	v1,0x0
			98d68: R_MIPS_HI16	HIFExchangeBMIMsg
   98d6c:	27a2001c 	addiu	v0,sp,28
   98d70:	afb0001c 	sw	s0,28(sp)
   98d74:	2406000c 	li	a2,12
   98d78:	afa00014 	sw	zero,20(sp)
   98d7c:	24630000 	addiu	v1,v1,0
			98d7c: R_MIPS_LO16	HIFExchangeBMIMsg
   98d80:	afa20010 	sw	v0,16(sp)
   98d84:	02a02021 	move	a0,s5
   98d88:	02402821 	move	a1,s2
   98d8c:	0060f809 	jalr	v1
   98d90:	02603821 	move	a3,s3
   98d94:	14400015 	bnez	v0,98dec <BMIExecute+0x12c>
   98d98:	24060004 	li	a2,4
   98d9c:	02802021 	move	a0,s4
   98da0:	0220f809 	jalr	s1
   98da4:	02602821 	move	a1,s3
   98da8:	00001021 	move	v0,zero
   98dac:	8fbf003c 	lw	ra,60(sp)
   98db0:	8fb50038 	lw	s5,56(sp)
   98db4:	8fb40034 	lw	s4,52(sp)
   98db8:	8fb30030 	lw	s3,48(sp)
   98dbc:	8fb2002c 	lw	s2,44(sp)
   98dc0:	8fb10028 	lw	s1,40(sp)
   98dc4:	8fb00024 	lw	s0,36(sp)
   98dc8:	03e00008 	jr	ra
   98dcc:	27bd0040 	addiu	sp,sp,64
   98dd0:	3c040000 	lui	a0,0x0
			98dd0: R_MIPS_HI16	$LC0
   98dd4:	3c030000 	lui	v1,0x0
			98dd4: R_MIPS_HI16	printk
   98dd8:	24630000 	addiu	v1,v1,0
			98dd8: R_MIPS_LO16	printk
   98ddc:	0060f809 	jalr	v1
   98de0:	24840000 	addiu	a0,a0,0
			98de0: R_MIPS_LO16	$LC0
   98de4:	0802636b 	j	98dac <BMIExecute+0xec>
			98de4: R_MIPS_26	.text
   98de8:	2402ffff 	li	v0,-1
   98dec:	3c040000 	lui	a0,0x0
			98dec: R_MIPS_HI16	$LC6
   98df0:	3c030000 	lui	v1,0x0
			98df0: R_MIPS_HI16	printk
   98df4:	24630000 	addiu	v1,v1,0
			98df4: R_MIPS_LO16	printk
   98df8:	0060f809 	jalr	v1
   98dfc:	24840000 	addiu	a0,a0,0
			98dfc: R_MIPS_LO16	$LC6
   98e00:	0802636b 	j	98dac <BMIExecute+0xec>
			98e00: R_MIPS_26	.text
   98e04:	2402ffff 	li	v0,-1

00098e08 <BMIWriteMemory>:
   98e08:	27bdfeb8 	addiu	sp,sp,-328
   98e0c:	3c030000 	lui	v1,0x0
			98e0c: R_MIPS_HI16	memset
   98e10:	afb00120 	sw	s0,288(sp)
   98e14:	24630000 	addiu	v1,v1,0
			98e14: R_MIPS_LO16	memset
   98e18:	afb7013c 	sw	s7,316(sp)
   98e1c:	00e0b821 	move	s7,a3
   98e20:	afa5014c 	sw	a1,332(sp)
   98e24:	00002821 	move	a1,zero
   98e28:	afa60150 	sw	a2,336(sp)
   98e2c:	2406010c 	li	a2,268
   98e30:	afbf0144 	sw	ra,324(sp)
   98e34:	afbe0140 	sw	s8,320(sp)
   98e38:	afb60138 	sw	s6,312(sp)
   98e3c:	afb50134 	sw	s5,308(sp)
   98e40:	afb40130 	sw	s4,304(sp)
   98e44:	afb3012c 	sw	s3,300(sp)
   98e48:	afb20128 	sw	s2,296(sp)
   98e4c:	afb10124 	sw	s1,292(sp)
   98e50:	8fb00158 	lw	s0,344(sp)
   98e54:	8e133634 	lw	s3,13876(s0)
   98e58:	afa40148 	sw	a0,328(sp)
   98e5c:	0060f809 	jalr	v1
   98e60:	02602021 	move	a0,s3
   98e64:	92043630 	lbu	a0,13872(s0)
   98e68:	14800065 	bnez	a0,99000 <BMIWriteMemory+0x1f8>
   98e6c:	3c040000 	lui	a0,0x0
			98e6c: R_MIPS_HI16	$LC0
   98e70:	12e00044 	beqz	s7,98f84 <BMIWriteMemory+0x17c>
   98e74:	3c020000 	lui	v0,0x0
			98e74: R_MIPS_HI16	memcpy
   98e78:	8fa50150 	lw	a1,336(sp)
   98e7c:	02e08021 	move	s0,s7
   98e80:	24520000 	addiu	s2,v0,0
			98e80: R_MIPS_LO16	memcpy
   98e84:	24020003 	li	v0,3
   98e88:	2e0300f4 	sltiu	v1,s0,244
   98e8c:	afa20018 	sw	v0,24(sp)
   98e90:	02f01023 	subu	v0,s7,s0
   98e94:	26760004 	addiu	s6,s3,4
   98e98:	26750008 	addiu	s5,s3,8
   98e9c:	2674000c 	addiu	s4,s3,12
   98ea0:	241e03e8 	li	s8,1000
   98ea4:	32040003 	andi	a0,s0,0x3
   98ea8:	1060002b 	beqz	v1,98f58 <BMIWriteMemory+0x150>
   98eac:	00a28821 	addu	s1,a1,v0
   98eb0:	1480002c 	bnez	a0,98f64 <BMIWriteMemory+0x15c>
   98eb4:	2403fffc 	li	v1,-4
   98eb8:	afb0001c 	sw	s0,28(sp)
   98ebc:	24060004 	li	a2,4
   98ec0:	27a50018 	addiu	a1,sp,24
   98ec4:	0240f809 	jalr	s2
   98ec8:	02602021 	move	a0,s3
   98ecc:	27a5014c 	addiu	a1,sp,332
   98ed0:	24060004 	li	a2,4
   98ed4:	0240f809 	jalr	s2
   98ed8:	02c02021 	move	a0,s6
   98edc:	27a5001c 	addiu	a1,sp,28
   98ee0:	24060004 	li	a2,4
   98ee4:	0240f809 	jalr	s2
   98ee8:	02a02021 	move	a0,s5
   98eec:	02802021 	move	a0,s4
   98ef0:	8fa6001c 	lw	a2,28(sp)
   98ef4:	0240f809 	jalr	s2
   98ef8:	02202821 	move	a1,s1
   98efc:	3c030000 	lui	v1,0x0
			98efc: R_MIPS_HI16	HIFExchangeBMIMsg
   98f00:	8fa6001c 	lw	a2,28(sp)
   98f04:	00003821 	move	a3,zero
   98f08:	8fa40148 	lw	a0,328(sp)
   98f0c:	24630000 	addiu	v1,v1,0
			98f0c: R_MIPS_LO16	HIFExchangeBMIMsg
   98f10:	02602821 	move	a1,s3
   98f14:	afa00010 	sw	zero,16(sp)
   98f18:	24c6000c 	addiu	a2,a2,12
   98f1c:	0060f809 	jalr	v1
   98f20:	afbe0014 	sw	s8,20(sp)
   98f24:	14400024 	bnez	v0,98fb8 <BMIWriteMemory+0x1b0>
   98f28:	8fa3001c 	lw	v1,28(sp)
   98f2c:	8fa2014c 	lw	v0,332(sp)
   98f30:	02038023 	subu	s0,s0,v1
   98f34:	12000013 	beqz	s0,98f84 <BMIWriteMemory+0x17c>
   98f38:	00431021 	addu	v0,v0,v1
   98f3c:	8fa50150 	lw	a1,336(sp)
   98f40:	2e0300f4 	sltiu	v1,s0,244
   98f44:	afa2014c 	sw	v0,332(sp)
   98f48:	02f01023 	subu	v0,s7,s0
   98f4c:	32040003 	andi	a0,s0,0x3
   98f50:	1460ffd7 	bnez	v1,98eb0 <BMIWriteMemory+0xa8>
   98f54:	00a28821 	addu	s1,a1,v0
   98f58:	240500f4 	li	a1,244
   98f5c:	080263af 	j	98ebc <BMIWriteMemory+0xb4>
			98f5c: R_MIPS_26	.text
   98f60:	afa5001c 	sw	a1,28(sp)
   98f64:	27a40020 	addiu	a0,sp,32
   98f68:	02031024 	and	v0,s0,v1
   98f6c:	24500004 	addiu	s0,v0,4
   98f70:	02202821 	move	a1,s1
   98f74:	0240f809 	jalr	s2
   98f78:	02003021 	move	a2,s0
   98f7c:	080263ae 	j	98eb8 <BMIWriteMemory+0xb0>
			98f7c: R_MIPS_26	.text
   98f80:	27b10020 	addiu	s1,sp,32
   98f84:	00001021 	move	v0,zero
   98f88:	8fbf0144 	lw	ra,324(sp)
   98f8c:	8fbe0140 	lw	s8,320(sp)
   98f90:	8fb7013c 	lw	s7,316(sp)
   98f94:	8fb60138 	lw	s6,312(sp)
   98f98:	8fb50134 	lw	s5,308(sp)
   98f9c:	8fb40130 	lw	s4,304(sp)
   98fa0:	8fb3012c 	lw	s3,300(sp)
   98fa4:	8fb20128 	lw	s2,296(sp)
   98fa8:	8fb10124 	lw	s1,292(sp)
   98fac:	8fb00120 	lw	s0,288(sp)
   98fb0:	03e00008 	jr	ra
   98fb4:	27bd0148 	addiu	sp,sp,328
   98fb8:	3c040000 	lui	a0,0x0
			98fb8: R_MIPS_HI16	$LC5
   98fbc:	3c030000 	lui	v1,0x0
			98fbc: R_MIPS_HI16	printk
   98fc0:	24630000 	addiu	v1,v1,0
			98fc0: R_MIPS_LO16	printk
   98fc4:	0060f809 	jalr	v1
   98fc8:	24840000 	addiu	a0,a0,0
			98fc8: R_MIPS_LO16	$LC5
   98fcc:	2402ffff 	li	v0,-1
   98fd0:	8fbf0144 	lw	ra,324(sp)
   98fd4:	8fbe0140 	lw	s8,320(sp)
   98fd8:	8fb7013c 	lw	s7,316(sp)
   98fdc:	8fb60138 	lw	s6,312(sp)
   98fe0:	8fb50134 	lw	s5,308(sp)
   98fe4:	8fb40130 	lw	s4,304(sp)
   98fe8:	8fb3012c 	lw	s3,300(sp)
   98fec:	8fb20128 	lw	s2,296(sp)
   98ff0:	8fb10124 	lw	s1,292(sp)
   98ff4:	8fb00120 	lw	s0,288(sp)
   98ff8:	03e00008 	jr	ra
   98ffc:	27bd0148 	addiu	sp,sp,328
   99000:	3c030000 	lui	v1,0x0
			99000: R_MIPS_HI16	printk
   99004:	24630000 	addiu	v1,v1,0
			99004: R_MIPS_LO16	printk
   99008:	0060f809 	jalr	v1
   9900c:	24840000 	addiu	a0,a0,0
			9900c: R_MIPS_LO16	$LC0
   99010:	080263e2 	j	98f88 <BMIWriteMemory+0x180>
			99010: R_MIPS_26	.text
   99014:	2402ffff 	li	v0,-1
