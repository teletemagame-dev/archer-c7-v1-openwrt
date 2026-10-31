
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

00085b1c <ol_ath_download_firmware>:
   85b1c:	27bdffc8 	addiu	sp,sp,-56
   85b20:	24020003 	li	v0,3
   85b24:	afb00024 	sw	s0,36(sp)
   85b28:	00808021 	move	s0,a0
   85b2c:	afbf0034 	sw	ra,52(sp)
   85b30:	afb30030 	sw	s3,48(sp)
   85b34:	afb2002c 	sw	s2,44(sp)
   85b38:	afb10028 	sw	s1,40(sp)
   85b3c:	afa0001c 	sw	zero,28(sp)
   85b40:	8c83360c 	lw	v1,13836(a0)
   85b44:	10620090 	beq	v1,v0,85d88 <ol_ath_download_firmware+0x26c>
   85b48:	8c843654 	lw	a0,13908(a0)
   85b4c:	2c620003 	sltiu	v0,v1,3
   85b50:	10400004 	beqz	v0,85b64 <ol_ath_download_firmware+0x48>
   85b54:	2462fffb 	addiu	v0,v1,-5
   85b58:	3c020050 	lui	v0,0x50
   85b5c:	080216de 	j	85b78 <ol_ath_download_firmware+0x5c>
			85b5c: R_MIPS_26	.text
   85b60:	34450454 	ori	a1,v0,0x454
   85b64:	2c420004 	sltiu	v0,v0,4
   85b68:	1040fffc 	beqz	v0,85b5c <ol_ath_download_firmware+0x40>
   85b6c:	3c020050 	lui	v0,0x50
   85b70:	3c020040 	lui	v0,0x40
   85b74:	34450854 	ori	a1,v0,0x854
   85b78:	3c030000 	lui	v1,0x0
			85b78: R_MIPS_HI16	BMIReadMemory
   85b7c:	afb00010 	sw	s0,16(sp)
   85b80:	27a6001c 	addiu	a2,sp,28
   85b84:	24630000 	addiu	v1,v1,0
			85b84: R_MIPS_LO16	BMIReadMemory
   85b88:	0060f809 	jalr	v1
   85b8c:	24070004 	li	a3,4
   85b90:	8fa6001c 	lw	a2,28(sp)
   85b94:	50c000b8 	beqzl	a2,85e78 <ol_ath_download_firmware+0x35c>
   85b98:	3c060042 	lui	a2,0x42
   85b9c:	8e02361c 	lw	v0,13852(s0)
   85ba0:	10400046 	beqz	v0,85cbc <ol_ath_download_firmware+0x1a0>
   85ba4:	3c020000 	lui	v0,0x0
			85ba4: R_MIPS_HI16	ol_transfer_bin_file
   85ba8:	24050004 	li	a1,4
   85bac:	24510000 	addiu	s1,v0,0
			85bac: R_MIPS_LO16	ol_transfer_bin_file
   85bb0:	00003821 	move	a3,zero
   85bb4:	0220f809 	jalr	s1
   85bb8:	02002021 	move	a0,s0
   85bbc:	144000ac 	bnez	v0,85e70 <ol_ath_download_firmware+0x354>
   85bc0:	24020001 	li	v0,1
   85bc4:	8e05360c 	lw	a1,13836(s0)
   85bc8:	24030003 	li	v1,3
   85bcc:	8e043654 	lw	a0,13908(s0)
   85bd0:	10a30070 	beq	a1,v1,85d94 <ol_ath_download_firmware+0x278>
   85bd4:	afa20018 	sw	v0,24(sp)
   85bd8:	2ca20003 	sltiu	v0,a1,3
   85bdc:	10400004 	beqz	v0,85bf0 <ol_ath_download_firmware+0xd4>
   85be0:	24a2fffb 	addiu	v0,a1,-5
   85be4:	3c020050 	lui	v0,0x50
   85be8:	08021701 	j	85c04 <ol_ath_download_firmware+0xe8>
			85be8: R_MIPS_26	.text
   85bec:	34450458 	ori	a1,v0,0x458
   85bf0:	2c420004 	sltiu	v0,v0,4
   85bf4:	1040fffc 	beqz	v0,85be8 <ol_ath_download_firmware+0xcc>
   85bf8:	3c020050 	lui	v0,0x50
   85bfc:	3c020040 	lui	v0,0x40
   85c00:	34450858 	ori	a1,v0,0x858
   85c04:	3c030000 	lui	v1,0x0
			85c04: R_MIPS_HI16	BMIWriteMemory
   85c08:	afb00010 	sw	s0,16(sp)
   85c0c:	27b20018 	addiu	s2,sp,24
   85c10:	24730000 	addiu	s3,v1,0
			85c10: R_MIPS_LO16	BMIWriteMemory
   85c14:	24070004 	li	a3,4
   85c18:	0260f809 	jalr	s3
   85c1c:	02403021 	move	a2,s2
   85c20:	24021234 	li	v0,4660
   85c24:	24050001 	li	a1,1
   85c28:	24061234 	li	a2,4660
   85c2c:	afa2001c 	sw	v0,28(sp)
   85c30:	24070001 	li	a3,1
   85c34:	0220f809 	jalr	s1
   85c38:	02002021 	move	a0,s0
   85c3c:	14400026 	bnez	v0,85cd8 <ol_ath_download_firmware+0x1bc>
   85c40:	2403ffff 	li	v1,-1
   85c44:	92023728 	lbu	v0,14120(s0)
   85c48:	5440002b 	bnezl	v0,85cf8 <ol_ath_download_firmware+0x1dc>
   85c4c:	8e05360c 	lw	a1,13836(s0)
   85c50:	8e03360c 	lw	v1,13836(s0)
   85c54:	24020003 	li	v0,3
   85c58:	8e043654 	lw	a0,13908(s0)
   85c5c:	10620050 	beq	v1,v0,85da0 <ol_ath_download_firmware+0x284>
   85c60:	afa00018 	sw	zero,24(sp)
   85c64:	2c620003 	sltiu	v0,v1,3
   85c68:	14400045 	bnez	v0,85d80 <ol_ath_download_firmware+0x264>
   85c6c:	3c020050 	lui	v0,0x50
   85c70:	2462fffb 	addiu	v0,v1,-5
   85c74:	2c420004 	sltiu	v0,v0,4
   85c78:	10400041 	beqz	v0,85d80 <ol_ath_download_firmware+0x264>
   85c7c:	3c020050 	lui	v0,0x50
   85c80:	3c020040 	lui	v0,0x40
   85c84:	34450814 	ori	a1,v0,0x814
   85c88:	24070004 	li	a3,4
   85c8c:	afb00010 	sw	s0,16(sp)
   85c90:	0260f809 	jalr	s3
   85c94:	02403021 	move	a2,s2
   85c98:	00001821 	move	v1,zero
   85c9c:	8fbf0034 	lw	ra,52(sp)
   85ca0:	00601021 	move	v0,v1
   85ca4:	8fb30030 	lw	s3,48(sp)
   85ca8:	8fb2002c 	lw	s2,44(sp)
   85cac:	8fb10028 	lw	s1,40(sp)
   85cb0:	8fb00024 	lw	s0,36(sp)
   85cb4:	03e00008 	jr	ra
   85cb8:	27bd0038 	addiu	sp,sp,56
   85cbc:	24510000 	addiu	s1,v0,0
			85cbc: R_MIPS_LO16	ol_transfer_bin_file
   85cc0:	24050003 	li	a1,3
   85cc4:	00003821 	move	a3,zero
   85cc8:	0220f809 	jalr	s1
   85ccc:	02002021 	move	a0,s0
   85cd0:	10400036 	beqz	v0,85dac <ol_ath_download_firmware+0x290>
   85cd4:	2403ffff 	li	v1,-1
   85cd8:	8fbf0034 	lw	ra,52(sp)
   85cdc:	00601021 	move	v0,v1
   85ce0:	8fb30030 	lw	s3,48(sp)
   85ce4:	8fb2002c 	lw	s2,44(sp)
   85ce8:	8fb10028 	lw	s1,40(sp)
   85cec:	8fb00024 	lw	s0,36(sp)
   85cf0:	03e00008 	jr	ra
   85cf4:	27bd0038 	addiu	sp,sp,56
   85cf8:	24020007 	li	v0,7
   85cfc:	24030003 	li	v1,3
   85d00:	8e043654 	lw	a0,13908(s0)
   85d04:	10a30057 	beq	a1,v1,85e64 <ol_ath_download_firmware+0x348>
   85d08:	afa20018 	sw	v0,24(sp)
   85d0c:	2ca20003 	sltiu	v0,a1,3
   85d10:	10400004 	beqz	v0,85d24 <ol_ath_download_firmware+0x208>
   85d14:	24a2fffb 	addiu	v0,a1,-5
   85d18:	3c020050 	lui	v0,0x50
   85d1c:	0802174e 	j	85d38 <ol_ath_download_firmware+0x21c>
			85d1c: R_MIPS_26	.text
   85d20:	34450480 	ori	a1,v0,0x480
   85d24:	2c420004 	sltiu	v0,v0,4
   85d28:	1040fffc 	beqz	v0,85d1c <ol_ath_download_firmware+0x200>
   85d2c:	3c020050 	lui	v0,0x50
   85d30:	3c020040 	lui	v0,0x40
   85d34:	34450880 	ori	a1,v0,0x880
   85d38:	24070004 	li	a3,4
   85d3c:	afb00010 	sw	s0,16(sp)
   85d40:	0260f809 	jalr	s3
   85d44:	02403021 	move	a2,s2
   85d48:	24020001 	li	v0,1
   85d4c:	8e05360c 	lw	a1,13836(s0)
   85d50:	24030003 	li	v1,3
   85d54:	8e043654 	lw	a0,13908(s0)
   85d58:	10a30011 	beq	a1,v1,85da0 <ol_ath_download_firmware+0x284>
   85d5c:	afa20018 	sw	v0,24(sp)
   85d60:	2ca20003 	sltiu	v0,a1,3
   85d64:	14400006 	bnez	v0,85d80 <ol_ath_download_firmware+0x264>
   85d68:	3c020050 	lui	v0,0x50
   85d6c:	24a2fffb 	addiu	v0,a1,-5
   85d70:	2c420004 	sltiu	v0,v0,4
   85d74:	1440ffc3 	bnez	v0,85c84 <ol_ath_download_firmware+0x168>
   85d78:	3c020040 	lui	v0,0x40
   85d7c:	3c020050 	lui	v0,0x50
   85d80:	08021722 	j	85c88 <ol_ath_download_firmware+0x16c>
			85d80: R_MIPS_26	.text
   85d84:	34450414 	ori	a1,v0,0x414
   85d88:	3c020054 	lui	v0,0x54
   85d8c:	080216de 	j	85b78 <ol_ath_download_firmware+0x5c>
			85d8c: R_MIPS_26	.text
   85d90:	34450654 	ori	a1,v0,0x654
   85d94:	3c020054 	lui	v0,0x54
   85d98:	08021701 	j	85c04 <ol_ath_download_firmware+0xe8>
			85d98: R_MIPS_26	.text
   85d9c:	34450658 	ori	a1,v0,0x658
   85da0:	3c020054 	lui	v0,0x54
   85da4:	08021722 	j	85c88 <ol_ath_download_firmware+0x16c>
			85da4: R_MIPS_26	.text
   85da8:	34450614 	ori	a1,v0,0x614
   85dac:	8e05360c 	lw	a1,13836(s0)
   85db0:	24020001 	li	v0,1
   85db4:	24030003 	li	v1,3
   85db8:	8e043654 	lw	a0,13908(s0)
   85dbc:	10a30043 	beq	a1,v1,85ecc <ol_ath_download_firmware+0x3b0>
   85dc0:	afa20018 	sw	v0,24(sp)
   85dc4:	2ca20003 	sltiu	v0,a1,3
   85dc8:	10400020 	beqz	v0,85e4c <ol_ath_download_firmware+0x330>
   85dcc:	24a2fffb 	addiu	v0,a1,-5
   85dd0:	3c020050 	lui	v0,0x50
   85dd4:	34450458 	ori	a1,v0,0x458
   85dd8:	3c030000 	lui	v1,0x0
			85dd8: R_MIPS_HI16	BMIWriteMemory
   85ddc:	afb00010 	sw	s0,16(sp)
   85de0:	27b20018 	addiu	s2,sp,24
   85de4:	24070004 	li	a3,4
   85de8:	24730000 	addiu	s3,v1,0
			85de8: R_MIPS_LO16	BMIWriteMemory
   85dec:	0260f809 	jalr	s3
   85df0:	02403021 	move	a2,s2
   85df4:	3c050001 	lui	a1,0x1
			85df4: R_MIPS_HI16	.rodata
   85df8:	3c040000 	lui	a0,0x0
			85df8: R_MIPS_HI16	$LC39
   85dfc:	3c030000 	lui	v1,0x0
			85dfc: R_MIPS_HI16	printk
   85e00:	24021234 	li	v0,4660
   85e04:	24630000 	addiu	v1,v1,0
			85e04: R_MIPS_LO16	printk
   85e08:	24a59948 	addiu	a1,a1,-26296
			85e08: R_MIPS_LO16	.rodata
   85e0c:	afa2001c 	sw	v0,28(sp)
   85e10:	24840000 	addiu	a0,a0,0
			85e10: R_MIPS_LO16	$LC39
   85e14:	0060f809 	jalr	v1
   85e18:	24061234 	li	a2,4660
   85e1c:	00002821 	move	a1,zero
   85e20:	8fa6001c 	lw	a2,28(sp)
   85e24:	24070001 	li	a3,1
   85e28:	0220f809 	jalr	s1
   85e2c:	02002021 	move	a0,s0
   85e30:	1040001c 	beqz	v0,85ea4 <ol_ath_download_firmware+0x388>
   85e34:	00401821 	move	v1,v0
   85e38:	2402ffff 	li	v0,-1
   85e3c:	1462ff79 	bne	v1,v0,85c24 <ol_ath_download_firmware+0x108>
   85e40:	24021234 	li	v0,4660
   85e44:	08021737 	j	85cdc <ol_ath_download_firmware+0x1c0>
			85e44: R_MIPS_26	.text
   85e48:	8fbf0034 	lw	ra,52(sp)
   85e4c:	2c420004 	sltiu	v0,v0,4
   85e50:	1040ffe0 	beqz	v0,85dd4 <ol_ath_download_firmware+0x2b8>
   85e54:	3c020050 	lui	v0,0x50
   85e58:	3c020040 	lui	v0,0x40
   85e5c:	08021776 	j	85dd8 <ol_ath_download_firmware+0x2bc>
			85e5c: R_MIPS_26	.text
   85e60:	34450858 	ori	a1,v0,0x858
   85e64:	3c020054 	lui	v0,0x54
   85e68:	0802174e 	j	85d38 <ol_ath_download_firmware+0x21c>
			85e68: R_MIPS_26	.text
   85e6c:	34450680 	ori	a1,v0,0x680
   85e70:	08021730 	j	85cc0 <ol_ath_download_firmware+0x1a4>
			85e70: R_MIPS_26	.text
   85e74:	8fa6001c 	lw	a2,28(sp)
   85e78:	3c040000 	lui	a0,0x0
			85e78: R_MIPS_HI16	$LC38
   85e7c:	3c050001 	lui	a1,0x1
			85e7c: R_MIPS_HI16	.rodata
   85e80:	3c030000 	lui	v1,0x0
			85e80: R_MIPS_HI16	printk
   85e84:	34c63900 	ori	a2,a2,0x3900
   85e88:	24840000 	addiu	a0,a0,0
			85e88: R_MIPS_LO16	$LC38
   85e8c:	afa6001c 	sw	a2,28(sp)
   85e90:	24630000 	addiu	v1,v1,0
			85e90: R_MIPS_LO16	printk
   85e94:	0060f809 	jalr	v1
   85e98:	24a59948 	addiu	a1,a1,-26296
			85e98: R_MIPS_LO16	.rodata
   85e9c:	080216e7 	j	85b9c <ol_ath_download_firmware+0x80>
			85e9c: R_MIPS_26	.text
   85ea0:	8fa6001c 	lw	a2,28(sp)
   85ea4:	3c030000 	lui	v1,0x0
			85ea4: R_MIPS_HI16	BMIExecute
   85ea8:	8e043654 	lw	a0,13908(s0)
   85eac:	8fa5001c 	lw	a1,28(sp)
   85eb0:	02403021 	move	a2,s2
   85eb4:	24630000 	addiu	v1,v1,0
			85eb4: R_MIPS_LO16	BMIExecute
   85eb8:	afa00018 	sw	zero,24(sp)
   85ebc:	0060f809 	jalr	v1
   85ec0:	02003821 	move	a3,s0
   85ec4:	08021709 	j	85c24 <ol_ath_download_firmware+0x108>
			85ec4: R_MIPS_26	.text
   85ec8:	24021234 	li	v0,4660
   85ecc:	3c020054 	lui	v0,0x54
   85ed0:	08021776 	j	85dd8 <ol_ath_download_firmware+0x2bc>
			85ed0: R_MIPS_26	.text
   85ed4:	34450658 	ori	a1,v0,0x658

/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

000a436c <ol_ath_pci_resume>:
   a436c:	27bdffd0 	addiu	sp,sp,-48
   a4370:	3c030000 	lui	v1,0x0
			a4370: R_MIPS_HI16	pci_enable_device
   a4374:	24630000 	addiu	v1,v1,0
			a4374: R_MIPS_LO16	pci_enable_device
   a4378:	afb00018 	sw	s0,24(sp)
   a437c:	afbf002c 	sw	ra,44(sp)
   a4380:	00808021 	move	s0,a0
   a4384:	afb40028 	sw	s4,40(sp)
   a4388:	afb30024 	sw	s3,36(sp)
   a438c:	afb20020 	sw	s2,32(sp)
   a4390:	afb1001c 	sw	s1,28(sp)
   a4394:	0060f809 	jalr	v1
   a4398:	8c9100a0 	lw	s1,160(a0)
   a439c:	50400009 	beqzl	v0,a43c4 <ol_ath_pci_resume+0x58>
   a43a0:	3c020000 	lui	v0,0x0
			a43a0: R_MIPS_HI16	pci_bus_read_config_dword
   a43a4:	8fbf002c 	lw	ra,44(sp)
   a43a8:	8fb40028 	lw	s4,40(sp)
   a43ac:	8fb30024 	lw	s3,36(sp)
   a43b0:	8fb20020 	lw	s2,32(sp)
   a43b4:	8fb1001c 	lw	s1,28(sp)
   a43b8:	8fb00018 	lw	s0,24(sp)
   a43bc:	03e00008 	jr	ra
   a43c0:	27bd0030 	addiu	sp,sp,48
   a43c4:	8e040008 	lw	a0,8(s0)
   a43c8:	8e05001c 	lw	a1,28(s0)
   a43cc:	27b30010 	addiu	s3,sp,16
   a43d0:	24520000 	addiu	s2,v0,0
			a43d0: R_MIPS_LO16	pci_bus_read_config_dword
   a43d4:	24060044 	li	a2,68
   a43d8:	0240f809 	jalr	s2
   a43dc:	02603821 	move	a3,s3
   a43e0:	93a30013 	lbu	v1,19(sp)
   a43e4:	14600009 	bnez	v1,a440c <ol_ath_pci_resume+0xa0>
   a43e8:	3c030000 	lui	v1,0x0
			a43e8: R_MIPS_HI16	pci_restore_state
   a43ec:	3c030000 	lui	v1,0x0
			a43ec: R_MIPS_HI16	__ol_ath_resume
   a43f0:	24630000 	addiu	v1,v1,0
			a43f0: R_MIPS_LO16	__ol_ath_resume
   a43f4:	0060f809 	jalr	v1
   a43f8:	02202021 	move	a0,s1
   a43fc:	2404ffff 	li	a0,-1
   a4400:	0002200a 	movz	a0,zero,v0
   a4404:	080290e9 	j	a43a4 <ol_ath_pci_resume+0x38>
			a4404: R_MIPS_26	.text
   a4408:	00801021 	move	v0,a0
   a440c:	24630000 	addiu	v1,v1,0
			a440c: R_MIPS_LO16	pci_restore_state
   a4410:	0060f809 	jalr	v1
   a4414:	02002021 	move	a0,s0
   a4418:	3c020000 	lui	v0,0x0
			a4418: R_MIPS_HI16	pci_bus_write_config_dword
   a441c:	8fa70010 	lw	a3,16(sp)
   a4420:	24060044 	li	a2,68
   a4424:	8e040008 	lw	a0,8(s0)
   a4428:	24540000 	addiu	s4,v0,0
			a4428: R_MIPS_LO16	pci_bus_write_config_dword
   a442c:	8e05001c 	lw	a1,28(s0)
   a4430:	2402ff00 	li	v0,-256
   a4434:	0280f809 	jalr	s4
   a4438:	00e23824 	and	a3,a3,v0
   a443c:	24060040 	li	a2,64
   a4440:	8e040008 	lw	a0,8(s0)
   a4444:	02603821 	move	a3,s3
   a4448:	0240f809 	jalr	s2
   a444c:	8e05001c 	lw	a1,28(s0)
   a4450:	8fa30010 	lw	v1,16(sp)
   a4454:	3062ff00 	andi	v0,v1,0xff00
   a4458:	5040ffe5 	beqzl	v0,a43f0 <ol_ath_pci_resume+0x84>
   a445c:	3c030000 	lui	v1,0x0
			a445c: R_MIPS_HI16	__ol_ath_resume
   a4460:	3c07ffff 	lui	a3,0xffff
   a4464:	8e05001c 	lw	a1,28(s0)
   a4468:	8e040008 	lw	a0,8(s0)
   a446c:	24060040 	li	a2,64
   a4470:	34e700ff 	ori	a3,a3,0xff
   a4474:	0280f809 	jalr	s4
   a4478:	00673824 	and	a3,v1,a3
   a447c:	080290fc 	j	a43f0 <ol_ath_pci_resume+0x84>
			a447c: R_MIPS_26	.text
   a4480:	3c030000 	lui	v1,0x0
			a4480: R_MIPS_HI16	__ol_ath_resume

000a4484 <ol_ath_pci_suspend>:
   a4484:	27bdffe0 	addiu	sp,sp,-32
   a4488:	3c030000 	lui	v1,0x0
			a4488: R_MIPS_HI16	__ol_ath_suspend
   a448c:	afb00018 	sw	s0,24(sp)
   a4490:	00808021 	move	s0,a0
   a4494:	afbf001c 	sw	ra,28(sp)
   a4498:	24630000 	addiu	v1,v1,0
			a4498: R_MIPS_LO16	__ol_ath_suspend
   a449c:	0060f809 	jalr	v1
   a44a0:	8c8400a0 	lw	a0,160(a0)
   a44a4:	10400005 	beqz	v0,a44bc <ol_ath_pci_suspend+0x38>
   a44a8:	8fbf001c 	lw	ra,28(sp)
   a44ac:	2402ffff 	li	v0,-1
   a44b0:	8fb00018 	lw	s0,24(sp)
   a44b4:	03e00008 	jr	ra
   a44b8:	27bd0020 	addiu	sp,sp,32
   a44bc:	3c030000 	lui	v1,0x0
			a44bc: R_MIPS_HI16	pci_bus_read_config_dword
   a44c0:	8e040008 	lw	a0,8(s0)
   a44c4:	8e05001c 	lw	a1,28(s0)
   a44c8:	24060044 	li	a2,68
   a44cc:	24630000 	addiu	v1,v1,0
			a44cc: R_MIPS_LO16	pci_bus_read_config_dword
   a44d0:	0060f809 	jalr	v1
   a44d4:	27a70010 	addiu	a3,sp,16
   a44d8:	24020003 	li	v0,3
   a44dc:	93a40013 	lbu	a0,19(sp)
   a44e0:	10820012 	beq	a0,v0,a452c <ol_ath_pci_suspend+0xa8>
   a44e4:	3c030000 	lui	v1,0x0
			a44e4: R_MIPS_HI16	pci_save_state
   a44e8:	24630000 	addiu	v1,v1,0
			a44e8: R_MIPS_LO16	pci_save_state
   a44ec:	0060f809 	jalr	v1
   a44f0:	02002021 	move	a0,s0
   a44f4:	3c020000 	lui	v0,0x0
			a44f4: R_MIPS_HI16	pci_disable_device
   a44f8:	24420000 	addiu	v0,v0,0
			a44f8: R_MIPS_LO16	pci_disable_device
   a44fc:	0040f809 	jalr	v0
   a4500:	02002021 	move	a0,s0
   a4504:	2402ff00 	li	v0,-256
   a4508:	8fa70010 	lw	a3,16(sp)
   a450c:	3c030000 	lui	v1,0x0
			a450c: R_MIPS_HI16	pci_bus_write_config_dword
   a4510:	8e05001c 	lw	a1,28(s0)
   a4514:	24060044 	li	a2,68
   a4518:	8e040008 	lw	a0,8(s0)
   a451c:	24630000 	addiu	v1,v1,0
			a451c: R_MIPS_LO16	pci_bus_write_config_dword
   a4520:	00e23824 	and	a3,a3,v0
   a4524:	0060f809 	jalr	v1
   a4528:	34e70003 	ori	a3,a3,0x3
   a452c:	8fbf001c 	lw	ra,28(sp)
   a4530:	00001021 	move	v0,zero
   a4534:	8fb00018 	lw	s0,24(sp)
   a4538:	03e00008 	jr	ra
   a453c:	27bd0020 	addiu	sp,sp,32

000a4540 <ath_pci_msi_fw_handler>:
   a4540:	27bdffe8 	addiu	sp,sp,-24
   a4544:	3c030000 	lui	v1,0x0
			a4544: R_MIPS_HI16	HIF_fw_interrupt_handler
   a4548:	afbf0014 	sw	ra,20(sp)
   a454c:	24630000 	addiu	v1,v1,0
			a454c: R_MIPS_LO16	HIF_fw_interrupt_handler
   a4550:	8ca23918 	lw	v0,14616(a1)
   a4554:	00402821 	move	a1,v0
   a4558:	0060f809 	jalr	v1
   a455c:	8c4400c8 	lw	a0,200(v0)
   a4560:	24020001 	li	v0,1
   a4564:	8fbf0014 	lw	ra,20(sp)
   a4568:	03e00008 	jr	ra
   a456c:	27bd0018 	addiu	sp,sp,24

000a4570 <ath_tasklet>:
   a4570:	27bdffd8 	addiu	sp,sp,-40
   a4574:	3c030000 	lui	v1,0x0
			a4574: R_MIPS_HI16	HIF_fw_interrupt_handler
   a4578:	afbf0024 	sw	ra,36(sp)
   a457c:	24630000 	addiu	v1,v1,0
			a457c: R_MIPS_LO16	HIF_fw_interrupt_handler
   a4580:	afb10020 	sw	s1,32(sp)
   a4584:	afb0001c 	sw	s0,28(sp)
   a4588:	8c913918 	lw	s1,14616(a0)
   a458c:	02202821 	move	a1,s1
   a4590:	0060f809 	jalr	v1
   a4594:	8e2400c8 	lw	a0,200(s1)
   a4598:	3c020000 	lui	v0,0x0
			a4598: R_MIPS_HI16	CE_per_engine_service_any
   a459c:	8e2400c8 	lw	a0,200(s1)
   a45a0:	24420000 	addiu	v0,v0,0
			a45a0: R_MIPS_LO16	CE_per_engine_service_any
   a45a4:	0040f809 	jalr	v0
   a45a8:	02202821 	move	a1,s1
   a45ac:	8e2300ac 	lw	v1,172(s1)
   a45b0:	14600019 	bnez	v1,a4618 <ath_tasklet+0xa8>
   a45b4:	8fbf0024 	lw	ra,36(sp)
   a45b8:	3c100000 	lui	s0,0x0
			a45b8: R_MIPS_HI16	targetdef
   a45bc:	8e270000 	lw	a3,0(s1)
   a45c0:	8e020000 	lw	v0,0(s0)
			a45c0: R_MIPS_LO16	targetdef
   a45c4:	8c430114 	lw	v1,276(v0)
   a45c8:	8c45012c 	lw	a1,300(v0)
   a45cc:	8c460138 	lw	a2,312(v0)
   a45d0:	8c440134 	lw	a0,308(v0)
   a45d4:	3c020000 	lui	v0,0x0
			a45d4: R_MIPS_HI16	iowrite32
   a45d8:	00a32825 	or	a1,a1,v1
   a45dc:	00e52821 	addu	a1,a3,a1
   a45e0:	24420000 	addiu	v0,v0,0
			a45e0: R_MIPS_LO16	iowrite32
   a45e4:	0040f809 	jalr	v0
   a45e8:	00c42025 	or	a0,a2,a0
   a45ec:	8e030000 	lw	v1,0(s0)
			a45ec: R_MIPS_LO16	targetdef
   a45f0:	8e250000 	lw	a1,0(s1)
   a45f4:	8c620114 	lw	v0,276(v1)
   a45f8:	8c64012c 	lw	a0,300(v1)
   a45fc:	3c030000 	lui	v1,0x0
			a45fc: R_MIPS_HI16	ioread32
   a4600:	24630000 	addiu	v1,v1,0
			a4600: R_MIPS_LO16	ioread32
   a4604:	00822025 	or	a0,a0,v0
   a4608:	0060f809 	jalr	v1
   a460c:	00a42021 	addu	a0,a1,a0
   a4610:	afa20010 	sw	v0,16(sp)
   a4614:	8fbf0024 	lw	ra,36(sp)
   a4618:	8fb10020 	lw	s1,32(sp)
   a461c:	8fb0001c 	lw	s0,28(sp)
   a4620:	03e00008 	jr	ra
   a4624:	27bd0028 	addiu	sp,sp,40

000a4628 <ol_ath_pci_nointrs>:
   a4628:	27bdffd8 	addiu	sp,sp,-40
   a462c:	afb10018 	sw	s1,24(sp)
   a4630:	afbf0024 	sw	ra,36(sp)
   a4634:	afb30020 	sw	s3,32(sp)
   a4638:	afb2001c 	sw	s2,28(sp)
   a463c:	afb00014 	sw	s0,20(sp)
   a4640:	8c923918 	lw	s2,14616(a0)
   a4644:	8e4200ac 	lw	v0,172(s2)
   a4648:	18400015 	blez	v0,a46a0 <ol_ath_pci_nointrs+0x78>
   a464c:	00808821 	move	s1,a0
   a4650:	3c020000 	lui	v0,0x0
			a4650: R_MIPS_HI16	free_irq
   a4654:	00008021 	move	s0,zero
   a4658:	24530000 	addiu	s3,v0,0
			a4658: R_MIPS_LO16	free_irq
   a465c:	8e240028 	lw	a0,40(s1)
   a4660:	02202821 	move	a1,s1
   a4664:	02042021 	addu	a0,s0,a0
   a4668:	0260f809 	jalr	s3
   a466c:	26100001 	addiu	s0,s0,1
   a4670:	8e4200ac 	lw	v0,172(s2)
   a4674:	0202102a 	slt	v0,s0,v0
   a4678:	5440fff9 	bnezl	v0,a4660 <ol_ath_pci_nointrs+0x38>
   a467c:	8e240028 	lw	a0,40(s1)
   a4680:	ae4000ac 	sw	zero,172(s2)
   a4684:	8fbf0024 	lw	ra,36(sp)
   a4688:	8fb30020 	lw	s3,32(sp)
   a468c:	8fb2001c 	lw	s2,28(sp)
   a4690:	8fb10018 	lw	s1,24(sp)
   a4694:	8fb00014 	lw	s0,20(sp)
   a4698:	03e00008 	jr	ra
   a469c:	27bd0028 	addiu	sp,sp,40
   a46a0:	3c190000 	lui	t9,0x0
			a46a0: R_MIPS_HI16	free_irq
   a46a4:	8c840028 	lw	a0,40(a0)
   a46a8:	02202821 	move	a1,s1
   a46ac:	8fbf0024 	lw	ra,36(sp)
   a46b0:	8fb30020 	lw	s3,32(sp)
   a46b4:	27390000 	addiu	t9,t9,0
			a46b4: R_MIPS_LO16	free_irq
   a46b8:	8fb2001c 	lw	s2,28(sp)
   a46bc:	8fb10018 	lw	s1,24(sp)
   a46c0:	8fb00014 	lw	s0,20(sp)
   a46c4:	03200008 	jr	t9
   a46c8:	27bd0028 	addiu	sp,sp,40

000a46cc <ol_ath_pci_remove>:
   a46cc:	27bdffd8 	addiu	sp,sp,-40
   a46d0:	afb30020 	sw	s3,32(sp)
   a46d4:	afbf0024 	sw	ra,36(sp)
   a46d8:	afb2001c 	sw	s2,28(sp)
   a46dc:	afb10018 	sw	s1,24(sp)
   a46e0:	afb00014 	sw	s0,20(sp)
   a46e4:	8c9200a0 	lw	s2,160(a0)
   a46e8:	16400008 	bnez	s2,a470c <ol_ath_pci_remove+0x40>
   a46ec:	00809821 	move	s3,a0
   a46f0:	8fbf0024 	lw	ra,36(sp)
   a46f4:	8fb30020 	lw	s3,32(sp)
   a46f8:	8fb2001c 	lw	s2,28(sp)
   a46fc:	8fb10018 	lw	s1,24(sp)
   a4700:	8fb00014 	lw	s0,20(sp)
   a4704:	03e00008 	jr	ra
   a4708:	27bd0028 	addiu	sp,sp,40
   a470c:	3c020000 	lui	v0,0x0
			a470c: R_MIPS_HI16	ol_ath_pci_nointrs
   a4710:	8e503918 	lw	s0,14616(s2)
   a4714:	02402021 	move	a0,s2
   a4718:	24420000 	addiu	v0,v0,0
			a4718: R_MIPS_LO16	ol_ath_pci_nointrs
   a471c:	0040f809 	jalr	v0
   a4720:	8e510020 	lw	s1,32(s2)
   a4724:	3c020000 	lui	v0,0x0
			a4724: R_MIPS_HI16	tasklet_kill
   a4728:	24420000 	addiu	v0,v0,0
			a4728: R_MIPS_LO16	tasklet_kill
   a472c:	0040f809 	jalr	v0
   a4730:	260400b0 	addiu	a0,s0,176
   a4734:	3c030000 	lui	v1,0x0
			a4734: R_MIPS_HI16	__ol_ath_detach
   a4738:	24630000 	addiu	v1,v1,0
			a4738: R_MIPS_LO16	__ol_ath_detach
   a473c:	0060f809 	jalr	v1
   a4740:	02402021 	move	a0,s2
   a4744:	3c020000 	lui	v0,0x0
			a4744: R_MIPS_HI16	ath_pci_device_reset
   a4748:	24420000 	addiu	v0,v0,0
			a4748: R_MIPS_LO16	ath_pci_device_reset
   a474c:	0040f809 	jalr	v0
   a4750:	02002021 	move	a0,s0
   a4754:	3c020000 	lui	v0,0x0
			a4754: R_MIPS_HI16	kfree
   a4758:	24420000 	addiu	v0,v0,0
			a4758: R_MIPS_LO16	kfree
   a475c:	0040f809 	jalr	v0
   a4760:	02002021 	move	a0,s0
   a4764:	3c020000 	lui	v0,0x0
			a4764: R_MIPS_HI16	pci_iounmap
   a4768:	02202821 	move	a1,s1
   a476c:	ae6000a0 	sw	zero,160(s3)
   a4770:	24420000 	addiu	v0,v0,0
			a4770: R_MIPS_LO16	pci_iounmap
   a4774:	0040f809 	jalr	v0
   a4778:	02602021 	move	a0,s3
   a477c:	3c020000 	lui	v0,0x0
			a477c: R_MIPS_HI16	pci_release_region
   a4780:	00002821 	move	a1,zero
   a4784:	24420000 	addiu	v0,v0,0
			a4784: R_MIPS_LO16	pci_release_region
   a4788:	0040f809 	jalr	v0
   a478c:	02602021 	move	a0,s3
   a4790:	3c020000 	lui	v0,0x0
			a4790: R_MIPS_HI16	pci_clear_master
   a4794:	24420000 	addiu	v0,v0,0
			a4794: R_MIPS_LO16	pci_clear_master
   a4798:	0040f809 	jalr	v0
   a479c:	02602021 	move	a0,s3
   a47a0:	3c020000 	lui	v0,0x0
			a47a0: R_MIPS_HI16	pci_disable_device
   a47a4:	24420000 	addiu	v0,v0,0
			a47a4: R_MIPS_LO16	pci_disable_device
   a47a8:	0040f809 	jalr	v0
   a47ac:	02602021 	move	a0,s3
   a47b0:	3c040000 	lui	a0,0x0
			a47b0: R_MIPS_HI16	$LC0
   a47b4:	3c190000 	lui	t9,0x0
			a47b4: R_MIPS_HI16	printk
   a47b8:	8fbf0024 	lw	ra,36(sp)
   a47bc:	8fb30020 	lw	s3,32(sp)
   a47c0:	24840000 	addiu	a0,a0,0
			a47c0: R_MIPS_LO16	$LC0
   a47c4:	8fb2001c 	lw	s2,28(sp)
   a47c8:	27390000 	addiu	t9,t9,0
			a47c8: R_MIPS_LO16	printk
   a47cc:	8fb10018 	lw	s1,24(sp)
   a47d0:	8fb00014 	lw	s0,20(sp)
   a47d4:	03200008 	jr	t9
   a47d8:	27bd0028 	addiu	sp,sp,40

000a47dc <ol_ath_pci_configure>:
   a47dc:	27bdffc0 	addiu	sp,sp,-64
   a47e0:	afb5002c 	sw	s5,44(sp)
   a47e4:	00c0a821 	move	s5,a2
   a47e8:	afb30024 	sw	s3,36(sp)
   a47ec:	00a09821 	move	s3,a1
   a47f0:	afb1001c 	sw	s1,28(sp)
   a47f4:	00808821 	move	s1,a0
   a47f8:	afbf003c 	sw	ra,60(sp)
   a47fc:	afbe0038 	sw	s8,56(sp)
   a4800:	afb70034 	sw	s7,52(sp)
   a4804:	afb60030 	sw	s6,48(sp)
   a4808:	afb40028 	sw	s4,40(sp)
   a480c:	afb20020 	sw	s2,32(sp)
   a4810:	afb00018 	sw	s0,24(sp)
   a4814:	8c840008 	lw	a0,8(a0)
   a4818:	8c8200a0 	lw	v0,160(a0)
   a481c:	0002102b 	sltu	v0,zero,v0
   a4820:	00028036 	tne	zero,v0,0x200
   a4824:	ac8500a0 	sw	a1,160(a0)
   a4828:	24a302c0 	addiu	v1,a1,704
   a482c:	ae250010 	sw	a1,16(s1)
   a4830:	ae2300a8 	sw	v1,168(s1)
   a4834:	8e220000 	lw	v0,0(s1)
   a4838:	aca20020 	sw	v0,32(a1)
   a483c:	8e220008 	lw	v0,8(s1)
   a4840:	8c430100 	lw	v1,256(v0)
   a4844:	1060004c 	beqz	v1,a4978 <ol_ath_pci_configure+0x19c>
   a4848:	8e240000 	lw	a0,0(s1)
   a484c:	8c420104 	lw	v0,260(v0)
   a4850:	00431023 	subu	v0,v0,v1
   a4854:	24420001 	addiu	v0,v0,1
   a4858:	00821021 	addu	v0,a0,v0
   a485c:	3c170001 	lui	s7,0x1
			a485c: R_MIPS_HI16	.rodata
   a4860:	ae62001c 	sw	v0,28(s3)
   a4864:	3c020000 	lui	v0,0x0
			a4864: R_MIPS_HI16	dev_driver_string
   a4868:	8e240008 	lw	a0,8(s1)
   a486c:	24500000 	addiu	s0,v0,0
			a486c: R_MIPS_LO16	dev_driver_string
   a4870:	0200f809 	jalr	s0
   a4874:	24840058 	addiu	a0,a0,88
   a4878:	3c030000 	lui	v1,0x0
			a4878: R_MIPS_HI16	printk
   a487c:	8e270008 	lw	a3,8(s1)
   a4880:	3c040000 	lui	a0,0x0
			a4880: R_MIPS_HI16	$LC1
   a4884:	24760000 	addiu	s6,v1,0
			a4884: R_MIPS_LO16	printk
   a4888:	24840000 	addiu	a0,a0,0
			a4888: R_MIPS_LO16	$LC1
   a488c:	00402821 	move	a1,v0
   a4890:	8ce60060 	lw	a2,96(a3)
   a4894:	02c0f809 	jalr	s6
   a4898:	02203821 	move	a3,s1
   a489c:	3c05000a 	lui	a1,0xa
			a489c: R_MIPS_HI16	.text
   a48a0:	8e230008 	lw	v1,8(s1)
   a48a4:	3c020000 	lui	v0,0x0
			a48a4: R_MIPS_HI16	tasklet_init
   a48a8:	24a54570 	addiu	a1,a1,17776
			a48a8: R_MIPS_LO16	.text
   a48ac:	262400b0 	addiu	a0,s1,176
   a48b0:	24630058 	addiu	v1,v1,88
   a48b4:	24420000 	addiu	v0,v0,0
			a48b4: R_MIPS_LO16	tasklet_init
   a48b8:	ae6301f8 	sw	v1,504(s3)
   a48bc:	0040f809 	jalr	v0
   a48c0:	02603021 	move	a2,s3
   a48c4:	3c040000 	lui	a0,0x0
			a48c4: R_MIPS_HI16	$LC2
   a48c8:	26e503e0 	addiu	a1,s7,992
			a48c8: R_MIPS_LO16	.rodata
   a48cc:	24840000 	addiu	a0,a0,0
			a48cc: R_MIPS_LO16	$LC2
   a48d0:	02c0f809 	jalr	s6
   a48d4:	00003021 	move	a2,zero
   a48d8:	3c050000 	lui	a1,0x0
			a48d8: R_MIPS_HI16	ath_pci_interrupt_handler
   a48dc:	8e240008 	lw	a0,8(s1)
   a48e0:	00003021 	move	a2,zero
   a48e4:	24a50000 	addiu	a1,a1,0
			a48e4: R_MIPS_LO16	ath_pci_interrupt_handler
   a48e8:	24070080 	li	a3,128
   a48ec:	8c8300fc 	lw	v1,252(a0)
   a48f0:	ae630028 	sw	v1,40(s3)
   a48f4:	3c030000 	lui	v1,0x0
			a48f4: R_MIPS_HI16	request_threaded_irq
   a48f8:	8e220008 	lw	v0,8(s1)
   a48fc:	24630000 	addiu	v1,v1,0
			a48fc: R_MIPS_LO16	request_threaded_irq
