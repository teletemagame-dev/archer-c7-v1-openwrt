
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

00093c00 <ol_transfer_bin_file+0x434>:
   93c00:	24021c00 	li	v0,7168
   93c04:	12420078 	beq	s2,v0,93de8 <ol_transfer_bin_file+0x61c>
   93c08:	3c020000 	lui	v0,0x0
			93c08: R_MIPS_HI16	BMIWriteMemory
   93c0c:	12e0ff66 	beqz	s7,939a8 <ol_transfer_bin_file+0x1dc>
   93c10:	24061c00 	li	a2,7168
   93c14:	3c030000 	lui	v1,0x0
			93c14: R_MIPS_HI16	BMIFastDownload
   93c18:	8ec43654 	lw	a0,13908(s6)
   93c1c:	00c03821 	move	a3,a2
   93c20:	afb60010 	sw	s6,16(sp)
   93c24:	24630000 	addiu	v1,v1,0
			93c24: R_MIPS_LO16	BMIFastDownload
   93c28:	03c02821 	move	a1,s8
   93c2c:	0060f809 	jalr	v1
   93c30:	02203021 	move	a2,s1
   93c34:	08024e75 	j	939d4 <ol_transfer_bin_file+0x208>
			93c34: R_MIPS_26	.text
   93c38:	00408021 	move	s0,v0
   93c3c:	8ec43654 	lw	a0,13908(s6)
   93c40:	00c03821 	move	a3,a2
   93c44:	afb60010 	sw	s6,16(sp)
   93c48:	24630000 	addiu	v1,v1,0
			93c48: R_MIPS_LO16	BMIWriteMemory
   93c4c:	03c02821 	move	a1,s8
   93c50:	0060f809 	jalr	v1
   93c54:	02203021 	move	a2,s1
   93c58:	08024e75 	j	939d4 <ol_transfer_bin_file+0x208>
			93c58: R_MIPS_26	.text
   93c5c:	00408021 	move	s0,v0
   93c60:	3c020000 	lui	v0,0x0
			93c60: R_MIPS_HI16	testmode
   93c64:	8c430000 	lw	v1,0(v0)
			93c64: R_MIPS_LO16	testmode
   93c68:	147500c5 	bne	v1,s5,93f80 <ol_transfer_bin_file+0x7b4>
   93c6c:	3c040000 	lui	a0,0x0
			93c6c: R_MIPS_HI16	$LC20
   93c70:	3c120001 	lui	s2,0x1
			93c70: R_MIPS_HI16	.rodata
   93c74:	3c100000 	lui	s0,0x0
			93c74: R_MIPS_HI16	printk
   93c78:	3c110002 	lui	s1,0x2
   93c7c:	26100000 	addiu	s0,s0,0
			93c7c: R_MIPS_LO16	printk
   93c80:	2645a8a0 	addiu	a1,s2,-22368
			93c80: R_MIPS_LO16	.rodata
   93c84:	24840000 	addiu	a0,a0,0
			93c84: R_MIPS_LO16	$LC20
   93c88:	24060607 	li	a2,1543
   93c8c:	3c020000 	lui	v0,0x0
			93c8c: R_MIPS_HI16	utf_bin
   93c90:	362781e1 	ori	a3,s1,0x81e1
   93c94:	0200f809 	jalr	s0
   93c98:	24530000 	addiu	s3,v0,0
			93c98: R_MIPS_LO16	utf_bin
   93c9c:	3c040000 	lui	a0,0x0
			93c9c: R_MIPS_HI16	$LC21
   93ca0:	2645a8a0 	addiu	a1,s2,-22368
			93ca0: R_MIPS_LO16	.rodata
   93ca4:	24840000 	addiu	a0,a0,0
			93ca4: R_MIPS_LO16	$LC21
   93ca8:	2406060a 	li	a2,1546
   93cac:	0200f809 	jalr	s0
   93cb0:	362781e4 	ori	a3,s1,0x81e4
   93cb4:	3c020000 	lui	v0,0x0
			93cb4: R_MIPS_HI16	amalloc_private
   93cb8:	363281e4 	ori	s2,s1,0x81e4
   93cbc:	00002021 	move	a0,zero
   93cc0:	24540000 	addiu	s4,v0,0
			93cc0: R_MIPS_LO16	amalloc_private
   93cc4:	00003021 	move	a2,zero
   93cc8:	0280f809 	jalr	s4
   93ccc:	02402821 	move	a1,s2
   93cd0:	363081e1 	ori	s0,s1,0x81e1
   93cd4:	08024e40 	j	93900 <ol_transfer_bin_file+0x134>
			93cd4: R_MIPS_26	.text
   93cd8:	00408821 	move	s1,v0
   93cdc:	8ec2361c 	lw	v0,13852(s6)
   93ce0:	10400062 	beqz	v0,93e6c <ol_transfer_bin_file+0x6a0>
   93ce4:	8ec33620 	lw	v1,13856(s6)
   93ce8:	10600060 	beqz	v1,93e6c <ol_transfer_bin_file+0x6a0>
   93cec:	24711000 	addiu	s1,v1,4096
   93cf0:	94641000 	lhu	a0,4096(v1)
   93cf4:	7c0410a0 	wsbh	v0,a0
   93cf8:	3046ffff 	andi	a2,v0,0xffff
   93cfc:	24020844 	li	v0,2116
   93d00:	14c200cf 	bne	a2,v0,94040 <ol_transfer_bin_file+0x874>
   93d04:	24651842 	addiu	a1,v1,6210
   93d08:	00003821 	move	a3,zero
   93d0c:	08024f47 	j	93d1c <ol_transfer_bin_file+0x550>
			93d0c: R_MIPS_26	.text
   93d10:	02201821 	move	v1,s1
   93d14:	24630002 	addiu	v1,v1,2
   93d18:	94640000 	lhu	a0,0(v1)
   93d1c:	7c0410a0 	wsbh	v0,a0
   93d20:	3042ffff 	andi	v0,v0,0xffff
   93d24:	1465fffb 	bne	v1,a1,93d14 <ol_transfer_bin_file+0x548>
   93d28:	00e23826 	xor	a3,a3,v0
   93d2c:	3402ffff 	li	v0,0xffff
   93d30:	10e200ae 	beq	a3,v0,93fec <ol_transfer_bin_file+0x820>
   93d34:	3c040000 	lui	a0,0x0
			93d34: R_MIPS_HI16	$LC24
   93d38:	96260002 	lhu	a2,2(s1)
   93d3c:	3c050001 	lui	a1,0x1
			93d3c: R_MIPS_HI16	.rodata
   93d40:	3c030000 	lui	v1,0x0
			93d40: R_MIPS_HI16	printk
   93d44:	00073827 	nor	a3,zero,a3
   93d48:	24840000 	addiu	a0,a0,0
			93d48: R_MIPS_LO16	$LC24
   93d4c:	24a5a8b8 	addiu	a1,a1,-22344
			93d4c: R_MIPS_LO16	.rodata
   93d50:	24630000 	addiu	v1,v1,0
			93d50: R_MIPS_LO16	printk
   93d54:	7c0630a0 	wsbh	a2,a2
   93d58:	30e7ffff 	andi	a3,a3,0xffff
   93d5c:	0060f809 	jalr	v1
   93d60:	30c6ffff 	andi	a2,a2,0xffff
   93d64:	2410ffea 	li	s0,-22
   93d68:	8fbf0044 	lw	ra,68(sp)
   93d6c:	02001021 	move	v0,s0
   93d70:	8fbe0040 	lw	s8,64(sp)
   93d74:	8fb7003c 	lw	s7,60(sp)
   93d78:	8fb60038 	lw	s6,56(sp)
   93d7c:	8fb50034 	lw	s5,52(sp)
   93d80:	8fb40030 	lw	s4,48(sp)
   93d84:	8fb3002c 	lw	s3,44(sp)
   93d88:	8fb20028 	lw	s2,40(sp)
   93d8c:	8fb10024 	lw	s1,36(sp)
   93d90:	8fb00020 	lw	s0,32(sp)
   93d94:	03e00008 	jr	ra
   93d98:	27bd0048 	addiu	sp,sp,72
   93d9c:	8c833610 	lw	v1,13840(a0)
   93da0:	34420623 	ori	v0,v0,0x623
   93da4:	1062ff2d 	beq	v1,v0,93a5c <ol_transfer_bin_file+0x290>
   93da8:	24020001 	li	v0,1
   93dac:	3c044000 	lui	a0,0x4000
   93db0:	3482002c 	ori	v0,a0,0x2c
   93db4:	1062ff28 	beq	v1,v0,93a58 <ol_transfer_bin_file+0x28c>
   93db8:	3482270f 	ori	v0,a0,0x270f
   93dbc:	1062ff26 	beq	v1,v0,93a58 <ol_transfer_bin_file+0x28c>
   93dc0:	3c024100 	lui	v0,0x4100
   93dc4:	3442006b 	ori	v0,v0,0x6b
   93dc8:	1062ff24 	beq	v1,v0,93a5c <ol_transfer_bin_file+0x290>
   93dcc:	24020001 	li	v0,1
   93dd0:	3c040000 	lui	a0,0x0
			93dd0: R_MIPS_HI16	$LC10
   93dd4:	08024ec6 	j	93b18 <ol_transfer_bin_file+0x34c>
			93dd4: R_MIPS_26	.text
   93dd8:	24840000 	addiu	a0,a0,0
			93dd8: R_MIPS_LO16	$LC10
   93ddc:	3c020040 	lui	v0,0x40
   93de0:	08024ef8 	j	93be0 <ol_transfer_bin_file+0x414>
			93de0: R_MIPS_26	.text
   93de4:	344508ac 	ori	a1,v0,0x8ac
   93de8:	8ec43654 	lw	a0,13908(s6)
   93dec:	26661c00 	addiu	a2,s3,7168
   93df0:	afb60010 	sw	s6,16(sp)
   93df4:	24520000 	addiu	s2,v0,0
			93df4: R_MIPS_LO16	BMIWriteMemory
   93df8:	0240f809 	jalr	s2
   93dfc:	00003821 	move	a3,zero
   93e00:	1440009a 	bnez	v0,9406c <ol_transfer_bin_file+0x8a0>
   93e04:	24020001 	li	v0,1
   93e08:	8ec5360c 	lw	a1,13836(s6)
   93e0c:	24030002 	li	v1,2
   93e10:	8ec43654 	lw	a0,13908(s6)
   93e14:	10a30044 	beq	a1,v1,93f28 <ol_transfer_bin_file+0x75c>
   93e18:	afa2001c 	sw	v0,28(sp)
   93e1c:	24020003 	li	v0,3
   93e20:	10a2004d 	beq	a1,v0,93f58 <ol_transfer_bin_file+0x78c>
   93e24:	24020005 	li	v0,5
   93e28:	10a2003c 	beq	a1,v0,93f1c <ol_transfer_bin_file+0x750>
   93e2c:	24020006 	li	v0,6
   93e30:	10a2003a 	beq	a1,v0,93f1c <ol_transfer_bin_file+0x750>
   93e34:	24020007 	li	v0,7
   93e38:	10a20038 	beq	a1,v0,93f1c <ol_transfer_bin_file+0x750>
   93e3c:	24020008 	li	v0,8
   93e40:	10a20036 	beq	a1,v0,93f1c <ol_transfer_bin_file+0x750>
   93e44:	24020009 	li	v0,9
   93e48:	10a20035 	beq	a1,v0,93f20 <ol_transfer_bin_file+0x754>
   93e4c:	3c020040 	lui	v0,0x40
   93e50:	00002821 	move	a1,zero
   93e54:	27a6001c 	addiu	a2,sp,28
   93e58:	afb60010 	sw	s6,16(sp)
   93e5c:	0240f809 	jalr	s2
   93e60:	24070004 	li	a3,4
   93e64:	08024e68 	j	939a0 <ol_transfer_bin_file+0x1d4>
			93e64: R_MIPS_26	.text
   93e68:	24061c00 	li	a2,7168
   93e6c:	3c040000 	lui	a0,0x0
			93e6c: R_MIPS_HI16	$LC22
   93e70:	3c050001 	lui	a1,0x1
			93e70: R_MIPS_HI16	.rodata
   93e74:	3c030000 	lui	v1,0x0
			93e74: R_MIPS_HI16	printk
   93e78:	24840000 	addiu	a0,a0,0
			93e78: R_MIPS_LO16	$LC22
   93e7c:	24a5a8a0 	addiu	a1,a1,-22368
			93e7c: R_MIPS_LO16	.rodata
   93e80:	24630000 	addiu	v1,v1,0
			93e80: R_MIPS_LO16	printk
   93e84:	0060f809 	jalr	v1
   93e88:	2410ffea 	li	s0,-22
   93e8c:	08024e0d 	j	93834 <ol_transfer_bin_file+0x68>
			93e8c: R_MIPS_26	.text
   93e90:	8fbf0044 	lw	ra,68(sp)
   93e94:	3c020050 	lui	v0,0x50
   93e98:	08024ef8 	j	93be0 <ol_transfer_bin_file+0x414>
			93e98: R_MIPS_26	.text
   93e9c:	344504ac 	ori	a1,v0,0x4ac
   93ea0:	8c833610 	lw	v1,13840(a0)
   93ea4:	34420623 	ori	v0,v0,0x623
   93ea8:	1062fee9 	beq	v1,v0,93a50 <ol_transfer_bin_file+0x284>
   93eac:	24020003 	li	v0,3
   93eb0:	3c044000 	lui	a0,0x4000
   93eb4:	3482002c 	ori	v0,a0,0x2c
   93eb8:	1062fee4 	beq	v1,v0,93a4c <ol_transfer_bin_file+0x280>
   93ebc:	3482270f 	ori	v0,a0,0x270f
   93ec0:	1062fee2 	beq	v1,v0,93a4c <ol_transfer_bin_file+0x280>
   93ec4:	3c024100 	lui	v0,0x4100
   93ec8:	3442006b 	ori	v0,v0,0x6b
   93ecc:	1062fee0 	beq	v1,v0,93a50 <ol_transfer_bin_file+0x284>
   93ed0:	24020003 	li	v0,3
   93ed4:	08024f75 	j	93dd4 <ol_transfer_bin_file+0x608>
			93ed4: R_MIPS_26	.text
   93ed8:	3c040000 	lui	a0,0x0
			93ed8: R_MIPS_HI16	$LC10
   93edc:	3c020054 	lui	v0,0x54
   93ee0:	08024ef8 	j	93be0 <ol_transfer_bin_file+0x414>
			93ee0: R_MIPS_26	.text
   93ee4:	344506ac 	ori	a1,v0,0x6ac
   93ee8:	3c050001 	lui	a1,0x1
			93ee8: R_MIPS_HI16	.rodata
   93eec:	3c030000 	lui	v1,0x0
			93eec: R_MIPS_HI16	printk
   93ef0:	3c020000 	lui	v0,0x0
			93ef0: R_MIPS_HI16	raw_Data
   93ef4:	24840000 	addiu	a0,a0,0
			93ef4: R_MIPS_LO16	$LC19
   93ef8:	24a5a8a0 	addiu	a1,a1,-22368
			93ef8: R_MIPS_LO16	.rodata
   93efc:	240605ff 	li	a2,1535
   93f00:	24070844 	li	a3,2116
   93f04:	24630000 	addiu	v1,v1,0
			93f04: R_MIPS_LO16	printk
   93f08:	24530000 	addiu	s3,v0,0
			93f08: R_MIPS_LO16	raw_Data
   93f0c:	0060f809 	jalr	v1
   93f10:	24100844 	li	s0,2116
   93f14:	08024e39 	j	938e4 <ol_transfer_bin_file+0x118>
			93f14: R_MIPS_26	.text
   93f18:	24120844 	li	s2,2116
   93f1c:	3c020040 	lui	v0,0x40
   93f20:	08024f95 	j	93e54 <ol_transfer_bin_file+0x688>
			93f20: R_MIPS_26	.text
   93f24:	344508b0 	ori	a1,v0,0x8b0
   93f28:	3c020050 	lui	v0,0x50
   93f2c:	08024f95 	j	93e54 <ol_transfer_bin_file+0x688>
			93f2c: R_MIPS_26	.text
   93f30:	344504b0 	ori	a1,v0,0x4b0
   93f34:	3c040000 	lui	a0,0x0
			93f34: R_MIPS_HI16	$LC12
   93f38:	24840000 	addiu	a0,a0,0
			93f38: R_MIPS_LO16	$LC12
   93f3c:	3c050001 	lui	a1,0x1
			93f3c: R_MIPS_HI16	.rodata
   93f40:	3c030000 	lui	v1,0x0
			93f40: R_MIPS_HI16	printk
   93f44:	24630000 	addiu	v1,v1,0
			93f44: R_MIPS_LO16	printk
   93f48:	0060f809 	jalr	v1
   93f4c:	24a5a8a0 	addiu	a1,a1,-22368
			93f4c: R_MIPS_LO16	.rodata
   93f50:	08024e94 	j	93a50 <ol_transfer_bin_file+0x284>
			93f50: R_MIPS_26	.text
   93f54:	24020003 	li	v0,3
   93f58:	3c020054 	lui	v0,0x54
   93f5c:	08024f95 	j	93e54 <ol_transfer_bin_file+0x688>
			93f5c: R_MIPS_26	.text
   93f60:	344506b0 	ori	a1,v0,0x6b0
   93f64:	3c040000 	lui	a0,0x0
			93f64: R_MIPS_HI16	$LC16
   93f68:	08024ec6 	j	93b18 <ol_transfer_bin_file+0x34c>
			93f68: R_MIPS_26	.text
   93f6c:	24840000 	addiu	a0,a0,0
			93f6c: R_MIPS_LO16	$LC16
   93f70:	08024fcf 	j	93f3c <ol_transfer_bin_file+0x770>
			93f70: R_MIPS_26	.text
   93f74:	24840000 	addiu	a0,a0,0
			93f74: R_MIPS_LO16	$LC14
   93f78:	08024fcf 	j	93f3c <ol_transfer_bin_file+0x770>
			93f78: R_MIPS_26	.text
   93f7c:	24840000 	addiu	a0,a0,0
			93f7c: R_MIPS_LO16	$LC13
   93f80:	3c040000 	lui	a0,0x0
			93f80: R_MIPS_HI16	$LC21
   93f84:	3c050001 	lui	a1,0x1
			93f84: R_MIPS_HI16	.rodata
   93f88:	3c030000 	lui	v1,0x0
			93f88: R_MIPS_HI16	printk
   93f8c:	3c100002 	lui	s0,0x2
   93f90:	3c020000 	lui	v0,0x0
			93f90: R_MIPS_HI16	athwlan_bin
   93f94:	24840000 	addiu	a0,a0,0
			93f94: R_MIPS_LO16	$LC21
   93f98:	24a5a8a0 	addiu	a1,a1,-22368
			93f98: R_MIPS_LO16	.rodata
   93f9c:	24060611 	li	a2,1553
   93fa0:	24630000 	addiu	v1,v1,0
			93fa0: R_MIPS_LO16	printk
   93fa4:	3607d700 	ori	a3,s0,0xd700
   93fa8:	0060f809 	jalr	v1
   93fac:	24530000 	addiu	s3,v0,0
			93fac: R_MIPS_LO16	athwlan_bin
   93fb0:	3612d700 	ori	s2,s0,0xd700
   93fb4:	08024e39 	j	938e4 <ol_transfer_bin_file+0x118>
			93fb4: R_MIPS_26	.text
   93fb8:	3610d6fd 	ori	s0,s0,0xd6fd
   93fbc:	3c040000 	lui	a0,0x0
			93fbc: R_MIPS_HI16	$LC1
   93fc0:	08024e06 	j	93818 <ol_transfer_bin_file+0x4c>
			93fc0: R_MIPS_26	.text
   93fc4:	24840000 	addiu	a0,a0,0
			93fc4: R_MIPS_LO16	$LC1
   93fc8:	3c050001 	lui	a1,0x1
			93fc8: R_MIPS_HI16	.rodata
   93fcc:	3c030000 	lui	v1,0x0
			93fcc: R_MIPS_HI16	printk
   93fd0:	24840000 	addiu	a0,a0,0
			93fd0: R_MIPS_LO16	$LC9
   93fd4:	24a5a8a0 	addiu	a1,a1,-22368
			93fd4: R_MIPS_LO16	.rodata
   93fd8:	24630000 	addiu	v1,v1,0
			93fd8: R_MIPS_LO16	printk
   93fdc:	0060f809 	jalr	v1
   93fe0:	2410fffe 	li	s0,-2
   93fe4:	08024e0d 	j	93834 <ol_transfer_bin_file+0x68>
			93fe4: R_MIPS_26	.text
   93fe8:	8fbf0044 	lw	ra,68(sp)
   93fec:	3c040000 	lui	a0,0x0
			93fec: R_MIPS_HI16	$LC25
   93ff0:	96260002 	lhu	a2,2(s1)
   93ff4:	3c050001 	lui	a1,0x1
			93ff4: R_MIPS_HI16	.rodata
   93ff8:	3c100000 	lui	s0,0x0
			93ff8: R_MIPS_HI16	printk
   93ffc:	24840000 	addiu	a0,a0,0
			93ffc: R_MIPS_LO16	$LC25
