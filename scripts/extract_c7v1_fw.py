#!/usr/bin/env python3
"""
Extract QCA9880-AR1A (hw1.0, 0x4000002c) firmware, OTP, and board data blobs
from official TP-Link Archer C7 v1 stock firmware (umac.ko) and package them
into ath10k QCA-ATH10K IE container format (firmware-2.bin + board.bin).
"""

import lzma
import struct
import time
from pathlib import Path
from elftools.elf.elffile import ELFFile

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOWNLOADS_DIR = PROJECT_ROOT / "downloads"
EXTRACTED_DIR = PROJECT_ROOT / "extracted"
FW_OUT_DIR = PROJECT_ROOT / "files" / "lib" / "firmware" / "ath10k" / "QCA988X" / "hw1.0"

ATH10K_FW_MAGIC = b"QCA-ATH10K\x00\x00"
ATH10K_FW_IE_FW_VERSION = 0
ATH10K_FW_IE_TIMESTAMP = 1
ATH10K_FW_IE_FEATURES = 2
ATH10K_FW_IE_FW_IMAGE = 3
ATH10K_FW_IE_OTP_IMAGE = 4
ATH10K_FW_IE_WMI_OP_VERSION = 5
ATH10K_FW_IE_HTT_OP_VERSION = 6

# enum ath10k_fw_wmi_op_version:
# ATH10K_FW_WMI_OP_VERSION_MAIN = 1
# ATH10K_FW_WMI_OP_VERSION_10_1 = 2
ATH10K_FW_WMI_OP_VERSION_10_1 = 2

# enum ath10k_fw_htt_op_version:
# ATH10K_FW_HTT_OP_VERSION_MAIN = 1
# ATH10K_FW_HTT_OP_VERSION_10_1 = 2
ATH10K_FW_HTT_OP_VERSION_10_1 = 2

# enum ath10k_fw_features:
# ATH10K_FW_FEATURE_EXT_WMI_MGMT_RX = 0
# ATH10K_FW_FEATURE_WMI_10X = 1
# ATH10K_FW_FEATURE_HAS_WMI_MGMT_TX = 2
ATH10K_FW_FEATURE_WMI_10X = 1
ATH10K_FW_FEATURE_HAS_WMI_MGMT_TX = 2


def lzma_dec_tplink(data: bytes) -> bytes:
    """Decompress TP-Link / LSDK SquashFS 4.0 5-byte header LZMA chunk."""
    return lzma.decompress(data[:5] + b"\xff" * 8 + data[5:])


def read_meta_block(sq: bytes, pos: int) -> tuple[bytes, int]:
    hdr = struct.unpack("<H", sq[pos : pos + 2])[0]
    sz = hdr & 0x7FFF
    uncomp = bool(hdr & 0x8000)
    raw = sq[pos + 2 : pos + 2 + sz]
    return (raw if uncomp else lzma_dec_tplink(raw)), pos + 2 + sz


def extract_file_from_tplink_squashfs(sq: bytes, target_name: bytes) -> bytes:
    sb = struct.unpack("<IIIIIHHHHHHQQQQQQQQ", sq[:96])
    (
        magic,
        inodes,
        mkfs_time,
        block_size,
        fragments,
        comp,
        block_log,
        flags,
        no_ids,
        maj,
        min_,
        root_inode,
        bytes_used,
        id_start,
        xattr_start,
        inode_start,
        dir_start,
        frag_start,
        export_start,
    ) = sb
    assert magic == 0x73717368, f"Invalid SquashFS magic: {hex(magic)}"

    frag_blocks = (fragments + 511) // 512
    frag_ptrs = struct.unpack(f"<{frag_blocks}Q", sq[frag_start : frag_start + 8 * frag_blocks])
    frag_buf = b""
    for fp in frag_ptrs:
        b, _ = read_meta_block(sq, fp)
        frag_buf += b
    frag_entries = [struct.unpack("<QII", frag_buf[i * 16 : (i + 1) * 16]) for i in range(fragments)]

    inode_blocks: dict[int, tuple[bytes, int]] = {}
    pos = inode_start
    while pos < dir_start:
        rel = pos - inode_start
        b, next_pos = read_meta_block(sq, pos)
        inode_blocks[rel] = (b, next_pos - inode_start)
        pos = next_pos

    def read_inode_bytes(block_rel: int, off: int, length: int) -> bytes:
        res = bytearray()
        cur_rel = block_rel
        cur_off = off
        while len(res) < length:
            b, next_rel = inode_blocks[cur_rel]
            take = min(length - len(res), len(b) - cur_off)
            res.extend(b[cur_off : cur_off + take])
            cur_rel = next_rel
            cur_off = 0
        return bytes(res)

    dir_buf = b""
    pos = dir_start
    while pos < frag_start:
        b, pos = read_meta_block(sq, pos)
        dir_buf += b

    idx = dir_buf.find(target_name)
    if idx == -1:
        raise FileNotFoundError(f"{target_name!r} not found in SquashFS")
    ent_off, ino_off, ent_type, name_sz = struct.unpack("<HhHH", dir_buf[idx - 8 : idx])

    for blk_rel in inode_blocks:
        if ent_off + 32 <= len(inode_blocks[blk_rel][0]):
            ihdr = read_inode_bytes(blk_rel, ent_off, 32)
            itype, mode, uid, guid, mtime, ino, start_block, fragment, offset, file_size = struct.unpack(
                "<HHHHIIIIII", ihdr
            )
            if itype == 2 and 100000 < file_size < 10000000:
                nblocks = (
                    (file_size // block_size)
                    if fragment != 0xFFFFFFFF
                    else ((file_size + block_size - 1) // block_size)
                )
                raw_inode = read_inode_bytes(blk_rel, ent_off, 32 + 4 * nblocks)
                blist = struct.unpack(f"<{nblocks}I", raw_inode[32:])
                fbytes = bytearray()
                cur = start_block
                for b_entry in blist:
                    bsz = b_entry & 0xFFFFFF
                    uncomp = bool(b_entry & (1 << 24))
                    chunk = sq[cur : cur + bsz]
                    fbytes.extend(chunk if uncomp else lzma_dec_tplink(chunk))
                    cur += bsz
                if fragment != 0xFFFFFFFF:
                    fstart, fsz, _ = frag_entries[fragment]
                    funcomp = bool(fsz & (1 << 24))
                    fsz &= 0xFFFFFF
                    fchunk = sq[fstart : fstart + fsz]
                    fdec = fchunk if funcomp else lzma_dec_tplink(fchunk)
                    fbytes.extend(fdec[offset : offset + (file_size % block_size)])
                if fbytes[:4] == b"\x7fELF":
                    return bytes(fbytes)
    raise RuntimeError(f"Failed to reconstruct inode for {target_name!r}")


def inspect_and_extract_umac_blobs(umac_path: Path) -> dict[str, bytes]:
    blobs: dict[str, bytes] = {}
    with open(umac_path, "rb") as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name(".symtab")
        for sym in symtab.iter_symbols():
            name = sym.name
            sz = sym["st_size"]
            val = sym["st_value"]
            shndx = sym["st_shndx"]
            if sz > 0 and isinstance(shndx, int) and shndx < elf.num_sections():
                sec = elf.get_section(shndx)
                if any(k in name.lower() for k in ["bin", "otp", "raw", "board", "988", "athwlan", "fw"]):
                    print(f"  Symbol: {name:35s} offset={hex(val):10s} size={sz:8d} section={sec.name}")
                    sec_data = sec.data()
                    blobs[name] = sec_data[val : val + sz]
    return blobs


def pack_ie(ie_id: int, payload: bytes) -> bytes:
    hdr = struct.pack("<II", ie_id, len(payload))
    rem = len(payload) % 4
    pad = b"\x00" * (4 - rem) if rem else b""
    return hdr + payload + pad


def build_firmware_2_bin(fw_bytes: bytes, otp_bytes: bytes, fw_ver_str: str = "10.1.389-qca988x-hw1.0") -> bytes:
    ver_bytes = fw_ver_str.encode("ascii") + b"\x00"
    ts_bytes = struct.pack("<I", int(time.time()))
    # Feature bits: bit 1 (ATH10K_FW_FEATURE_WMI_10X) | bit 2 (ATH10K_FW_FEATURE_HAS_WMI_MGMT_TX)
    feat_mask = (1 << ATH10K_FW_FEATURE_WMI_10X) | (1 << ATH10K_FW_FEATURE_HAS_WMI_MGMT_TX)
    feat_bytes = struct.pack("<B", feat_mask)
    wmi_op_bytes = struct.pack("<I", ATH10K_FW_WMI_OP_VERSION_10_1)
    htt_op_bytes = struct.pack("<I", ATH10K_FW_HTT_OP_VERSION_10_1)

    container = bytearray(ATH10K_FW_MAGIC)
    container.extend(pack_ie(ATH10K_FW_IE_FW_VERSION, ver_bytes))
    container.extend(pack_ie(ATH10K_FW_IE_TIMESTAMP, ts_bytes))
    container.extend(pack_ie(ATH10K_FW_IE_FEATURES, feat_bytes))
    container.extend(pack_ie(ATH10K_FW_IE_WMI_OP_VERSION, wmi_op_bytes))
    container.extend(pack_ie(ATH10K_FW_IE_HTT_OP_VERSION, htt_op_bytes))
    container.extend(pack_ie(ATH10K_FW_IE_FW_IMAGE, fw_bytes))
    container.extend(pack_ie(ATH10K_FW_IE_OTP_IMAGE, otp_bytes))
    return bytes(container)


def main():
    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
    FW_OUT_DIR.mkdir(parents=True, exist_ok=True)

    for label, rel_bin in [
        ("150511", "150511/ArcherC7v1_en_3_15_3_up_boot(150511).bin"),
        ("130729", "130729/ArcherC7v1_en_3_13_33_up_boot(130729).bin"),
    ]:
        bin_path = DOWNLOADS_DIR / rel_bin
        if not bin_path.exists():
            continue
        umac_path = bin_path.parent / "umac.ko"
        if not umac_path.exists():
            raw = bin_path.read_bytes()
            sq = raw[raw.find(b"hsqs") :]
            umac_path.write_bytes(extract_file_from_tplink_squashfs(sq, b"umac.ko"))
        print(f"=== Inspecting {label} ({umac_path.name}) ===")
        blobs = inspect_and_extract_umac_blobs(umac_path)
        for k, v in blobs.items():
            (EXTRACTED_DIR / f"{label}_{k}.bin").write_bytes(v)

        # Save primary extracted blobs from latest 150511 stock firmware
        if label == "150511":
            fw_data = blobs.get("athwlan_bin")
            otp_data = blobs.get("otp_bin")
            board_data = blobs.get("raw_Data")
            if fw_data and otp_data and board_data:
                (EXTRACTED_DIR / "firmware.bin").write_bytes(fw_data)
                (EXTRACTED_DIR / "otp.bin").write_bytes(otp_data)
                (EXTRACTED_DIR / "board.bin").write_bytes(board_data)

                fw2 = build_firmware_2_bin(fw_data, otp_data)
                (FW_OUT_DIR / "firmware-5.bin").write_bytes(fw2)
                (FW_OUT_DIR / "firmware-2.bin").write_bytes(fw2)
                (FW_OUT_DIR / "board.bin").write_bytes(board_data)
                print(
                    f"Generated {FW_OUT_DIR / 'firmware-5.bin'}, firmware-2.bin ({len(fw2)} B) and board.bin ({len(board_data)} B)"
                )


if __name__ == "__main__":
    main()
