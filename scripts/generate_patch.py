"""Generate 999-ath10k-restore-qca988x-hw1.0-support.patch from src_ref/."""
import difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_REF = ROOT / "src_ref"
PATCH_DIR = ROOT / "patches"


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise ValueError(f"Target block not found for {label}")
    if text.count(old) > 1:
        raise ValueError(f"Target block matched multiple times for {label}")
    return text.replace(old, new, 1)


def make_diff(rel_path: str, old_text: str, new_text: str) -> str:
    old_lines = old_text.splitlines(keepends=True)
    new_lines = new_text.splitlines(keepends=True)
    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=f"a/{rel_path}",
        tofile=f"b/{rel_path}",
        n=3,
    )
    return "".join(diff)


def build_patch() -> str:
    diffs = []

    # 1. hw.h
    hw_h = (SRC_REF / "hw.h").read_text(encoding="utf-8")
    hw_h_new = replace_exact(
        hw_h,
        """/* QCA988X 1.0 definitions (unsupported) */
#define QCA988X_HW_1_0_CHIP_ID_REV\t0x0""",
        """/* QCA988X 1.0 definitions */
#define QCA988X_HW_1_0_VERSION\t\t0x4000002c
#define QCA988X_HW_1_0_CHIP_ID_REV\t0x0
#define QCA988X_HW_1_0_FW_DIR\t\tATH10K_FW_DIR "/QCA988X/hw1.0"
#define QCA988X_HW_1_0_BOARD_DATA_FILE\t"board.bin"
#define QCA988X_HW_1_0_PATCH_LOAD_ADDR\t0x1234""",
        "hw.h QCA988X_HW_1_0",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/hw.h", hw_h, hw_h_new))

    # 2. core.h
    core_h = (SRC_REF / "core.h").read_text(encoding="utf-8")
    core_h_new = replace_exact(
        core_h,
        """\tconst u8 *wmi_key_cipher;
\tvoid *ce_priv;""",
        """\tconst u8 *wmi_key_cipher;
\tvoid *ce_priv;
\tbool hw_v1_workaround;
\tbool hw_v1_fw_running;""",
        "core.h hw_v1_workaround",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/core.h", core_h, core_h_new))

    # 3. core.c
    core_c = (SRC_REF / "core.c").read_text(encoding="utf-8")
    core_c_new = replace_exact(
        core_c,
        """static const struct ath10k_hw_params ath10k_hw_params_list[] = {
\t{
\t\t.id = QCA988X_HW_2_0_VERSION,""",
        """static const struct ath10k_hw_params ath10k_hw_params_list[] = {
\t{
\t\t.id = QCA988X_HW_1_0_VERSION,
\t\t.dev_id = QCA988X_2_0_DEVICE_ID,
\t\t.bus = ATH10K_BUS_PCI,
\t\t.name = "qca988x hw1.0",
\t\t.led_pin = 1,
\t\t.patch_load_addr = QCA988X_HW_1_0_PATCH_LOAD_ADDR,
\t\t.uart_pin = 7,
\t\t.cc_wraparound_type = ATH10K_HW_CC_WRAP_SHIFTED_ALL,
\t\t.otp_exe_param = 0,
\t\t.channel_counters_freq_hz = 88000,
\t\t.max_probe_resp_desc_thres = 0,
\t\t.cal_data_len = 2116,
\t\t.fw = {
\t\t\t.dir = QCA988X_HW_1_0_FW_DIR,
\t\t\t.board = QCA988X_HW_1_0_BOARD_DATA_FILE,
\t\t\t.board_size = 2116,
\t\t\t.board_ext_size = 0,
\t\t},
\t\t.rx_desc_ops = &qca988x_rx_desc_ops,
\t\t.hw_ops = &qca988x_ops,
\t\t.decap_align_bytes = 4,
\t\t.spectral_bin_discard = 0,
\t\t.spectral_bin_offset = 0,
\t\t.vht160_mcs_rx_highest = 0,
\t\t.vht160_mcs_tx_highest = 0,
\t\t.n_cipher_suites = 8,
\t\t.num_peers = 72,
\t\t.ast_skid_limit = 0x30,
\t\t.num_wds_entries = 0x20,
\t\t.target_64bit = false,
\t\t.rx_ring_fill_level = HTT_RX_RING_FILL_LEVEL,
\t\t.shadow_reg_support = false,
\t\t.rri_on_ddr = false,
\t\t.hw_filter_reset_required = false,
\t\t.fw_diag_ce_download = false,
\t\t.credit_size_workaround = false,
\t\t.tx_stats_over_pktlog = false,
\t\t.dynamic_sar_support = false,
\t\t.hw_restart_disconnect = false,
\t\t.use_fw_tx_credits = true,
\t\t.delay_unmap_buffer = false,
\t},
\t{
\t\t.id = QCA988X_HW_2_0_VERSION,""",
        "core.c ath10k_hw_params_list",
    )
    core_c_new = replace_exact(
        core_c_new,
        """\t/* FW descriptor/Data swap flags */
\tret = ath10k_bmi_write32(ar, hi_fw_swap, 0);

\tif (ret) {
\t\tath10k_err(ar, "setting FW data/desc swap flags failed\\n");
\t\treturn ret;
\t}

\t/* Some devices have a special sanity check that verifies the PCI
\t * Device ID is written to this host interest var. It is known to be
\t * required to boot QCA6164.
\t */
\tret = ath10k_bmi_write32(ar, hi_hci_uart_pwr_mgmt_params_ext,
\t\t\t\t ar->dev_id);
\tif (ret) {
\t\tath10k_err(ar, "failed to set pwr_mgmt_params: %d\\n", ret);
\t\treturn ret;
\t}""",
        """\tif (ar->target_version != QCA988X_HW_1_0_VERSION) {
\t\t/* FW descriptor/Data swap flags */
\t\tret = ath10k_bmi_write32(ar, hi_fw_swap, 0);

\t\tif (ret) {
\t\t\tath10k_err(ar, "setting FW data/desc swap flags failed\\n");
\t\t\treturn ret;
\t\t}

\t\t/* Some devices have a special sanity check that verifies the PCI
\t\t * Device ID is written to this host interest var. It is known to be
\t\t * required to boot QCA6164.
\t\t */
\t\tret = ath10k_bmi_write32(ar, hi_hci_uart_pwr_mgmt_params_ext,
\t\t\t\t\t ar->dev_id);
\t\tif (ret) {
\t\t\tath10k_err(ar, "failed to set pwr_mgmt_params: %d\\n", ret);
\t\t\treturn ret;
\t\t}
\t}""",
        "core.c ath10k_init_configure_target",
    )
    core_c_new = replace_exact(
        core_c_new,
        """\tu32 board_data_size = ar->hw_params.fw.board_size;
\tu32 board_ext_data_size = ar->hw_params.fw.board_ext_size;
\tu32 board_ext_data_addr;
\tint ret;

\tret = ath10k_bmi_read32(ar, hi_board_ext_data, &board_ext_data_addr);""",
        """\tu32 board_data_size = ar->hw_params.fw.board_size;
\tu32 board_ext_data_size = ar->hw_params.fw.board_ext_size;
\tu32 board_ext_data_addr;
\tint ret;

\tif (board_ext_data_size == 0)
\t\treturn 0;

\tret = ath10k_bmi_read32(ar, hi_board_ext_data, &board_ext_data_addr);""",
        "core.c ath10k_push_board_ext_data",
    )
    core_c_new = replace_exact(
        core_c_new,
        """static int ath10k_core_get_board_id_from_otp(struct ath10k *ar)
{
\tu32 result, address;
\tu8 board_id, chip_id;
\tbool ext_bid_support;
\tint ret, bmi_board_id_param;

\taddress = ar->hw_params.patch_load_addr;""",
        """static int ath10k_core_get_board_id_from_otp(struct ath10k *ar)
{
\tu32 result, address;
\tu8 board_id, chip_id;
\tbool ext_bid_support;
\tint ret, bmi_board_id_param;

\tif (ar->target_version == QCA988X_HW_1_0_VERSION)
\t\treturn -EOPNOTSUPP;

\taddress = ar->hw_params.patch_load_addr;""",
        "core.c ath10k_core_get_board_id_from_otp",
    )
    core_c_new = replace_exact(
        core_c_new,
        """\tret = ath10k_bmi_read32(ar, hi_board_data, &board_address);
\tif (ret) {
\t\tath10k_err(ar, "could not read board data addr (%d)\\n", ret);
\t\tgoto exit;
\t}""",
        """\tret = ath10k_bmi_read32(ar, hi_board_data, &board_address);
\tif (ret) {
\t\tath10k_err(ar, "could not read board data addr (%d)\\n", ret);
\t\tgoto exit;
\t}

\tif (board_address == 0 && ar->target_version == QCA988X_HW_1_0_VERSION)
\t\tboard_address = 0x00423900;""",
        "core.c ath10k_download_board_data",
    )
    core_c_new = replace_exact(
        core_c_new,
        """\t\tif (ath10k_peer_stats_enabled(ar)) {
\t\t\tmax_num_peers = TARGET_10X_TX_STATS_NUM_PEERS;
\t\t\tar->max_num_stations = TARGET_10X_TX_STATS_NUM_STATIONS;
\t\t} else {
\t\t\tmax_num_peers = TARGET_10X_NUM_PEERS;
\t\t\tar->max_num_stations = TARGET_10X_NUM_STATIONS;
\t\t}""",
        """\t\tif (ar->hw_v1_workaround) {
\t\t\tmax_num_peers = 72;
\t\t\tar->max_num_stations = 56;
\t\t} else if (ath10k_peer_stats_enabled(ar)) {
\t\t\tmax_num_peers = TARGET_10X_TX_STATS_NUM_PEERS;
\t\t\tar->max_num_stations = TARGET_10X_TX_STATS_NUM_STATIONS;
\t\t} else {
\t\t\tmax_num_peers = TARGET_10X_NUM_PEERS;
\t\t\tar->max_num_stations = TARGET_10X_NUM_STATIONS;
\t\t}""",
        "core.c ath10k_core_init_max_sta_count hw_v1_workaround",
    )
    core_c_new = replace_exact(
        core_c_new,
        """\tath10k_debug_print_boot_info(ar);
\tath10k_core_stop(ar);

\tmutex_unlock(&ar->conf_mutex);

\tath10k_hif_power_down(ar);
\treturn 0;""",
        """\tath10k_debug_print_boot_info(ar);
\tif (ar->hw_v1_workaround) {
\t\tar->hw_v1_fw_running = true;
\t\tmutex_unlock(&ar->conf_mutex);
\t\treturn 0;
\t}

\tath10k_core_stop(ar);

\tmutex_unlock(&ar->conf_mutex);

\tath10k_hif_power_down(ar);
\treturn 0;""",
        "core.c ath10k_core_probe_fw keep hw_v1_fw_running",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/core.c", core_c, core_c_new))

    # 3b. mac.c
    mac_c = (SRC_REF / "mac.c").read_text(encoding="utf-8")
    mac_c_new = replace_exact(
        mac_c,
        """\tret = ath10k_hif_power_up(ar, ATH10K_FIRMWARE_MODE_NORMAL);
\tif (ret) {
\t\tath10k_err(ar, "Could not init hif: %d\\n", ret);
\t\tgoto err_off;
\t}

\tret = ath10k_core_start(ar, ATH10K_FIRMWARE_MODE_NORMAL,
\t\t\t\t&ar->normal_mode_fw);
\tif (ret) {
\t\tath10k_err(ar, "Could not init core: %d\\n", ret);
\t\tgoto err_power_down;
\t}""",
        """\tif (!ar->hw_v1_fw_running) {
\t\tret = ath10k_hif_power_up(ar, ATH10K_FIRMWARE_MODE_NORMAL);
\t\tif (ret) {
\t\t\tath10k_err(ar, "Could not init hif: %d\\n", ret);
\t\t\tgoto err_off;
\t\t}

\t\tret = ath10k_core_start(ar, ATH10K_FIRMWARE_MODE_NORMAL,
\t\t\t\t\t&ar->normal_mode_fw);
\t\tif (ret) {
\t\t\tath10k_err(ar, "Could not init core: %d\\n", ret);
\t\t\tgoto err_power_down;
\t\t}
\t\tif (ar->hw_v1_workaround)
\t\t\tar->hw_v1_fw_running = true;
\t}""",
        "mac.c ath10k_start hw_v1_fw_running",
    )
    mac_c_new = replace_exact(
        mac_c_new,
        """\t\t\tif (ar->state != ATH10K_STATE_RESTARTING) {
\t\t\t\tath10k_halt(ar);
\t\t\t} else {""",
        """\t\t\tif (ar->hw_v1_workaround && ar->hw_v1_fw_running &&
\t\t\t    ar->state == ATH10K_STATE_ON) {
\t\t\t\t/* Keep QCA9880-AR1A v1 firmware running */
\t\t\t} else if (ar->state != ATH10K_STATE_RESTARTING) {
\t\t\t\tath10k_halt(ar);
\t\t\t} else {""",
        "mac.c ath10k_stop hw_v1_fw_running",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/mac.c", mac_c, mac_c_new))

    # 4. ce.h
    ce_h = (SRC_REF / "ce.h").read_text(encoding="utf-8")
    ce_h_new = replace_exact(
        ce_h,
        """/* Descriptor rings must be aligned to this boundary */
#define CE_DESC_RING_ALIGN\t8
#define CE_SEND_FLAG_GATHER\t0x00010000""",
        """/* Descriptor rings must be aligned to this boundary */
#define CE_DESC_RING_ALIGN\t8
#define CE_SEND_FLAG_GATHER\t0x00010000

#ifndef CDC_WAR_MAGIC_STR
#define CDC_WAR_MAGIC_STR\t0xceef0000
#define CDC_WAR_DATA_CE\t\t4
#endif""",
        "ce.h CDC_WAR_MAGIC_STR",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/ce.h", ce_h, ce_h_new))

    # 5. ce.c
    ce_c = (SRC_REF / "ce.c").read_text(encoding="utf-8")
    ce_c_new = replace_exact(
        ce_c,
        """static inline void ath10k_ce_src_ring_write_index_set(struct ath10k *ar,
\t\t\t\t\t\t      u32 ce_ctrl_addr,
\t\t\t\t\t\t      unsigned int n)
{
\tath10k_ce_write32(ar, ce_ctrl_addr +
\t\t\t  ar->hw_ce_regs->sr_wr_index_addr, n);
}""",
        """static inline void ath10k_ce_src_ring_write_index_set(struct ath10k *ar,
\t\t\t\t\t\t      u32 ce_ctrl_addr,
\t\t\t\t\t\t      unsigned int n)
{
\tif (ar->hw_v1_workaround) {
\t\tu32 indicator_addr = ce_ctrl_addr +
\t\t\t\t     ar->hw_ce_regs->wm_dstr->addr;
\t\tunsigned long irq_flags;

\t\tif (ce_ctrl_addr == ath10k_ce_base_address(ar, CDC_WAR_DATA_CE)) {
\t\t\tath10k_ce_write32(ar, indicator_addr,
\t\t\t\t\t  (CDC_WAR_MAGIC_STR | n));
\t\t\treturn;
\t\t}

\t\tlocal_irq_save(irq_flags);
\t\tath10k_ce_write32(ar, indicator_addr, 1);
\t\t(void)ath10k_ce_read32(ar, indicator_addr);
\t\t(void)ath10k_ce_read32(ar, indicator_addr);

\t\tath10k_ce_write32(ar, ce_ctrl_addr +
\t\t\t\t  ar->hw_ce_regs->sr_wr_index_addr, n);

\t\tath10k_ce_write32(ar, indicator_addr, 0);
\t\tlocal_irq_restore(irq_flags);
\t\treturn;
\t}

\tath10k_ce_write32(ar, ce_ctrl_addr +
\t\t\t  ar->hw_ce_regs->sr_wr_index_addr, n);
}""",
        "ce.c ath10k_ce_src_ring_write_index_set",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/ce.c", ce_c, ce_c_new))

    # 6. pci.h
    pci_h = (SRC_REF / "pci.h").read_text(encoding="utf-8")
    pci_h_new = replace_exact(
        pci_h,
        """\t/* Protects ps_awake and ps_wake_refcount */
\tspinlock_t ps_lock;""",
        """\t/* Protects ps_awake and ps_wake_refcount */
\tspinlock_t ps_lock;

\t/* Protects QCA988X hw1.0 PCIe write workaround */
\tspinlock_t hw_v1_workaround_lock;""",
        "pci.h hw_v1_workaround_lock",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/pci.h", pci_h, pci_h_new))

    # 7. pci.c
    pci_c = (SRC_REF / "pci.c").read_text(encoding="utf-8")
    pci_c_new = replace_exact(
        pci_c,
        """\t{ QCA988X_2_0_DEVICE_ID_UBNT, QCA988X_HW_2_0_CHIP_ID_REV },
\t{ QCA988X_2_0_DEVICE_ID, QCA988X_HW_2_0_CHIP_ID_REV },""",
        """\t{ QCA988X_2_0_DEVICE_ID_UBNT, QCA988X_HW_2_0_CHIP_ID_REV },
\t{ QCA988X_2_0_DEVICE_ID, QCA988X_HW_1_0_CHIP_ID_REV },
\t{ QCA988X_2_0_DEVICE_ID, QCA988X_HW_2_0_CHIP_ID_REV },""",
        "pci.c ath10k_pci_supp_chips",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """static void __ath10k_pci_wake(struct ath10k *ar)""",
        """static inline void ath10k_pci_raw_write32(struct ath10k *ar, u32 offset,
\t\t\t\t\t  u32 value)
{
\tstruct ath10k_pci *ar_pci = ath10k_pci_priv(ar);

\t/* Match TP-Link umac.ko WAR_PCI_WRITE32:
\t * Only perform the 3x (offset+4) dummy reads on Target SoC registers
\t * (< PCIE_LOCAL_BASE_ADDRESS) and never on the last CE register (0x50),
\t * where (offset+4) = 0x54 is unmapped.
\t */
\tif (ar->hw_v1_workaround &&
\t    offset < PCIE_LOCAL_BASE_ADDRESS &&
\t    !(offset >= 0x57400 && offset < 0x59400 && (offset & 0x3ff) == 0x50)) {
\t\tunsigned long irq_flags;

\t\tspin_lock_irqsave(&ar_pci->hw_v1_workaround_lock, irq_flags);
\t\t(void)ioread32(ar_pci->mem + offset + 4);
\t\t(void)ioread32(ar_pci->mem + offset + 4);
\t\t(void)ioread32(ar_pci->mem + offset + 4);
\t\tiowrite32(value, ar_pci->mem + offset);
\t\tspin_unlock_irqrestore(&ar_pci->hw_v1_workaround_lock, irq_flags);
\t} else {
\t\tiowrite32(value, ar_pci->mem + offset);
\t}
}

static void __ath10k_pci_wake(struct ath10k *ar)""",
        "pci.c ath10k_pci_raw_write32",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """\tiowrite32(value, ar_pci->mem + offset);
\tath10k_pci_sleep(ar);""",
        """\tath10k_pci_raw_write32(ar, offset, value);
\tath10k_pci_sleep(ar);""",
        "pci.c ath10k_bus_pci_write32",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """static int ath10k_pci_warm_reset(struct ath10k *ar)
{
\tint ret;

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot warm reset\\n");""",
        """static int ath10k_pci_warm_reset(struct ath10k *ar)
{
\tint ret;

\tif (ar->hw_v1_workaround)
\t\treturn ath10k_pci_wait_for_target_init(ar);

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot warm reset\\n");""",
        "pci.c ath10k_pci_warm_reset",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """static int ath10k_pci_qca988x_chip_reset(struct ath10k *ar)
{
\tint i, ret;
\tu32 val;

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot 988x chip reset\\n");""",
        """static int ath10k_pci_qca988x_chip_reset(struct ath10k *ar)
{
\tint i, ret;
\tu32 val;

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot 988x chip reset\\n");

\tif (ar->hw_v1_workaround)
\t\treturn ath10k_pci_wait_for_target_init(ar);""",
        "pci.c ath10k_pci_qca988x_chip_reset",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """static int ath10k_pci_cold_reset(struct ath10k *ar)
{
\tu32 val;

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot cold reset\\n");

\tspin_lock_bh(&ar->data_lock);

\tar->stats.fw_cold_reset_counter++;

\tspin_unlock_bh(&ar->data_lock);

\t/* Put Target, including PCIe, into RESET. */
\tval = ath10k_pci_reg_read32(ar, SOC_GLOBAL_RESET_ADDRESS);
\tval |= 1;
\tath10k_pci_reg_write32(ar, SOC_GLOBAL_RESET_ADDRESS, val);

\t/* After writing into SOC_GLOBAL_RESET to put device into
\t * reset and pulling out of reset pcie may not be stable
\t * for any immediate pcie register access and cause bus error,
\t * add delay before any pcie access request to fix this issue.
\t */
\tmsleep(20);

\t/* Pull Target, including PCIe, out of RESET. */
\tval &= ~1;
\tath10k_pci_reg_write32(ar, SOC_GLOBAL_RESET_ADDRESS, val);

\tmsleep(20);

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot cold reset complete\\n");

\treturn 0;
}""",
        """static int ath10k_pci_cold_reset(struct ath10k *ar)
{
\tstruct ath10k_pci *ar_pci = ath10k_pci_priv(ar);
\tu32 val;
\tint i;

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot cold reset\\n");

\tspin_lock_bh(&ar->data_lock);

\tar->stats.fw_cold_reset_counter++;

\tspin_unlock_bh(&ar->data_lock);

\tif (ar->hw_v1_workaround) {
\t\t/* Exact TP-Link umac.ko ath_pci_device_reset + ol_ath_pci_configure:
\t\t * 1. Wake target SoC via PCIE_SOC_WAKE_ADDRESS (0x80004)
\t\t * 2. Pulse SOC_GLOBAL_RESET_ADDRESS (0x80008) for 3ms (udelay 3000)
\t\t * 3. Re-wake target SoC via PCIE_SOC_WAKE_ADDRESS because
\t\t *    SOC_GLOBAL_RESET clears PCIE_SOC_WAKE back to 0!
\t\t */
\t\tiowrite32(PCIE_SOC_WAKE_V_MASK,
\t\t\t  ar_pci->mem + PCIE_LOCAL_BASE_ADDRESS +
\t\t\t  PCIE_SOC_WAKE_ADDRESS);
\t\tfor (i = 0; i < 10; i++) {
\t\t\tif (ath10k_pci_is_awake(ar))
\t\t\t\tbreak;
\t\t\tudelay(1000);
\t\t}

\t\tval = ioread32(ar_pci->mem + PCIE_LOCAL_BASE_ADDRESS +
\t\t\t       SOC_GLOBAL_RESET_ADDRESS);
\t\tval |= 1;
\t\tiowrite32(val,
\t\t\t  ar_pci->mem + PCIE_LOCAL_BASE_ADDRESS +
\t\t\t  SOC_GLOBAL_RESET_ADDRESS);
\t\tudelay(3000);

\t\tval &= ~1;
\t\tiowrite32(val,
\t\t\t  ar_pci->mem + PCIE_LOCAL_BASE_ADDRESS +
\t\t\t  SOC_GLOBAL_RESET_ADDRESS);
\t\tudelay(3000);

\t\tiowrite32(PCIE_SOC_WAKE_V_MASK,
\t\t\t  ar_pci->mem + PCIE_LOCAL_BASE_ADDRESS +
\t\t\t  PCIE_SOC_WAKE_ADDRESS);
\t\tfor (i = 0; i < 20; i++) {
\t\t\tif (ath10k_pci_is_awake(ar))
\t\t\t\tbreak;
\t\t\tudelay(1000);
\t\t}
\t\tar_pci->ps_awake = true;
\t\treturn 0;
\t}

\t/* Put Target, including PCIe, into RESET. */
\tval = ath10k_pci_reg_read32(ar, SOC_GLOBAL_RESET_ADDRESS);
\tval |= 1;
\tath10k_pci_reg_write32(ar, SOC_GLOBAL_RESET_ADDRESS, val);

\t/* After writing into SOC_GLOBAL_RESET to put device into
\t * reset and pulling out of reset pcie may not be stable
\t * for any immediate pcie register access and cause bus error,
\t * add delay before any pcie access request to fix this issue.
\t */
\tmsleep(20);

\t/* Pull Target, including PCIe, out of RESET. */
\tval &= ~1;
\tath10k_pci_reg_write32(ar, SOC_GLOBAL_RESET_ADDRESS, val);

\tmsleep(20);

\tath10k_dbg(ar, ATH10K_DBG_BOOT, "boot cold reset complete\\n");

\treturn 0;
}""",
        "pci.c ath10k_pci_cold_reset",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """\tpci_set_master(pdev);

\t/* Arrange for access to Target SoC registers. */""",
        """\tpci_set_master(pdev);

\t/* Match TP-Link umac.ko (0xa4c20..0xa4c5c): clear L0s/L1 ASPM bits at 0x80 */
\t{
\t\tu32 lnkctl = 0;
\t\tpci_read_config_dword(pdev, 0x80, &lnkctl);
\t\tpci_write_config_dword(pdev, 0x80, lnkctl & 0xffffff00);
\t}

\t/* Arrange for access to Target SoC registers. */""",
        "pci.c ath10k_pci_claim disable ASPM 0x80",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """\tspin_lock_init(&ce->ce_lock);
\tspin_lock_init(&ar_pci->ps_lock);
\tmutex_init(&ar_pci->ce_diag_mutex);""",
        """\tspin_lock_init(&ce->ce_lock);
\tspin_lock_init(&ar_pci->ps_lock);
\tspin_lock_init(&ar_pci->hw_v1_workaround_lock);
\tmutex_init(&ar_pci->ce_diag_mutex);""",
        "pci.c ath10k_pci_setup_resource",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """\tret = ath10k_pci_claim(ar);
\tif (ret) {
\t\tath10k_err(ar, "failed to claim device: %d\\n", ret);
\t\tgoto err_free_pipes;
\t}

\tret = ath10k_pci_force_wake(ar);""",
        """\tret = ath10k_pci_claim(ar);
\tif (ret) {
\t\tath10k_err(ar, "failed to claim device: %d\\n", ret);
\t\tgoto err_free_pipes;
\t}

\tif (is_qca988x)
\t\tar->hw_v1_workaround = true;

\tret = ath10k_pci_force_wake(ar);""",
        "pci.c ath10k_pci_probe provisional hw_v1_workaround",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """\tif (is_qca988x) {
\t\tbus_params.chip_id =
\t\t\tath10k_pci_soc_read32(ar, SOC_CHIP_ID_ADDRESS);
\t\tif (bus_params.chip_id != 0xffffffff) {
\t\t\tif (!ath10k_pci_chip_is_supported(pdev->device,
\t\t\t\t\t\t\t  bus_params.chip_id)) {
\t\t\t\tret = -ENODEV;
\t\t\t\tgoto err_unsupported;
\t\t\t}
\t\t}
\t}""",
        """\tif (is_qca988x) {
\t\tbus_params.chip_id =
\t\t\tath10k_pci_soc_read32(ar, SOC_CHIP_ID_ADDRESS);
\t\tif (bus_params.chip_id != 0xffffffff) {
\t\t\tif (MS(bus_params.chip_id, SOC_CHIP_ID_REV) !=
\t\t\t    QCA988X_HW_1_0_CHIP_ID_REV)
\t\t\t\tar->hw_v1_workaround = false;

\t\t\tif (!ath10k_pci_chip_is_supported(pdev->device,
\t\t\t\t\t\t\t  bus_params.chip_id)) {
\t\t\t\tret = -ENODEV;
\t\t\t\tgoto err_unsupported;
\t\t\t}
\t\t}
\t}""",
        "pci.c ath10k_pci_probe chip_id check",
    )
    pci_c_new = replace_exact(
        pci_c_new,
        """/* QCA988x 2.0 firmware files */""",
        """/* QCA988x 1.0 firmware files */
MODULE_FIRMWARE(QCA988X_HW_1_0_FW_DIR "/" ATH10K_FW_API2_FILE);
MODULE_FIRMWARE(QCA988X_HW_1_0_FW_DIR "/" ATH10K_FW_API5_FILE);
MODULE_FIRMWARE(QCA988X_HW_1_0_FW_DIR "/" QCA988X_HW_1_0_BOARD_DATA_FILE);

/* QCA988x 2.0 firmware files */""",
        "pci.c MODULE_FIRMWARE",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/pci.c", pci_c, pci_c_new))

    # 8. wmi.c
    wmi_c = (SRC_REF / "wmi.c").read_text(encoding="utf-8")
    wmi_c_new = replace_exact(
        wmi_c,
        """\tif (skb_push(skb, sizeof(struct wmi_cmd_hdr)) == NULL)
\t\treturn -ENOMEM;

\tcmd |= SM(cmd_id, WMI_CMD_HDR_CMD_ID);""",
        """\tif (skb_push(skb, sizeof(struct wmi_cmd_hdr)) == NULL)
\t\treturn -ENOMEM;

\tif (ar->hw_v1_workaround) {
\t\tif (cmd_id == WMI_10X_ECHO_CMDID)
\t\t\tcmd_id = 0x9005;
\t\telse if (cmd_id == WMI_10X_PDEV_SET_REGDOMAIN_CMDID)
\t\t\tcmd_id = 0x9006;
\t\telse if (cmd_id == WMI_10X_PDEV_SET_CHANNEL_CMDID)
\t\t\tcmd_id = 0x9007;
\t\telse if (cmd_id >= WMI_10X_PDEV_SET_PARAM_CMDID &&
\t\t\t cmd_id <= WMI_10X_PDEV_SET_VHT_CAP_IE_CMDID)
\t\t\tcmd_id += 3;
\t\telse if (cmd_id >= WMI_10X_PDEV_GET_TPC_CONFIG_CMDID &&
\t\t\t cmd_id <= WMI_10X_VDEV_START_REQUEST_CMDID)
\t\t\tcmd_id -= 1;
\t\telse if (cmd_id == WMI_10X_VDEV_RESTART_REQUEST_CMDID)
\t\t\tcmd_id = 0x9012;
\t\telse if (cmd_id >= WMI_10X_VDEV_UP_CMDID &&
\t\t\t cmd_id <= WMI_10X_PEER_FLUSH_TIDS_CMDID)
\t\t\tcmd_id -= 2;
\t\telse if (cmd_id >= WMI_10X_PEER_ASSOC_CMDID &&
\t\t\t cmd_id <= WMI_10X_RTT_TSF_CMDID)
\t\t\tcmd_id += 1;
\t\telse if (cmd_id == WMI_10X_PDEV_SEND_BCN_CMDID)
\t\t\tcmd_id = 0x9057;
\t\telse if (cmd_id == WMI_10X_REQUEST_STATS_CMDID)
\t\t\tcmd_id = 0x9059;
\t}

\tcmd |= SM(cmd_id, WMI_CMD_HDR_CMD_ID);""",
        "wmi.c ath10k_wmi_cmd_send_nowait hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """static int
ath10k_wmi_op_pull_vdev_start_ev(struct ath10k *ar, struct sk_buff *skb,
\t\t\t\t struct wmi_vdev_start_ev_arg *arg)
{
\tstruct wmi_vdev_start_response_event *ev = (void *)skb->data;

\tif (skb->len < sizeof(*ev))
\t\treturn -EPROTO;""",
        """static int
ath10k_wmi_op_pull_vdev_start_ev(struct ath10k *ar, struct sk_buff *skb,
\t\t\t\t struct wmi_vdev_start_ev_arg *arg)
{
\tstruct wmi_vdev_start_response_event *ev = (void *)skb->data;

\tif (ar->hw_v1_workaround) {
\t\tif (skb->len < 4)
\t\t\treturn -EPROTO;
\t\targ->vdev_id = ev->vdev_id;
\t\targ->req_id = (skb->len >= 8) ? ev->req_id : 0;
\t\targ->resp_type = (skb->len >= 12) ? ev->resp_type : 0;
\t\targ->status = 0;
\t\tskb_pull(skb, skb->len);
\t\treturn 0;
\t}

\tif (skb->len < sizeof(*ev))
\t\treturn -EPROTO;""",
        "wmi.c ath10k_wmi_op_pull_vdev_start_ev hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """static int
ath10k_wmi_10x_op_pull_svc_rdy_ev(struct ath10k *ar, struct sk_buff *skb,
\t\t\t\t  struct wmi_svc_rdy_ev_arg *arg)
{
\tstruct wmi_10x_service_ready_event *ev;
\tint i, n;

\tif (skb->len < sizeof(*ev))
\t\treturn -EPROTO;""",
        """static int
ath10k_wmi_10x_op_pull_svc_rdy_ev(struct ath10k *ar, struct sk_buff *skb,
\t\t\t\t  struct wmi_svc_rdy_ev_arg *arg)
{
\tstruct wmi_10x_service_ready_event *ev;
\tint i, n;

\tif (ar->hw_v1_workaround) {
\t\tif (skb->len < 140)
\t\t\treturn -EPROTO;
\t\tev = (void *)skb->data;
\t\tskb_pull(skb, skb->len);
\t\targ->min_tx_power = ev->hw_min_tx_power;
\t\targ->max_tx_power = ev->hw_max_tx_power;
\t\targ->ht_cap = ev->ht_cap_info;
\t\targ->vht_cap = ev->vht_cap_info;
\t\targ->vht_supp_mcs = ev->vht_supp_mcs;
\t\targ->sw_ver0 = ev->sw_version;
\t\targ->phy_capab = ev->phy_capability;
\t\targ->num_rf_chains = ev->num_rf_chains;
\t\targ->eeprom_rd = 0;
\t\targ->low_2ghz_chan = ev->hal_reg_capabilities.low_2ghz_chan;
\t\targ->high_2ghz_chan = ev->hal_reg_capabilities.high_2ghz_chan;
\t\targ->low_5ghz_chan = ev->hal_reg_capabilities.low_5ghz_chan;
\t\targ->high_5ghz_chan = ev->hal_reg_capabilities.high_5ghz_chan;
\t\targ->num_mem_reqs = 0;
\t\targ->service_map = ev->wmi_service_bitmap;
\t\targ->service_map_len = sizeof(ev->wmi_service_bitmap);
\t\treturn 0;
\t}

\tif (skb->len < sizeof(*ev))
\t\treturn -EPROTO;""",
        "wmi.c ath10k_wmi_10x_op_pull_svc_rdy_ev hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """static void ath10k_wmi_10_1_op_rx(struct ath10k *ar, struct sk_buff *skb)
{
\tstruct wmi_cmd_hdr *cmd_hdr;
\tenum wmi_10x_event_id id;
\tbool consumed;

\tcmd_hdr = (struct wmi_cmd_hdr *)skb->data;
\tid = MS(__le32_to_cpu(cmd_hdr->cmd_id), WMI_CMD_HDR_CMD_ID);

\tif (skb_pull(skb, sizeof(struct wmi_cmd_hdr)) == NULL)
\t\tgoto out;""",
        """static void ath10k_wmi_10_1_op_rx(struct ath10k *ar, struct sk_buff *skb)
{
\tstruct wmi_cmd_hdr *cmd_hdr;
\tenum wmi_10x_event_id id;
\tbool consumed;

\tcmd_hdr = (struct wmi_cmd_hdr *)skb->data;
\tid = MS(__le32_to_cpu(cmd_hdr->cmd_id), WMI_CMD_HDR_CMD_ID);

\tif (skb_pull(skb, sizeof(struct wmi_cmd_hdr)) == NULL)
\t\tgoto out;

\tif (ar->hw_v1_workaround) {
\t\tif (id == 0x9009 || id == 0x9014 || id == 0x901c || id == 0x901d)
\t\t\tgoto out;
\t\telse if (id >= 0x900a && id <= 0x9013)
\t\t\tid -= 1;
\t\telse if (id >= 0x9015 && id <= 0x9019)
\t\t\tid -= 2;
\t\telse if (id == 0x901a)
\t\t\tid = WMI_10X_PDEV_TPC_CONFIG_EVENTID;
\t}""",
        "wmi.c ath10k_wmi_10_1_op_rx hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """static struct sk_buff *
ath10k_wmi_op_gen_pdev_set_base_macaddr(struct ath10k *ar,
\t\t\t\t\tconst u8 macaddr[ETH_ALEN])
{
\tstruct wmi_pdev_set_base_macaddr_cmd *cmd;
\tstruct sk_buff *skb;""",
        """static struct sk_buff *
ath10k_wmi_op_gen_pdev_set_base_macaddr(struct ath10k *ar,
\t\t\t\t\tconst u8 macaddr[ETH_ALEN])
{
\tstruct wmi_pdev_set_base_macaddr_cmd *cmd;
\tstruct sk_buff *skb;

\tif (ar->hw_v1_workaround)
\t\treturn ERR_PTR(-EOPNOTSUPP);""",
        "wmi.c ath10k_wmi_op_gen_pdev_set_base_macaddr hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """static struct sk_buff *
ath10k_wmi_10x_op_gen_pdev_set_rd(struct ath10k *ar, u16 rd, u16 rd2g, u16
\t\t\t\t  rd5g, u16 ctl2g, u16 ctl5g,
\t\t\t\t  enum wmi_dfs_region dfs_reg)
{
\tstruct wmi_pdev_set_regdomain_cmd_10x *cmd;
\tstruct sk_buff *skb;""",
        """static struct sk_buff *
ath10k_wmi_10x_op_gen_pdev_set_rd(struct ath10k *ar, u16 rd, u16 rd2g, u16
\t\t\t\t  rd5g, u16 ctl2g, u16 ctl5g,
\t\t\t\t  enum wmi_dfs_region dfs_reg)
{
\tstruct wmi_pdev_set_regdomain_cmd_10x *cmd;
\tstruct sk_buff *skb;

\tif (ar->hw_v1_workaround)
\t\treturn ath10k_wmi_op_gen_pdev_set_rd(ar, rd, rd2g, rd5g,
\t\t\t\t\t\t     ctl2g, ctl5g, dfs_reg);""",
        "wmi.c ath10k_wmi_10x_op_gen_pdev_set_rd hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """\tconfig.num_msdu_desc = __cpu_to_le32(TARGET_10X_NUM_MSDU_DESC);
\tconfig.max_frag_entries = __cpu_to_le32(TARGET_10X_MAX_FRAG_ENTRIES);

\tbuf = ath10k_wmi_alloc_skb(ar, struct_size(cmd, mem_chunks.items,
\t\t\t\t\t\t   ar->wmi.num_mem_chunks));
\tif (!buf)
\t\treturn ERR_PTR(-ENOMEM);

\tcmd = (struct wmi_init_cmd_10x *)buf->data;""",
        """\tconfig.num_msdu_desc = __cpu_to_le32(TARGET_10X_NUM_MSDU_DESC);
\tconfig.max_frag_entries = __cpu_to_le32(TARGET_10X_MAX_FRAG_ENTRIES);

\tif (ar->hw_v1_workaround) {
\t\tconfig.num_vdevs = __cpu_to_le32(16);
\t\tconfig.num_peers = __cpu_to_le32(72);
\t\tconfig.num_peer_keys = __cpu_to_le32(2);
\t\tconfig.num_tids = __cpu_to_le32(144);
\t\tconfig.ast_skid_limit = __cpu_to_le32(48);
\t\tconfig.num_mcast_groups = __cpu_to_le32(4);
\t\tconfig.num_mcast_table_elems = __cpu_to_le32(16);
\t\tconfig.mcast2ucast_mode = __cpu_to_le32(2);
\t\tconfig.dma_burst_size = __cpu_to_le32(1);
\t\tconfig.rx_skip_defrag_timeout_dup_detection_check = __cpu_to_le32(0);

\t\tbuf = ath10k_wmi_alloc_skb(ar, 96);
\t\tif (!buf)
\t\t\treturn ERR_PTR(-ENOMEM);
\t\tmemcpy(buf->data, &config, 96);
\t\treturn buf;
\t}

\tbuf = ath10k_wmi_alloc_skb(ar, struct_size(cmd, mem_chunks.items,
\t\t\t\t\t\t   ar->wmi.num_mem_chunks));
\tif (!buf)
\t\treturn ERR_PTR(-ENOMEM);

\tcmd = (struct wmi_init_cmd_10x *)buf->data;""",
        "wmi.c ath10k_wmi_10_1_op_gen_init hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """\tath10k_wmi_put_wmi_channel(ar, &cmd->chan, &arg->channel);

\tath10k_dbg(ar, ATH10K_DBG_WMI,""",
        """\tath10k_wmi_put_wmi_channel(ar, &cmd->chan, &arg->channel);

\tif (ar->hw_v1_workaround) {
\t\tmemset(skb->data + 28, 0, 40);
\t\tskb_trim(skb, 68);
\t}

\tath10k_dbg(ar, ATH10K_DBG_WMI,""",
        "wmi.c ath10k_wmi_op_gen_vdev_start hw_v1_workaround",
    )
    wmi_c_new = replace_exact(
        wmi_c_new,
        """\tif (deliver_cab)
\t\tcmd->flags |= __cpu_to_le32(WMI_BCN_TX_REF_FLAG_DELIVER_CAB);

\treturn skb;""",
        """\tif (deliver_cab)
\t\tcmd->flags |= __cpu_to_le32(WMI_BCN_TX_REF_FLAG_DELIVER_CAB);

\tif (ar->hw_v1_workaround)
\t\tskb_trim(skb, 24);

\treturn skb;""",
        "wmi.c ath10k_wmi_op_gen_beacon_dma hw_v1_workaround",
    )
    diffs.append(make_diff("drivers/net/wireless/ath/ath10k/wmi.c", wmi_c, wmi_c_new))

    return "".join(diffs)


if __name__ == "__main__":
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    patch_content = build_patch()
    out_path = PATCH_DIR / "999-ath10k-restore-qca988x-hw1.0-support.patch"
    out_path.write_bytes(patch_content.encode("utf-8"))
    print(f"Wrote {out_path} ({len(patch_content)} bytes)")
