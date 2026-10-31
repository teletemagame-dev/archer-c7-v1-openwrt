import hashlib
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATCH_FILE = ROOT / "patches" / "999-ath10k-restore-qca988x-hw1.0-support.patch"
OUTPUT_DIR = ROOT / "output"
FACTORY_BIN = OUTPUT_DIR / "openwrt-23.05.5-ath79-generic-tplink_archer-c7-v1-squashfs-factory.bin"
SHORT_FACTORY_BIN = OUTPUT_DIR / "factory.bin"
SYSUPGRADE_BIN = OUTPUT_DIR / "openwrt-23.05.5-ath79-generic-tplink_archer-c7-v1-squashfs-sysupgrade.bin"


def test_patch_structure_and_invariants():
    assert PATCH_FILE.exists(), f"Missing patch file: {PATCH_FILE}"
    raw = PATCH_FILE.read_bytes()
    assert b"\r\n" not in raw, "Patch file must use Unix LF line endings"
    text = raw.decode("utf-8")
    assert "#define QCA988X_HW_1_0_VERSION\t\t0x4000002c" in text
    assert '.name = "qca988x hw1.0"' in text
    assert "CDC_WAR_MAGIC_STR" in text
    assert "ath10k_pci_raw_write32" in text
    assert "hw_v1_workaround" in text
    assert "0x00423900" in text


def test_compiled_ko_modules_have_hw1_0_support():
    ko_core = OUTPUT_DIR / "ath10k_core.ko"
    ko_pci = OUTPUT_DIR / "ath10k_pci.ko"
    assert ko_core.exists(), "Missing compiled ath10k_core.ko in output/"
    assert ko_pci.exists(), "Missing compiled ath10k_pci.ko in output/"

    core_bytes = ko_core.read_bytes()
    pci_bytes = ko_pci.read_bytes()

    assert b"qca988x hw1.0" in core_bytes
    assert b"ath10k/QCA988X/hw1.0" in core_bytes
    # Verify MIPS big-endian instruction 'lui a2, 0xceef' (0x3c06ceef) for CDC_WAR_MAGIC_STR in ath10k_core.ko
    assert b"\x3c\x06\xce\xef" in core_bytes
    # Verify MIPS big-endian instructions 'di s4; andi s4,s4,1; ehb' and 'addiu s3,a1,4' for WAR_PCI_WRITE32 in ath10k_pci.ko
    assert b"\x41\x74\x60\x00\x32\x94\x00\x01\x00\x00\x00\xc0" in pci_bytes
    assert b"\x24\xb3\x00\x04" in pci_bytes


def test_factory_and_sysupgrade_images():
    assert FACTORY_BIN.exists(), f"Missing {FACTORY_BIN}"
    assert SHORT_FACTORY_BIN.exists(), f"Missing {SHORT_FACTORY_BIN}"
    assert SYSUPGRADE_BIN.exists(), f"Missing {SYSUPGRADE_BIN}"

    factory_data = FACTORY_BIN.read_bytes()
    short_factory_data = SHORT_FACTORY_BIN.read_bytes()
    sysupgrade_data = SYSUPGRADE_BIN.read_bytes()

    assert factory_data == short_factory_data, "factory.bin must match full factory image"

    # Must fit in 7936k (8,126,464 bytes) firmware partition
    assert 4_000_000 < len(factory_data) <= 8_126_464
    # Must leave >= 750 KB for JFFS2 overlay
    assert 4_000_000 < len(sysupgrade_data) <= 7_340_032

    # Verify TP-Link Archer C7 v1 hardware ID and revision in factory header
    hdr_ver = struct.unpack(">I", factory_data[0:4])[0]
    hwid = struct.unpack(">I", factory_data[0x40:0x44])[0]
    hwrev = struct.unpack(">I", factory_data[0x44:0x48])[0]
    assert hdr_ver == 0x01000000, f"Unexpected TP-Link header version: {hex(hdr_ver)}"
    assert hwid == 0x75000001, f"Expected Archer C7 v1 HWID 0x75000001, got {hex(hwid)}"
    assert hwrev == 0x00000001, f"Expected HWREV 1, got {hex(hwrev)}"

    # Locate SquashFS superblock ('hsqs') in sysupgrade.bin and verify contents
    hsqs_offset = sysupgrade_data.find(b"hsqs")
    assert hsqs_offset > 0x100000, f"SquashFS magic 'hsqs' not found in sysupgrade.bin"

    # Verify extracted rootfs listing generated during build verification
    manifest_file = OUTPUT_DIR / "squashfs_manifest.txt"
    assert manifest_file.exists(), "Missing squashfs_manifest.txt"
    manifest = manifest_file.read_text(encoding="utf-8")

    required_paths = [
        "lib/firmware/ath10k/QCA988X/hw1.0/firmware-5.bin",
        "lib/firmware/ath10k/QCA988X/hw1.0/firmware-2.bin",
        "lib/firmware/ath10k/QCA988X/hw1.0/board.bin",
        "etc/sysctl.d/99-ath10k-safe.conf",
        "etc/uci-defaults/99-archer-c7-v1-5g",
        "ath10k_core.ko",
        "ath10k_pci.ko",
        "ath9k.ko",
    ]
    for req in required_paths:
        assert req in manifest, f"Missing {req} in SquashFS rootfs manifest"
