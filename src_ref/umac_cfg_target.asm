
/workspace/archer-c7-v1-openwrt/downloads/150511/umac.ko:     file format elf32-tradbigmips


Disassembly of section .text:

00085700 <ol_ath_detach+0x170>:
   85700:	24420000 	addiu	v0,v0,0
			85700: R_MIPS_LO16	ol_txrx_pdev_detach
   85704:	0040f809 	jalr	v0
   85708:	02402821 	move	a1,s2
   8570c:	0802158c 	j	85630 <ol_ath_detach+0xa0>
			8570c: R_MIPS_26	.text
   85710:	ae003668 	sw	zero,13928(s0)
   85714:	24420000 	addiu	v0,v0,0
			85714: R_MIPS_LO16	ieee80211_stop_running
   85718:	0040f809 	jalr	v0
   8571c:	02002021 	move	a0,s0
   85720:	3c020000 	lui	v0,0x0
			85720: R_MIPS_HI16	ol_if_dfs_teardown
   85724:	24420000 	addiu	v0,v0,0
			85724: R_MIPS_LO16	ol_if_dfs_teardown
   85728:	0040f809 	jalr	v0
   8572c:	02002021 	move	a0,s0
   85730:	3c020000 	lui	v0,0x0
			85730: R_MIPS_HI16	ol_ath_phyerr_detach
   85734:	24420000 	addiu	v0,v0,0
			85734: R_MIPS_LO16	ol_ath_phyerr_detach
   85738:	0040f809 	jalr	v0
   8573c:	02002021 	move	a0,s0
   85740:	3c020000 	lui	v0,0x0
			85740: R_MIPS_HI16	ieee80211_ifdetach
   85744:	24420000 	addiu	v0,v0,0
			85744: R_MIPS_LO16	ieee80211_ifdetach
   85748:	0040f809 	jalr	v0
   8574c:	02002021 	move	a0,s0
   85750:	08021573 	j	855cc <ol_ath_detach+0x3c>
			85750: R_MIPS_26	.text
   85754:	8e0235d8 	lw	v0,13784(s0)

00085758 <ol_ath_connect_htc>:
   85758:	27bdff90 	addiu	sp,sp,-112
   8575c:	3c030000 	lui	v1,0x0
			8575c: R_MIPS_HI16	memset
   85760:	00002821 	move	a1,zero
   85764:	afb20064 	sw	s2,100(sp)
   85768:	3c120000 	lui	s2,0x0
			85768: R_MIPS_HI16	bypasswmi
   8576c:	afb10060 	sw	s1,96(sp)
   85770:	24060044 	li	a2,68
   85774:	00808821 	move	s1,a0
   85778:	afbf006c 	sw	ra,108(sp)
   8577c:	27a40010 	addiu	a0,sp,16
   85780:	afb30068 	sw	s3,104(sp)
   85784:	24630000 	addiu	v1,v1,0
			85784: R_MIPS_LO16	memset
   85788:	0060f809 	jalr	v1
   8578c:	afb0005c 	sw	s0,92(sp)
   85790:	8e440000 	lw	a0,0(s2)
			85790: R_MIPS_LO16	bypasswmi
   85794:	afa00014 	sw	zero,20(sp)
   85798:	a3a00018 	sb	zero,24(sp)
   8579c:	afb1001c 	sw	s1,28(sp)
   857a0:	afa00038 	sw	zero,56(sp)
   857a4:	afa00024 	sw	zero,36(sp)
   857a8:	afa00028 	sw	zero,40(sp)
   857ac:	14800010 	bnez	a0,857f0 <ol_ath_connect_htc+0x98>
   857b0:	afa0002c 	sw	zero,44(sp)
   857b4:	3c030000 	lui	v1,0x0
			857b4: R_MIPS_HI16	wmi_unified_connect_htc_service
   857b8:	8e243664 	lw	a0,13924(s1)
   857bc:	24630000 	addiu	v1,v1,0
			857bc: R_MIPS_LO16	wmi_unified_connect_htc_service
   857c0:	0060f809 	jalr	v1
   857c4:	8e253660 	lw	a1,13920(s1)
   857c8:	10400009 	beqz	v0,857f0 <ol_ath_connect_htc+0x98>
   857cc:	00408021 	move	s0,v0
   857d0:	8fbf006c 	lw	ra,108(sp)
   857d4:	02001021 	move	v0,s0
   857d8:	8fb30068 	lw	s3,104(sp)
   857dc:	8fb20064 	lw	s2,100(sp)
   857e0:	8fb10060 	lw	s1,96(sp)
   857e4:	8fb0005c 	lw	s0,92(sp)
   857e8:	03e00008 	jr	ra
   857ec:	27bd0070 	addiu	sp,sp,112
   857f0:	3c020000 	lui	v0,0x0
			857f0: R_MIPS_HI16	ol_cookie_init
   857f4:	24420000 	addiu	v0,v0,0
			857f4: R_MIPS_LO16	ol_cookie_init
   857f8:	0040f809 	jalr	v0
   857fc:	02202021 	move	a0,s1
   85800:	3c030000 	lui	v1,0x0
			85800: R_MIPS_HI16	HTCStart
   85804:	24630000 	addiu	v1,v1,0
			85804: R_MIPS_LO16	HTCStart
   85808:	0060f809 	jalr	v1
   8580c:	8e243660 	lw	a0,13920(s1)
   85810:	1440ffef 	bnez	v0,857d0 <ol_ath_connect_htc+0x78>
   85814:	00408021 	move	s0,v0
   85818:	8e420000 	lw	v0,0(s2)
			85818: R_MIPS_LO16	bypasswmi
   8581c:	1440ffed 	bnez	v0,857d4 <ol_ath_connect_htc+0x7c>
   85820:	8fbf006c 	lw	ra,108(sp)
   85824:	3c030000 	lui	v1,0x0
			85824: R_MIPS_HI16	__ol_ath_check_wmi_ready
   85828:	24630000 	addiu	v1,v1,0
			85828: R_MIPS_LO16	__ol_ath_check_wmi_ready
   8582c:	0060f809 	jalr	v1
   85830:	02202021 	move	a0,s1
   85834:	1040000d 	beqz	v0,8586c <ol_ath_connect_htc+0x114>
   85838:	00408021 	move	s0,v0
   8583c:	3c020000 	lui	v0,0x0
			8583c: R_MIPS_HI16	HTCStop
   85840:	24420000 	addiu	v0,v0,0
			85840: R_MIPS_LO16	HTCStop
   85844:	0040f809 	jalr	v0
   85848:	8e243660 	lw	a0,13920(s1)
   8584c:	02001021 	move	v0,s0
   85850:	8fbf006c 	lw	ra,108(sp)
   85854:	8fb30068 	lw	s3,104(sp)
   85858:	8fb20064 	lw	s2,100(sp)
   8585c:	8fb10060 	lw	s1,96(sp)
   85860:	8fb0005c 	lw	s0,92(sp)
   85864:	03e00008 	jr	ra
   85868:	27bd0070 	addiu	sp,sp,112
   8586c:	3c020000 	lui	v0,0x0
			8586c: R_MIPS_HI16	printk
   85870:	3c130001 	lui	s3,0x1
			85870: R_MIPS_HI16	.rodata
   85874:	3c040000 	lui	a0,0x0
			85874: R_MIPS_HI16	$LC31
   85878:	24520000 	addiu	s2,v0,0
			85878: R_MIPS_LO16	printk
   8587c:	24840000 	addiu	a0,a0,0
			8587c: R_MIPS_LO16	$LC31
   85880:	0240f809 	jalr	s2
   85884:	26659934 	addiu	a1,s3,-26316
			85884: R_MIPS_LO16	.rodata
   85888:	8e263628 	lw	a2,13864(s1)
   8588c:	10c00008 	beqz	a2,858b0 <ol_ath_connect_htc+0x158>
   85890:	3c040000 	lui	a0,0x0
			85890: R_MIPS_HI16	$LC15
   85894:	3c040000 	lui	a0,0x0
			85894: R_MIPS_HI16	$LC32
   85898:	26659934 	addiu	a1,s3,-26316
			85898: R_MIPS_LO16	.rodata
   8589c:	24840000 	addiu	a0,a0,0
			8589c: R_MIPS_LO16	$LC32
   858a0:	0240f809 	jalr	s2
   858a4:	24100013 	li	s0,19
   858a8:	08021610 	j	85840 <ol_ath_connect_htc+0xe8>
			858a8: R_MIPS_26	.text
   858ac:	3c020000 	lui	v0,0x0
			858ac: R_MIPS_HI16	HTCStop
   858b0:	0240f809 	jalr	s2
   858b4:	24840000 	addiu	a0,a0,0
			858b4: R_MIPS_LO16	$LC15
   858b8:	080215f5 	j	857d4 <ol_ath_connect_htc+0x7c>
			858b8: R_MIPS_26	.text
   858bc:	8fbf006c 	lw	ra,108(sp)

000858c0 <ol_ath_configure_target>:
   858c0:	27bdffc8 	addiu	sp,sp,-56
   858c4:	24020002 	li	v0,2
   858c8:	24030003 	li	v1,3
   858cc:	afb00024 	sw	s0,36(sp)
   858d0:	00808021 	move	s0,a0
   858d4:	afbf0034 	sw	ra,52(sp)
   858d8:	afb30030 	sw	s3,48(sp)
   858dc:	afb2002c 	sw	s2,44(sp)
   858e0:	afb10028 	sw	s1,40(sp)
   858e4:	8c85360c 	lw	a1,13836(a0)
   858e8:	8c843654 	lw	a0,13908(a0)
   858ec:	10a30038 	beq	a1,v1,859d0 <ol_ath_configure_target+0x110>
   858f0:	afa20018 	sw	v0,24(sp)
   858f4:	2ca20003 	sltiu	v0,a1,3
   858f8:	10400004 	beqz	v0,8590c <ol_ath_configure_target+0x4c>
   858fc:	24a2fffb 	addiu	v0,a1,-5
   85900:	3c020050 	lui	v0,0x50
   85904:	08021648 	j	85920 <ol_ath_configure_target+0x60>
			85904: R_MIPS_26	.text
   85908:	34450400 	ori	a1,v0,0x400
   8590c:	2c420004 	sltiu	v0,v0,4
   85910:	1040fffc 	beqz	v0,85904 <ol_ath_configure_target+0x44>
   85914:	3c020050 	lui	v0,0x50
   85918:	3c020040 	lui	v0,0x40
   8591c:	34450800 	ori	a1,v0,0x800
   85920:	3c020000 	lui	v0,0x0
			85920: R_MIPS_HI16	BMIWriteMemory
   85924:	afb00010 	sw	s0,16(sp)
   85928:	27b10018 	addiu	s1,sp,24
   8592c:	24520000 	addiu	s2,v0,0
			8592c: R_MIPS_LO16	BMIWriteMemory
   85930:	24070004 	li	a3,4
   85934:	0240f809 	jalr	s2
   85938:	02203021 	move	a2,s1
   8593c:	1440002a 	bnez	v0,859e8 <ol_ath_configure_target+0x128>
   85940:	3c040000 	lui	a0,0x0
			85940: R_MIPS_HI16	$LC33
   85944:	8e03360c 	lw	v1,13836(s0)
   85948:	24020003 	li	v0,3
   8594c:	10620023 	beq	v1,v0,859dc <ol_ath_configure_target+0x11c>
   85950:	8e043654 	lw	a0,13908(s0)
   85954:	2c620003 	sltiu	v0,v1,3
   85958:	10400004 	beqz	v0,8596c <ol_ath_configure_target+0xac>
   8595c:	2462fffb 	addiu	v0,v1,-5
   85960:	3c020050 	lui	v0,0x50
   85964:	08021660 	j	85980 <ol_ath_configure_target+0xc0>
			85964: R_MIPS_26	.text
   85968:	34450410 	ori	a1,v0,0x410
   8596c:	2c420004 	sltiu	v0,v0,4
   85970:	1040fffc 	beqz	v0,85964 <ol_ath_configure_target+0xa4>
   85974:	3c020050 	lui	v0,0x50
   85978:	3c020040 	lui	v0,0x40
   8597c:	34450810 	ori	a1,v0,0x810
   85980:	3c030000 	lui	v1,0x0
			85980: R_MIPS_HI16	BMIReadMemory
   85984:	afb00010 	sw	s0,16(sp)
   85988:	24070004 	li	a3,4
   8598c:	24630000 	addiu	v1,v1,0
			8598c: R_MIPS_LO16	BMIReadMemory
   85990:	0060f809 	jalr	v1
   85994:	02203021 	move	a2,s1
   85998:	10400019 	beqz	v0,85a00 <ol_ath_configure_target+0x140>
   8599c:	3c030000 	lui	v1,0x0
			8599c: R_MIPS_HI16	printk
   859a0:	3c040000 	lui	a0,0x0
			859a0: R_MIPS_HI16	$LC34
   859a4:	24630000 	addiu	v1,v1,0
			859a4: R_MIPS_LO16	printk
   859a8:	0060f809 	jalr	v1
   859ac:	24840000 	addiu	a0,a0,0
			859ac: R_MIPS_LO16	$LC34
   859b0:	2402ffff 	li	v0,-1
   859b4:	8fbf0034 	lw	ra,52(sp)
   859b8:	8fb30030 	lw	s3,48(sp)
   859bc:	8fb2002c 	lw	s2,44(sp)
   859c0:	8fb10028 	lw	s1,40(sp)
   859c4:	8fb00024 	lw	s0,36(sp)
   859c8:	03e00008 	jr	ra
   859cc:	27bd0038 	addiu	sp,sp,56
   859d0:	3c020054 	lui	v0,0x54
   859d4:	08021648 	j	85920 <ol_ath_configure_target+0x60>
			859d4: R_MIPS_26	.text
   859d8:	34450600 	ori	a1,v0,0x600
   859dc:	3c020054 	lui	v0,0x54
   859e0:	08021660 	j	85980 <ol_ath_configure_target+0xc0>
			859e0: R_MIPS_26	.text
   859e4:	34450610 	ori	a1,v0,0x610
   859e8:	3c030000 	lui	v1,0x0
			859e8: R_MIPS_HI16	printk
   859ec:	24630000 	addiu	v1,v1,0
			859ec: R_MIPS_LO16	printk
   859f0:	0060f809 	jalr	v1
   859f4:	24840000 	addiu	a0,a0,0
			859f4: R_MIPS_LO16	$LC33
   859f8:	0802166d 	j	859b4 <ol_ath_configure_target+0xf4>
			859f8: R_MIPS_26	.text
   859fc:	2402ffff 	li	v0,-1
   85a00:	3c020000 	lui	v0,0x0
			85a00: R_MIPS_HI16	printk
   85a04:	afa00010 	sw	zero,16(sp)
   85a08:	3c040000 	lui	a0,0x0
			85a08: R_MIPS_HI16	$LC35
   85a0c:	24530000 	addiu	s3,v0,0
			85a0c: R_MIPS_LO16	printk
   85a10:	8fa20018 	lw	v0,24(sp)
   85a14:	24840000 	addiu	a0,a0,0
			85a14: R_MIPS_LO16	$LC35
   85a18:	24050001 	li	a1,1
   85a1c:	24060002 	li	a2,2
   85a20:	00003821 	move	a3,zero
   85a24:	34422208 	ori	v0,v0,0x2208
   85a28:	0260f809 	jalr	s3
   85a2c:	afa20018 	sw	v0,24(sp)
   85a30:	24020003 	li	v0,3
   85a34:	8e03360c 	lw	v1,13836(s0)
   85a38:	1062002d 	beq	v1,v0,85af0 <ol_ath_configure_target+0x230>
   85a3c:	8e043654 	lw	a0,13908(s0)
   85a40:	2c620003 	sltiu	v0,v1,3
   85a44:	1040001e 	beqz	v0,85ac0 <ol_ath_configure_target+0x200>
   85a48:	2462fffb 	addiu	v0,v1,-5
   85a4c:	3c020050 	lui	v0,0x50
   85a50:	34450410 	ori	a1,v0,0x410
   85a54:	24070004 	li	a3,4
   85a58:	afb00010 	sw	s0,16(sp)
   85a5c:	0240f809 	jalr	s2
   85a60:	02203021 	move	a2,s1
   85a64:	14400028 	bnez	v0,85b08 <ol_ath_configure_target+0x248>
   85a68:	24030003 	li	v1,3
   85a6c:	8e05360c 	lw	a1,13836(s0)
   85a70:	24020001 	li	v0,1
   85a74:	8e043654 	lw	a0,13908(s0)
   85a78:	10a30020 	beq	a1,v1,85afc <ol_ath_configure_target+0x23c>
   85a7c:	afa20018 	sw	v0,24(sp)
   85a80:	2ca20003 	sltiu	v0,a1,3
   85a84:	10400014 	beqz	v0,85ad8 <ol_ath_configure_target+0x218>
   85a88:	24a2fffb 	addiu	v0,a1,-5
   85a8c:	3c020050 	lui	v0,0x50
   85a90:	34450444 	ori	a1,v0,0x444
   85a94:	24070004 	li	a3,4
   85a98:	afb00010 	sw	s0,16(sp)
   85a9c:	0240f809 	jalr	s2
   85aa0:	02203021 	move	a2,s1
   85aa4:	1040ffc4 	beqz	v0,859b8 <ol_ath_configure_target+0xf8>
   85aa8:	8fbf0034 	lw	ra,52(sp)
   85aac:	3c040000 	lui	a0,0x0
			85aac: R_MIPS_HI16	$LC37
   85ab0:	0260f809 	jalr	s3
   85ab4:	24840000 	addiu	a0,a0,0
			85ab4: R_MIPS_LO16	$LC37
   85ab8:	0802166d 	j	859b4 <ol_ath_configure_target+0xf4>
			85ab8: R_MIPS_26	.text
   85abc:	2402ffff 	li	v0,-1
   85ac0:	2c420004 	sltiu	v0,v0,4
   85ac4:	1040ffe2 	beqz	v0,85a50 <ol_ath_configure_target+0x190>
   85ac8:	3c020050 	lui	v0,0x50
   85acc:	3c020040 	lui	v0,0x40
   85ad0:	08021695 	j	85a54 <ol_ath_configure_target+0x194>
			85ad0: R_MIPS_26	.text
   85ad4:	34450810 	ori	a1,v0,0x810
   85ad8:	2c420004 	sltiu	v0,v0,4
   85adc:	1040ffec 	beqz	v0,85a90 <ol_ath_configure_target+0x1d0>
   85ae0:	3c020050 	lui	v0,0x50
   85ae4:	3c020040 	lui	v0,0x40
   85ae8:	080216a5 	j	85a94 <ol_ath_configure_target+0x1d4>
			85ae8: R_MIPS_26	.text
   85aec:	34450844 	ori	a1,v0,0x844
   85af0:	3c020054 	lui	v0,0x54
   85af4:	08021695 	j	85a54 <ol_ath_configure_target+0x194>
			85af4: R_MIPS_26	.text
   85af8:	34450610 	ori	a1,v0,0x610
   85afc:	3c020054 	lui	v0,0x54
   85b00:	080216a5 	j	85a94 <ol_ath_configure_target+0x1d4>
			85b00: R_MIPS_26	.text
   85b04:	34450644 	ori	a1,v0,0x644
   85b08:	3c040000 	lui	a0,0x0
			85b08: R_MIPS_HI16	$LC36
   85b0c:	0260f809 	jalr	s3
   85b10:	24840000 	addiu	a0,a0,0
			85b10: R_MIPS_LO16	$LC36
   85b14:	0802166d 	j	859b4 <ol_ath_configure_target+0xf4>
			85b14: R_MIPS_26	.text
   85b18:	2402ffff 	li	v0,-1
