#!/usr/bin/env python3
"""
Compiles the patched kmod-ath10k package in the OpenWrt 23.05.5 SDK (WSL2)
with unneeded mac80211 drivers disabled for fast compilation, then builds
the final TP-Link Archer C7 v1 factory.bin and sysupgrade.bin images using
the OpenWrt 23.05.5 ImageBuilder.
"""
import glob
import os
import re
import shutil
import subprocess
import sys

SDK_DIR = "/root/work/sdk"
IB_DIR = "/root/work/ib"
WIN_ROOT = "/workspace/archer-c7-v1-openwrt"
OUTPUT_DIR = f"{WIN_ROOT}/output"
FILES_DIR = f"{WIN_ROOT}/files"
PATCH_SRC = f"{WIN_ROOT}/patches/999-ath10k-restore-qca988x-hw1.0-support.patch"
PATCH_DST = f"{SDK_DIR}/package/kernel/mac80211/patches/ath10k/999-ath10k-restore-qca988x-hw1.0-support.patch"


def run(cmd, cwd=None, check=True):
    print(f"\n>>> Running: {' '.join(cmd)} (cwd={cwd})", flush=True)
    res = subprocess.run(cmd, cwd=cwd)
    if check and res.returncode != 0:
        sys.exit(res.returncode)
    return res.returncode


def trim_sdk_config():
    config_path = f"{SDK_DIR}/.config"
    with open(config_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Keep only the wireless packages needed for Archer C7 v1
    keep_pkgs = {
        "CONFIG_PACKAGE_kmod-cfg80211",
        "CONFIG_PACKAGE_kmod-mac80211",
        "CONFIG_PACKAGE_kmod-ath",
        "CONFIG_PACKAGE_kmod-ath9k-common",
        "CONFIG_PACKAGE_kmod-ath9k",
        "CONFIG_PACKAGE_kmod-ath10k",
    }

    # Disable all other wireless / mac80211 kmods so mac80211 builds in ~20s
    disable_prefixes = (
        "CONFIG_PACKAGE_kmod-ath10k-",
        "CONFIG_PACKAGE_kmod-ath11k",
        "CONFIG_PACKAGE_kmod-ath5k",
        "CONFIG_PACKAGE_kmod-ath6kl",
        "CONFIG_PACKAGE_kmod-ath9k-htc",
        "CONFIG_PACKAGE_kmod-ar5523",
        "CONFIG_PACKAGE_kmod-carl9170",
        "CONFIG_PACKAGE_kmod-wil6210",
        "CONFIG_PACKAGE_kmod-brcm",
        "CONFIG_PACKAGE_kmod-iwl",
        "CONFIG_PACKAGE_kmod-libertas",
        "CONFIG_PACKAGE_kmod-mac80211-hwsim",
        "CONFIG_PACKAGE_kmod-mt76",
        "CONFIG_PACKAGE_kmod-mwifiex",
        "CONFIG_PACKAGE_kmod-mwl8k",
        "CONFIG_PACKAGE_kmod-net-prism54",
        "CONFIG_PACKAGE_kmod-Net-rtl",
        "CONFIG_PACKAGE_kmod-owl-loader",
        "CONFIG_PACKAGE_kmod-p54",
        "CONFIG_PACKAGE_kmod-rsi91x",
        "CONFIG_PACKAGE_kmod-rt2",
        "CONFIG_PACKAGE_kmod-rtl",
        "CONFIG_PACKAGE_kmod-rtw88",
        "CONFIG_PACKAGE_kmod-rtw89",
        "CONFIG_PACKAGE_kmod-wl1",
        "CONFIG_PACKAGE_kmod-wlcore",
        "CONFIG_PACKAGE_kmod-zd1211rw",
        "CONFIG_PACKAGE_kmod-adm8211",
        "CONFIG_PACKAGE_kmod-airo",
        "CONFIG_PACKAGE_kmod-hermes",
        "CONFIG_PACKAGE_kmod-mac80211-smallbuffers",
    )

    new_lines = []
    for line in text.splitlines():
        m = re.match(r"^(CONFIG_PACKAGE_kmod-[A-Za-z0-9_-]+)=[ym]$", line)
        if m:
            pkg = m.group(1)
            if pkg not in keep_pkgs and pkg.startswith(disable_prefixes):
                new_lines.append(f"# {pkg} is not set")
                continue
        if line.startswith("CONFIG_ALL_KMODS=y"):
            new_lines.append("# CONFIG_ALL_KMODS is not set")
            continue
        new_lines.append(line)

    for pkg in keep_pkgs:
        new_lines.append(f"{pkg}=m")
    new_lines.append("CONFIG_ATH_USER_REGD=y")
    new_lines.append("CONFIG_PACKAGE_ATH_DEBUG=y")

    with open(config_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")

    run(["make", "defconfig"], cwd=SDK_DIR)


def main():
    os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pkg_dir = f"{SDK_DIR}/bin/targets/ath79/generic/packages"
    existing_ipks = glob.glob(f"{pkg_dir}/kmod-ath10k_*.ipk")
    ko_core = f"{SDK_DIR}/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-6.1.110-1/drivers/net/wireless/ath/ath10k/ath10k_core.ko"

    if not existing_ipks or not os.path.exists(ko_core) or os.path.getmtime(ko_core) < os.path.getmtime(PATCH_SRC):
        shutil.copyfile(PATCH_SRC, PATCH_DST)
        print(f"Copied patch to {PATCH_DST}", flush=True)
        trim_sdk_config()
        run(["make", "package/kernel/mac80211/clean"], cwd=SDK_DIR)
        run(["make", "package/kernel/mac80211/compile", f"-j{os.cpu_count() or 4}", "V=s"], cwd=SDK_DIR, check=False)
    else:
        print("Using freshly compiled kmod-ath10k package and .ko modules.", flush=True)

    # Locate built kmod-ath10k ipk and copy wireless kmod ipks into ImageBuilder
    pkg_dir = f"{SDK_DIR}/bin/targets/ath79/generic/packages"
    ib_pkg_dir = f"{IB_DIR}/packages"
    for pat in [
        "kmod-cfg80211_*.ipk",
        "kmod-mac80211_*.ipk",
        "kmod-ath_*.ipk",
        "kmod-ath9k-common_*.ipk",
        "kmod-ath9k_*.ipk",
        "kmod-ath10k_*.ipk",
    ]:
        matches = glob.glob(f"{pkg_dir}/{pat}")
        if not matches:
            print(f"ERROR: Missing compiled package matching {pat}", file=sys.stderr)
            sys.exit(1)
        for m in matches:
            dst = os.path.join(ib_pkg_dir, os.path.basename(m))
            if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(m):
                shutil.copyfile(m, dst)
                for idx in glob.glob(f"{IB_DIR}/packages/Packages*"):
                    os.remove(idx)
                print(f"Copied {m} -> {dst}", flush=True)
            shutil.copyfile(m, os.path.join(OUTPUT_DIR, os.path.basename(m)))

    # Also extract ath10k_core.ko and ath10k_pci.ko from kmod-ath10k_*.ipk to OUTPUT_DIR
    ath10k_ipk = glob.glob(f"{pkg_dir}/kmod-ath10k_*.ipk")[0]
    tmp_extract = "/tmp/extract_ath10k_ipk"
    shutil.rmtree(tmp_extract, ignore_errors=True)
    os.makedirs(tmp_extract, exist_ok=True)
    run(["tar", "-xzf", ath10k_ipk], cwd=tmp_extract)
    run(["tar", "-xzf", "data.tar.gz"], cwd=tmp_extract)
    for ko in glob.glob(f"{tmp_extract}/lib/modules/*/ath10k*.ko"):
        shutil.copyfile(ko, os.path.join(OUTPUT_DIR, os.path.basename(ko)))
        print(f"Extracted {ko} -> {OUTPUT_DIR}", flush=True)

    # Build final factory.bin and sysupgrade.bin via ImageBuilder
    # Note: remove ath10k-firmware-qca988x if selected by default profile, and include our custom files
    packages_arg = (
        "kmod-ath9k kmod-ath10k -ath10k-firmware-qca988x -kmod-ath10k-ct "
        "wpad-basic-mbedtls luci luci-ssl iwinfo"
    )
    for attempt in range(1, 5):
        print(f"Running ImageBuilder (attempt {attempt}/4)...", flush=True)
        rc = run(
            [
                "make",
                "image",
                "PROFILE=tplink_archer-c7-v1",
                f"PACKAGES={packages_arg}",
                f"FILES={FILES_DIR}",
            ],
            cwd=IB_DIR,
            check=False,
        )
        if rc == 0:
            break
        if attempt == 4:
            sys.exit(rc)

    ib_bin_dir = f"{IB_DIR}/bin/targets/ath79/generic"
    sysupgrade_src = f"{ib_bin_dir}/openwrt-23.05.5-ath79-generic-tplink_archer-c7-v1-squashfs-sysupgrade.bin"
    factory_src = f"{ib_bin_dir}/openwrt-23.05.5-ath79-generic-tplink_archer-c7-v1-squashfs-factory.bin"

    for src in [sysupgrade_src, factory_src]:
        if not os.path.exists(src):
            print(f"ERROR: Expected image not found: {src}", file=sys.stderr)
            sys.exit(1)
        shutil.copyfile(src, os.path.join(OUTPUT_DIR, os.path.basename(src)))
        print(f"Copied image {src} -> {OUTPUT_DIR} ({os.path.getsize(src)} bytes)", flush=True)

    # Also create short-named factory.bin for TP-Link stock web UI
    shutil.copyfile(factory_src, os.path.join(OUTPUT_DIR, "factory.bin"))
    shutil.copyfile(sysupgrade_src, os.path.join(OUTPUT_DIR, "sysupgrade.bin"))

    # Inspect SquashFS contents inside sysupgrade.bin and save manifest
    with open(sysupgrade_src, "rb") as f:
        data = f.read()
    hsqs_off = data.find(b"hsqs")
    if hsqs_off < 0:
        print("ERROR: SquashFS magic 'hsqs' not found in sysupgrade.bin", file=sys.stderr)
        sys.exit(1)
    sqfs_tmp = "/tmp/c7v1_rootfs.sqfs"
    with open(sqfs_tmp, "wb") as f:
        f.write(data[hsqs_off:])
    manifest_out = subprocess.check_output(["unsquashfs", "-l", sqfs_tmp], text=True)
    with open(os.path.join(OUTPUT_DIR, "squashfs_manifest.txt"), "w", encoding="utf-8") as f:
        f.write(manifest_out)
    print(f"Saved SquashFS manifest ({len(manifest_out.splitlines())} entries)", flush=True)
    print("ALL BUILD STEPS COMPLETED SUCCESSFULLY!", flush=True)


if __name__ == "__main__":
    main()
