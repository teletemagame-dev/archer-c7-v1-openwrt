import os
import struct
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXTRACTED_DIR = PROJECT_ROOT / "extracted"
FW_OUT_DIR = PROJECT_ROOT / "files" / "lib" / "firmware" / "ath10k" / "QCA988X" / "hw1.0"

ATH10K_FW_MAGIC = b"QCA-ATH10K\x00\x00"
ATH10K_FW_IE_FW_VERSION = 0
ATH10K_FW_IE_TIMESTAMP = 1
ATH10K_FW_IE_FEATURES = 2
ATH10K_FW_IE_FW_IMAGE = 3
ATH10K_FW_IE_OTP_IMAGE = 4
ATH10K_FW_IE_WMI_OP_VERSION = 5


def parse_ath10k_ie_container(data: bytes) -> dict[int, bytes]:
    """Parse a QCA-ATH10K firmware-N.bin IE container."""
    assert data.startswith(ATH10K_FW_MAGIC), "Invalid QCA-ATH10K magic header"
    offset = len(ATH10K_FW_MAGIC)
    ies: dict[int, bytes] = {}
    while offset + 8 <= len(data):
        ie_id, ie_len = struct.unpack("<II", data[offset : offset + 8])
        offset += 8
        assert offset + ie_len <= len(data), f"Truncated IE {ie_id}"
        ies[ie_id] = data[offset : offset + ie_len]
        offset += ie_len
        # 4-byte alignment padding
        rem = ie_len % 4
        if rem:
            offset += 4 - rem
    return ies


def test_extracted_blobs_exist_and_match_c7v1_specs():
    """Verify raw blobs extracted from TP-Link Archer C7 v1 umac.ko."""
    fw_bin = EXTRACTED_DIR / "firmware.bin"
    otp_bin = EXTRACTED_DIR / "otp.bin"
    board_bin = EXTRACTED_DIR / "board.bin"

    assert fw_bin.is_file(), f"Missing {fw_bin}"
    assert otp_bin.is_file(), f"Missing {otp_bin}"
    assert board_bin.is_file(), f"Missing {board_bin}"

    # Verify exact sizes from Archer C7 v1 ol_ath_attach boot log:
    # Download Board data len 2116, OTP data len 3572, Firmware data len 183920
    assert board_bin.stat().st_size == 2116, f"Expected board.bin=2116B, got {board_bin.stat().st_size}"
    assert otp_bin.stat().st_size >= 3000, f"Unexpected otp.bin size: {otp_bin.stat().st_size}"
    assert fw_bin.stat().st_size >= 150000, f"Unexpected firmware.bin size: {fw_bin.stat().st_size}"


def test_firmware_2_bin_ie_container_structure():
    """Verify generated firmware-2.bin for ath10k QCA988X hw1.0."""
    fw2_path = FW_OUT_DIR / "firmware-2.bin"
    board_path = FW_OUT_DIR / "board.bin"

    assert fw2_path.is_file(), f"Missing {fw2_path}"
    assert board_path.is_file(), f"Missing {board_path}"
    assert board_path.stat().st_size == 2116

    data = fw2_path.read_bytes()
    ies = parse_ath10k_ie_container(data)

    assert ATH10K_FW_IE_FW_VERSION in ies, "Missing FW_VERSION IE"
    assert ATH10K_FW_IE_WMI_OP_VERSION in ies, "Missing WMI_OP_VERSION IE"
    assert ATH10K_FW_IE_FW_IMAGE in ies, "Missing FW_IMAGE IE"
    assert ATH10K_FW_IE_OTP_IMAGE in ies, "Missing OTP_IMAGE IE"

    # WMI_OP_VERSION must be 2 (ATH10K_FW_WMI_OP_VERSION_10_1) so ath10k uses wmi_10x (0x8000 = 32768)
    (wmi_op_ver,) = struct.unpack("<I", ies[ATH10K_FW_IE_WMI_OP_VERSION])
    assert wmi_op_ver == 2, f"Expected ATH10K_FW_WMI_OP_VERSION_10_1 (2), got {wmi_op_ver}"

    assert ies[ATH10K_FW_IE_FW_IMAGE] == (EXTRACTED_DIR / "firmware.bin").read_bytes()
    assert ies[ATH10K_FW_IE_OTP_IMAGE] == (EXTRACTED_DIR / "otp.bin").read_bytes()
