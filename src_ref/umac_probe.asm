
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

000a4900 <ol_ath_pci_configure+0x124>:
   a4900:	8c4400fc 	lw	a0,252(v0)
   a4904:	afb30010 	sw	s3,16(sp)
   a4908:	0060f809 	jalr	v1
   a490c:	afb30014 	sw	s3,20(sp)
   a4910:	1040001e 	beqz	v0,a498c <ol_ath_pci_configure+0x1b0>
   a4914:	0040a021 	move	s4,v0
   a4918:	8e240008 	lw	a0,8(s1)
   a491c:	0200f809 	jalr	s0
   a4920:	24840058 	addiu	a0,a0,88
   a4924:	3c040000 	lui	a0,0x0
			a4924: R_MIPS_HI16	$LC3
   a4928:	8e230008 	lw	v1,8(s1)
   a492c:	00402821 	move	a1,v0
   a4930:	24840000 	addiu	a0,a0,0
			a4930: R_MIPS_LO16	$LC3
   a4934:	02c0f809 	jalr	s6
   a4938:	8c660060 	lw	a2,96(v1)
   a493c:	8e220008 	lw	v0,8(s1)
   a4940:	ac4000a0 	sw	zero,160(v0)
   a4944:	8fbf003c 	lw	ra,60(sp)
   a4948:	02801021 	move	v0,s4
   a494c:	8fbe0038 	lw	s8,56(sp)
   a4950:	8fb70034 	lw	s7,52(sp)
   a4954:	8fb60030 	lw	s6,48(sp)
   a4958:	8fb5002c 	lw	s5,44(sp)
   a495c:	8fb40028 	lw	s4,40(sp)
   a4960:	8fb30024 	lw	s3,36(sp)
   a4964:	8fb20020 	lw	s2,32(sp)
   a4968:	8fb1001c 	lw	s1,28(sp)
   a496c:	8fb00018 	lw	s0,24(sp)
   a4970:	03e00008 	jr	ra
   a4974:	27bd0040 	addiu	sp,sp,64
   a4978:	8c420104 	lw	v0,260(v0)
   a497c:	5440ffb5 	bnezl	v0,a4854 <ol_ath_pci_configure+0x78>
   a4980:	00431023 	subu	v0,v0,v1
   a4984:	08029217 	j	a485c <ol_ath_pci_configure+0x80>
			a4984: R_MIPS_26	.text
   a4988:	00821021 	addu	v0,a0,v0
   a498c:	3c040000 	lui	a0,0x0
			a498c: R_MIPS_HI16	$LC4
   a4990:	3c1e0000 	lui	s8,0x0
			a4990: R_MIPS_HI16	ath_hostdef
   a4994:	02c0f809 	jalr	s6
   a4998:	24840000 	addiu	a0,a0,0
			a4998: R_MIPS_LO16	$LC4
   a499c:	8fc30000 	lw	v1,0(s8)
			a499c: R_MIPS_LO16	ath_hostdef
   a49a0:	8e260000 	lw	a2,0(s1)
   a49a4:	8c6200a0 	lw	v0,160(v1)
   a49a8:	8c6500a8 	lw	a1,168(v1)
   a49ac:	8c6400ac 	lw	a0,172(v1)
   a49b0:	00a22821 	addu	a1,a1,v0
   a49b4:	3c020000 	lui	v0,0x0
			a49b4: R_MIPS_HI16	iowrite32
   a49b8:	24420000 	addiu	v0,v0,0
			a49b8: R_MIPS_LO16	iowrite32
   a49bc:	0040f809 	jalr	v0
   a49c0:	00c52821 	addu	a1,a2,a1
   a49c4:	3c020000 	lui	v0,0x0
			a49c4: R_MIPS_HI16	ath_pci_targ_is_awake
   a49c8:	24500000 	addiu	s0,v0,0
			a49c8: R_MIPS_LO16	ath_pci_targ_is_awake
   a49cc:	0200f809 	jalr	s0
   a49d0:	8e240000 	lw	a0,0(s1)
   a49d4:	1040fffd 	beqz	v0,a49cc <ol_ath_pci_configure+0x1f0>
   a49d8:	3c030000 	lui	v1,0x0
			a49d8: R_MIPS_HI16	targetdef
   a49dc:	8e270000 	lw	a3,0(s1)
   a49e0:	2412012b 	li	s2,299
   a49e4:	8c620000 	lw	v0,0(v1)
			a49e4: R_MIPS_LO16	targetdef
   a49e8:	8c430114 	lw	v1,276(v0)
   a49ec:	8c45012c 	lw	a1,300(v0)
   a49f0:	8c460138 	lw	a2,312(v0)
   a49f4:	8c440134 	lw	a0,308(v0)
   a49f8:	3c020000 	lui	v0,0x0
			a49f8: R_MIPS_HI16	iowrite32
   a49fc:	00a32825 	or	a1,a1,v1
   a4a00:	00e52821 	addu	a1,a3,a1
   a4a04:	24420000 	addiu	v0,v0,0
			a4a04: R_MIPS_LO16	iowrite32
   a4a08:	0040f809 	jalr	v0
   a4a0c:	00c42025 	or	a0,a2,a0
   a4a10:	8fc20000 	lw	v0,0(s8)
			a4a10: R_MIPS_LO16	ath_hostdef
   a4a14:	8e260000 	lw	a2,0(s1)
   a4a18:	8c4300a0 	lw	v1,160(v0)
   a4a1c:	8c4500a8 	lw	a1,168(v0)
   a4a20:	8c4400a4 	lw	a0,164(v0)
   a4a24:	00a32821 	addu	a1,a1,v1
   a4a28:	3c030000 	lui	v1,0x0
			a4a28: R_MIPS_HI16	iowrite32
   a4a2c:	24630000 	addiu	v1,v1,0
			a4a2c: R_MIPS_LO16	iowrite32
   a4a30:	0060f809 	jalr	v1
   a4a34:	00c52821 	addu	a1,a2,a1
   a4a38:	3c020000 	lui	v0,0x0
			a4a38: R_MIPS_HI16	targetdef
   a4a3c:	ae2000ac 	sw	zero,172(s1)
   a4a40:	8c440000 	lw	a0,0(v0)
			a4a40: R_MIPS_LO16	targetdef
   a4a44:	8c82011c 	lw	v0,284(a0)
   a4a48:	ae2200d4 	sw	v0,212(s1)
   a4a4c:	3c030000 	lui	v1,0x0
			a4a4c: R_MIPS_HI16	targetdef
   a4a50:	8c620000 	lw	v0,0(v1)
			a4a50: R_MIPS_LO16	targetdef
   a4a54:	8e230000 	lw	v1,0(s1)
   a4a58:	8c44010c 	lw	a0,268(v0)
   a4a5c:	00642021 	addu	a0,v1,a0
   a4a60:	3c030000 	lui	v1,0x0
			a4a60: R_MIPS_HI16	ioread32
   a4a64:	24630000 	addiu	v1,v1,0
			a4a64: R_MIPS_LO16	ioread32
   a4a68:	0060f809 	jalr	v1
   a4a6c:	00000000 	nop
   a4a70:	8fc30000 	lw	v1,0(s8)
			a4a70: R_MIPS_LO16	ath_hostdef
   a4a74:	8c6400bc 	lw	a0,188(v1)
   a4a78:	00441024 	and	v0,v0,a0
   a4a7c:	1440001f 	bnez	v0,a4afc <ol_ath_pci_configure+0x320>
   a4a80:	3c030000 	lui	v1,0x0
			a4a80: R_MIPS_HI16	targetdef
   a4a84:	8e270000 	lw	a3,0(s1)
   a4a88:	24100009 	li	s0,9
   a4a8c:	8c620000 	lw	v0,0(v1)
			a4a8c: R_MIPS_LO16	targetdef
   a4a90:	8c430114 	lw	v1,276(v0)
   a4a94:	8c45012c 	lw	a1,300(v0)
   a4a98:	8c460138 	lw	a2,312(v0)
   a4a9c:	8c440134 	lw	a0,308(v0)
   a4aa0:	3c020000 	lui	v0,0x0
			a4aa0: R_MIPS_HI16	iowrite32
   a4aa4:	00a32825 	or	a1,a1,v1
   a4aa8:	00e52821 	addu	a1,a3,a1
   a4aac:	24420000 	addiu	v0,v0,0
			a4aac: R_MIPS_LO16	iowrite32
   a4ab0:	0040f809 	jalr	v0
   a4ab4:	00c42025 	or	a0,a2,a0
   a4ab8:	3c030000 	lui	v1,0x0
			a4ab8: R_MIPS_HI16	__udelay
   a4abc:	240403e8 	li	a0,1000
   a4ac0:	24630000 	addiu	v1,v1,0
			a4ac0: R_MIPS_LO16	__udelay
   a4ac4:	0060f809 	jalr	v1
   a4ac8:	2610ffff 	addiu	s0,s0,-1
   a4acc:	2402ffff 	li	v0,-1
   a4ad0:	1602fffa 	bne	s0,v0,a4abc <ol_ath_pci_configure+0x2e0>
   a4ad4:	3c030000 	lui	v1,0x0
			a4ad4: R_MIPS_HI16	__udelay
   a4ad8:	2652ffff 	addiu	s2,s2,-1
   a4adc:	1642ffdc 	bne	s2,v0,a4a50 <ol_ath_pci_configure+0x274>
   a4ae0:	3c030000 	lui	v1,0x0
			a4ae0: R_MIPS_HI16	targetdef
   a4ae4:	3c040000 	lui	a0,0x0
			a4ae4: R_MIPS_HI16	$LC5
   a4ae8:	26e503e0 	addiu	a1,s7,992
			a4ae8: R_MIPS_LO16	.rodata
   a4aec:	02c0f809 	jalr	s6
   a4af0:	24840000 	addiu	a0,a0,0
			a4af0: R_MIPS_LO16	$LC5
   a4af4:	080292cd 	j	a4b34 <ol_ath_pci_configure+0x358>
			a4af4: R_MIPS_26	.text
   a4af8:	3c020000 	lui	v0,0x0
			a4af8: R_MIPS_HI16	ol_ath_pci_nointrs
   a4afc:	0640fff9 	bltz	s2,a4ae4 <ol_ath_pci_configure+0x308>
   a4b00:	3c030000 	lui	v1,0x0
			a4b00: R_MIPS_HI16	HIF_PCIDeviceProbed
   a4b04:	24630000 	addiu	v1,v1,0
			a4b04: R_MIPS_LO16	HIF_PCIDeviceProbed
   a4b08:	0060f809 	jalr	v1
   a4b0c:	02202021 	move	a0,s1
   a4b10:	54400004 	bnezl	v0,a4b24 <ol_ath_pci_configure+0x348>
   a4b14:	3c040000 	lui	a0,0x0
			a4b14: R_MIPS_HI16	$LC6
   a4b18:	8e2200f8 	lw	v0,248(s1)
   a4b1c:	08029251 	j	a4944 <ol_ath_pci_configure+0x168>
			a4b1c: R_MIPS_26	.text
   a4b20:	aea20000 	sw	v0,0(s5)
   a4b24:	26e503e0 	addiu	a1,s7,992
			a4b24: R_MIPS_LO16	.rodata
   a4b28:	02c0f809 	jalr	s6
   a4b2c:	24840000 	addiu	a0,a0,0
			a4b2c: R_MIPS_LO16	$LC6
   a4b30:	3c020000 	lui	v0,0x0
			a4b30: R_MIPS_HI16	ol_ath_pci_nointrs
   a4b34:	02602021 	move	a0,s3
   a4b38:	24420000 	addiu	v0,v0,0
			a4b38: R_MIPS_LO16	ol_ath_pci_nointrs
   a4b3c:	0040f809 	jalr	v0
   a4b40:	2414fffb 	li	s4,-5
   a4b44:	08029250 	j	a4940 <ol_ath_pci_configure+0x164>
			a4b44: R_MIPS_26	.text
   a4b48:	8e220008 	lw	v0,8(s1)

000a4b4c <ol_ath_pci_probe>:
   a4b4c:	27bdffc0 	addiu	sp,sp,-64
   a4b50:	3c030000 	lui	v1,0x0
			a4b50: R_MIPS_HI16	printk
   a4b54:	afb30024 	sw	s3,36(sp)
   a4b58:	00809821 	move	s3,a0
   a4b5c:	3c040000 	lui	a0,0x0
			a4b5c: R_MIPS_HI16	$LC7
   a4b60:	afbe0038 	sw	s8,56(sp)
   a4b64:	24630000 	addiu	v1,v1,0
			a4b64: R_MIPS_LO16	printk
   a4b68:	afb70034 	sw	s7,52(sp)
   a4b6c:	24840000 	addiu	a0,a0,0
			a4b6c: R_MIPS_LO16	$LC7
   a4b70:	afbf003c 	sw	ra,60(sp)
   a4b74:	afb60030 	sw	s6,48(sp)
   a4b78:	267e0058 	addiu	s8,s3,88
   a4b7c:	afb5002c 	sw	s5,44(sp)
   a4b80:	0000b821 	move	s7,zero
   a4b84:	afb40028 	sw	s4,40(sp)
   a4b88:	afb20020 	sw	s2,32(sp)
   a4b8c:	afb1001c 	sw	s1,28(sp)
   a4b90:	afb00018 	sw	s0,24(sp)
   a4b94:	0060f809 	jalr	v1
   a4b98:	afa50044 	sw	a1,68(sp)
   a4b9c:	3c030000 	lui	v1,0x0
			a4b9c: R_MIPS_HI16	pci_enable_device
   a4ba0:	24630000 	addiu	v1,v1,0
			a4ba0: R_MIPS_LO16	pci_enable_device
   a4ba4:	0060f809 	jalr	v1
   a4ba8:	02602021 	move	a0,s3
   a4bac:	144000d4 	bnez	v0,a4f00 <ol_ath_pci_probe+0x3b4>
   a4bb0:	3c020000 	lui	v0,0x0
			a4bb0: R_MIPS_HI16	$LC9
   a4bb4:	3c030000 	lui	v1,0x0
			a4bb4: R_MIPS_HI16	pci_request_region
   a4bb8:	00002821 	move	a1,zero
   a4bbc:	24460000 	addiu	a2,v0,0
			a4bbc: R_MIPS_LO16	$LC9
   a4bc0:	24630000 	addiu	v1,v1,0
			a4bc0: R_MIPS_LO16	pci_request_region
   a4bc4:	0060f809 	jalr	v1
   a4bc8:	02602021 	move	a0,s3
   a4bcc:	144000be 	bnez	v0,a4ec8 <ol_ath_pci_probe+0x37c>
   a4bd0:	2407ffff 	li	a3,-1
   a4bd4:	3c030000 	lui	v1,0x0
			a4bd4: R_MIPS_HI16	pci_set_dma_mask
   a4bd8:	00003021 	move	a2,zero
   a4bdc:	24630000 	addiu	v1,v1,0
			a4bdc: R_MIPS_LO16	pci_set_dma_mask
   a4be0:	0060f809 	jalr	v1
   a4be4:	02602021 	move	a0,s3
   a4be8:	144000b0 	bnez	v0,a4eac <ol_ath_pci_probe+0x360>
   a4bec:	0040a021 	move	s4,v0
   a4bf0:	3c030000 	lui	v1,0x0
			a4bf0: R_MIPS_HI16	pci_set_consistent_dma_mask
   a4bf4:	2407ffff 	li	a3,-1
   a4bf8:	00003021 	move	a2,zero
   a4bfc:	24630000 	addiu	v1,v1,0
			a4bfc: R_MIPS_LO16	pci_set_consistent_dma_mask
   a4c00:	0060f809 	jalr	v1
   a4c04:	02602021 	move	a0,s3
   a4c08:	144000e7 	bnez	v0,a4fa8 <ol_ath_pci_probe+0x45c>
   a4c0c:	0040a021 	move	s4,v0
   a4c10:	3c020000 	lui	v0,0x0
			a4c10: R_MIPS_HI16	pci_set_master
   a4c14:	24420000 	addiu	v0,v0,0
			a4c14: R_MIPS_LO16	pci_set_master
   a4c18:	0040f809 	jalr	v0
   a4c1c:	02602021 	move	a0,s3
   a4c20:	3c030000 	lui	v1,0x0
			a4c20: R_MIPS_HI16	pci_bus_read_config_dword
   a4c24:	8e640008 	lw	a0,8(s3)
   a4c28:	24060080 	li	a2,128
   a4c2c:	8e65001c 	lw	a1,28(s3)
   a4c30:	24630000 	addiu	v1,v1,0
			a4c30: R_MIPS_LO16	pci_bus_read_config_dword
   a4c34:	0060f809 	jalr	v1
   a4c38:	27a70014 	addiu	a3,sp,20
   a4c3c:	3c030000 	lui	v1,0x0
			a4c3c: R_MIPS_HI16	pci_bus_write_config_dword
   a4c40:	8fa70014 	lw	a3,20(sp)
   a4c44:	2402ff00 	li	v0,-256
   a4c48:	8e65001c 	lw	a1,28(s3)
   a4c4c:	24060080 	li	a2,128
   a4c50:	8e640008 	lw	a0,8(s3)
   a4c54:	24630000 	addiu	v1,v1,0
			a4c54: R_MIPS_LO16	pci_bus_write_config_dword
   a4c58:	0060f809 	jalr	v1
   a4c5c:	00e23824 	and	a3,a3,v0
   a4c60:	3c030000 	lui	v1,0x0
			a4c60: R_MIPS_HI16	pci_iomap
   a4c64:	00002821 	move	a1,zero
   a4c68:	00003021 	move	a2,zero
   a4c6c:	24630000 	addiu	v1,v1,0
			a4c6c: R_MIPS_LO16	pci_iomap
   a4c70:	0060f809 	jalr	v1
   a4c74:	02602021 	move	a0,s3
   a4c78:	104000c3 	beqz	v0,a4f88 <ol_ath_pci_probe+0x43c>
   a4c7c:	00409021 	move	s2,v0
   a4c80:	3c020000 	lui	v0,0x0
			a4c80: R_MIPS_HI16	malloc_sizes
   a4c84:	3c030000 	lui	v1,0x0
			a4c84: R_MIPS_HI16	kmem_cache_alloc
   a4c88:	24420000 	addiu	v0,v0,0
			a4c88: R_MIPS_LO16	malloc_sizes
   a4c8c:	240500d0 	li	a1,208
   a4c90:	24630000 	addiu	v1,v1,0
			a4c90: R_MIPS_LO16	kmem_cache_alloc
   a4c94:	0060f809 	jalr	v1
   a4c98:	8c44002c 	lw	a0,44(v0)
   a4c9c:	3c030000 	lui	v1,0x0
			a4c9c: R_MIPS_HI16	memset
   a4ca0:	00002821 	move	a1,zero
   a4ca4:	240600fc 	li	a2,252
   a4ca8:	24630000 	addiu	v1,v1,0
			a4ca8: R_MIPS_LO16	memset
   a4cac:	00408821 	move	s1,v0
   a4cb0:	0060f809 	jalr	v1
   a4cb4:	00402021 	move	a0,v0
   a4cb8:	122000b1 	beqz	s1,a4f80 <ol_ath_pci_probe+0x434>
   a4cbc:	24020002 	li	v0,2
   a4cc0:	ae320000 	sw	s2,0(s1)
   a4cc4:	ae330008 	sw	s3,8(s1)
   a4cc8:	24040006 	li	a0,6
   a4ccc:	ae3e0004 	sw	s8,4(s1)
   a4cd0:	3c150000 	lui	s5,0x0
			a4cd0: R_MIPS_HI16	ath_hostdef
   a4cd4:	ae33000c 	sw	s3,12(s1)
   a4cd8:	ae3e0094 	sw	s8,148(s1)
   a4cdc:	ae32008c 	sw	s2,140(s1)
   a4ce0:	ae200090 	sw	zero,144(s1)
   a4ce4:	a7a20012 	sh	v0,18(sp)
   a4ce8:	8fa20044 	lw	v0,68(sp)
   a4cec:	8c430004 	lw	v1,4(v0)
   a4cf0:	24020080 	li	v0,128
   a4cf4:	a7a30010 	sh	v1,16(sp)
   a4cf8:	ae2200cc 	sw	v0,204(s1)
   a4cfc:	3c020000 	lui	v0,0x0
			a4cfc: R_MIPS_HI16	hif_register_tbl_attach
   a4d00:	24420000 	addiu	v0,v0,0
			a4d00: R_MIPS_LO16	hif_register_tbl_attach
   a4d04:	0040f809 	jalr	v0
   a4d08:	ae2000d0 	sw	zero,208(s1)
   a4d0c:	3c020000 	lui	v0,0x0
			a4d0c: R_MIPS_HI16	target_register_tbl_attach
   a4d10:	24420000 	addiu	v0,v0,0
			a4d10: R_MIPS_LO16	target_register_tbl_attach
   a4d14:	0040f809 	jalr	v0
   a4d18:	24040007 	li	a0,7
   a4d1c:	3c020000 	lui	v0,0x0
			a4d1c: R_MIPS_HI16	iowrite32
   a4d20:	8ea30000 	lw	v1,0(s5)
			a4d20: R_MIPS_LO16	ath_hostdef
   a4d24:	24560000 	addiu	s6,v0,0
			a4d24: R_MIPS_LO16	iowrite32
   a4d28:	8c6500a8 	lw	a1,168(v1)
   a4d2c:	8c6200a0 	lw	v0,160(v1)
   a4d30:	8c6400ac 	lw	a0,172(v1)
   a4d34:	00a22821 	addu	a1,a1,v0
   a4d38:	02c0f809 	jalr	s6
   a4d3c:	02452821 	addu	a1,s2,a1
   a4d40:	3c020000 	lui	v0,0x0
			a4d40: R_MIPS_HI16	ath_pci_targ_is_awake
   a4d44:	24500000 	addiu	s0,v0,0
			a4d44: R_MIPS_LO16	ath_pci_targ_is_awake
   a4d48:	0200f809 	jalr	s0
   a4d4c:	02402021 	move	a0,s2
   a4d50:	1040fffd 	beqz	v0,a4d48 <ol_ath_pci_probe+0x1fc>
   a4d54:	3c020000 	lui	v0,0x0
			a4d54: R_MIPS_HI16	targetdef
   a4d58:	8c430000 	lw	v1,0(v0)
			a4d58: R_MIPS_LO16	targetdef
   a4d5c:	8c64010c 	lw	a0,268(v1)
   a4d60:	3c030000 	lui	v1,0x0
			a4d60: R_MIPS_HI16	ioread32
   a4d64:	24630000 	addiu	v1,v1,0
			a4d64: R_MIPS_LO16	ioread32
   a4d68:	0060f809 	jalr	v1
   a4d6c:	02442021 	addu	a0,s2,a0
   a4d70:	00408021 	move	s0,v0
   a4d74:	8ea20000 	lw	v0,0(s5)
			a4d74: R_MIPS_LO16	ath_hostdef
   a4d78:	8c4300a0 	lw	v1,160(v0)
   a4d7c:	8c4500a8 	lw	a1,168(v0)
   a4d80:	8c4400a4 	lw	a0,164(v0)
   a4d84:	00a32821 	addu	a1,a1,v1
   a4d88:	02c0f809 	jalr	s6
   a4d8c:	02452821 	addu	a1,s2,a1
   a4d90:	8ea20000 	lw	v0,0(s5)
			a4d90: R_MIPS_LO16	ath_hostdef
   a4d94:	8c4300bc 	lw	v1,188(v0)
   a4d98:	02038024 	and	s0,s0,v1
   a4d9c:	1600006f 	bnez	s0,a4f5c <ol_ath_pci_probe+0x410>
   a4da0:	3c030000 	lui	v1,0x0
			a4da0: R_MIPS_HI16	__ol_ath_attach
   a4da4:	27a50010 	addiu	a1,sp,16
   a4da8:	2626000c 	addiu	a2,s1,12
   a4dac:	00003821 	move	a3,zero
   a4db0:	24630000 	addiu	v1,v1,0
			a4db0: R_MIPS_LO16	__ol_ath_attach
   a4db4:	0060f809 	jalr	v1
   a4db8:	02202021 	move	a0,s1
   a4dbc:	10400034 	beqz	v0,a4e90 <ol_ath_pci_probe+0x344>
   a4dc0:	3c020000 	lui	v0,0x0
			a4dc0: R_MIPS_HI16	ath_pci_device_reset
   a4dc4:	ae6000a0 	sw	zero,160(s3)
   a4dc8:	02202021 	move	a0,s1
   a4dcc:	24420000 	addiu	v0,v0,0
			a4dcc: R_MIPS_LO16	ath_pci_device_reset
   a4dd0:	0040f809 	jalr	v0
   a4dd4:	2414fffb 	li	s4,-5
   a4dd8:	3c020000 	lui	v0,0x0
			a4dd8: R_MIPS_HI16	kfree
   a4ddc:	24420000 	addiu	v0,v0,0
			a4ddc: R_MIPS_LO16	kfree
   a4de0:	0040f809 	jalr	v0
   a4de4:	02202021 	move	a0,s1
   a4de8:	3c040000 	lui	a0,0x0
			a4de8: R_MIPS_HI16	$LC15
   a4dec:	3c050001 	lui	a1,0x1
			a4dec: R_MIPS_HI16	.rodata
   a4df0:	3c030000 	lui	v1,0x0
			a4df0: R_MIPS_HI16	printk
   a4df4:	24840000 	addiu	a0,a0,0
			a4df4: R_MIPS_LO16	$LC15
   a4df8:	24630000 	addiu	v1,v1,0
			a4df8: R_MIPS_LO16	printk
   a4dfc:	0060f809 	jalr	v1
   a4e00:	24a503f8 	addiu	a1,a1,1016
			a4e00: R_MIPS_LO16	.rodata
   a4e04:	3c020000 	lui	v0,0x0
			a4e04: R_MIPS_HI16	pci_iounmap
   a4e08:	02602021 	move	a0,s3
   a4e0c:	24420000 	addiu	v0,v0,0
			a4e0c: R_MIPS_LO16	pci_iounmap
   a4e10:	0040f809 	jalr	v0
   a4e14:	02402821 	move	a1,s2
   a4e18:	3c020000 	lui	v0,0x0
			a4e18: R_MIPS_HI16	pci_release_region
   a4e1c:	00002821 	move	a1,zero
   a4e20:	24420000 	addiu	v0,v0,0
			a4e20: R_MIPS_LO16	pci_release_region
   a4e24:	0040f809 	jalr	v0
   a4e28:	02602021 	move	a0,s3
   a4e2c:	3c030000 	lui	v1,0x0
			a4e2c: R_MIPS_HI16	pci_clear_master
   a4e30:	24630000 	addiu	v1,v1,0
			a4e30: R_MIPS_LO16	pci_clear_master
   a4e34:	0060f809 	jalr	v1
   a4e38:	02602021 	move	a0,s3
   a4e3c:	3c020000 	lui	v0,0x0
			a4e3c: R_MIPS_HI16	pci_disable_device
   a4e40:	24420000 	addiu	v0,v0,0
			a4e40: R_MIPS_LO16	pci_disable_device
   a4e44:	0040f809 	jalr	v0
   a4e48:	02602021 	move	a0,s3
   a4e4c:	12e00003 	beqz	s7,a4e5c <ol_ath_pci_probe+0x310>
   a4e50:	2ae20004 	slti	v0,s7,4
   a4e54:	54400032 	bnezl	v0,a4f20 <ol_ath_pci_probe+0x3d4>
   a4e58:	3c040000 	lui	a0,0x0
			a4e58: R_MIPS_HI16	$LC16
   a4e5c:	8fbf003c 	lw	ra,60(sp)
   a4e60:	02801021 	move	v0,s4
   a4e64:	8fbe0038 	lw	s8,56(sp)
   a4e68:	8fb70034 	lw	s7,52(sp)
   a4e6c:	8fb60030 	lw	s6,48(sp)
   a4e70:	8fb5002c 	lw	s5,44(sp)
   a4e74:	8fb40028 	lw	s4,40(sp)
   a4e78:	8fb30024 	lw	s3,36(sp)
   a4e7c:	8fb20020 	lw	s2,32(sp)
   a4e80:	8fb1001c 	lw	s1,28(sp)
   a4e84:	8fb00018 	lw	s0,24(sp)
   a4e88:	03e00008 	jr	ra
   a4e8c:	27bd0040 	addiu	sp,sp,64
   a4e90:	3c020000 	lui	v0,0x0
			a4e90: R_MIPS_HI16	__ol_ath_suspend_resume_attach
   a4e94:	24420000 	addiu	v0,v0,0
			a4e94: R_MIPS_LO16	__ol_ath_suspend_resume_attach
   a4e98:	0040f809 	jalr	v0
   a4e9c:	8e6400a0 	lw	a0,160(s3)
   a4ea0:	3c030000 	lui	v1,0x0
			a4ea0: R_MIPS_HI16	diag_sc
   a4ea4:	08029397 	j	a4e5c <ol_ath_pci_probe+0x310>
			a4ea4: R_MIPS_26	.text
   a4ea8:	ac710000 	sw	s1,0(v1)
			a4ea8: R_MIPS_LO16	diag_sc
   a4eac:	3c040000 	lui	a0,0x0
			a4eac: R_MIPS_HI16	$LC11
   a4eb0:	3c030000 	lui	v1,0x0
			a4eb0: R_MIPS_HI16	printk
   a4eb4:	24630000 	addiu	v1,v1,0
			a4eb4: R_MIPS_LO16	printk
   a4eb8:	0060f809 	jalr	v1
   a4ebc:	24840000 	addiu	a0,a0,0
			a4ebc: R_MIPS_LO16	$LC11
   a4ec0:	08029390 	j	a4e40 <ol_ath_pci_probe+0x2f4>
			a4ec0: R_MIPS_26	.text
   a4ec4:	3c020000 	lui	v0,0x0
			a4ec4: R_MIPS_HI16	pci_disable_device
   a4ec8:	3c030000 	lui	v1,0x0
			a4ec8: R_MIPS_HI16	dev_driver_string
   a4ecc:	03c02021 	move	a0,s8
   a4ed0:	24630000 	addiu	v1,v1,0
			a4ed0: R_MIPS_LO16	dev_driver_string
   a4ed4:	0060f809 	jalr	v1
   a4ed8:	2414fffb 	li	s4,-5
   a4edc:	3c040000 	lui	a0,0x0
			a4edc: R_MIPS_HI16	$LC10
   a4ee0:	3c030000 	lui	v1,0x0
			a4ee0: R_MIPS_HI16	printk
   a4ee4:	8e660060 	lw	a2,96(s3)
   a4ee8:	24840000 	addiu	a0,a0,0
			a4ee8: R_MIPS_LO16	$LC10
   a4eec:	24630000 	addiu	v1,v1,0
			a4eec: R_MIPS_LO16	printk
   a4ef0:	0060f809 	jalr	v1
   a4ef4:	00402821 	move	a1,v0
   a4ef8:	0802938c 	j	a4e30 <ol_ath_pci_probe+0x2e4>
			a4ef8: R_MIPS_26	.text
   a4efc:	3c030000 	lui	v1,0x0
			a4efc: R_MIPS_HI16	pci_clear_master
