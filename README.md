# Кастомная прошивка OpenWrt 23.05.5 для TP-Link Archer C7 v1 (с рабочим 5 ГГц модулем `QCA9880-AR1A hw1.0`)

Готовая сборка **OpenWrt 23.05.5 (`ath79/generic`, ядро Linux `5.15.167`)** для маршрутизатора **TP-Link Archer C7 v1 (Ver 1.0 / 1.1)** с восстановленной и пропатченной поддержкой встроенного 5 ГГц радиомодуля `QCA9880-AR1A` (`hw1.0`, `target_version = 0x4000002c`) и веб-интерфейсом **LuCI (HTTPS/HTTP)**.

---

## Готовые файлы прошивки (`output/`)

| Файл | Назначение | Размер | SHA-256 |
|---|---|---|---|
| `output/factory.bin` *(короткое имя для заводского веб-интерфейса TP-Link)* | **Первичная прошивка со стоковой (заводской) прошивки TP-Link** (`HWID: 0x75000001`, `HWREV: 0x00000001`) | `8,126,464` байт (`7.75 МБ`) | `595b6380b825b547f6794378ab416411aeea512ebc1257e5a508e35e4145fc11` |
| `output/openwrt-23.05.5-ath79-generic-tplink_archer-c7-v1-squashfs-factory.bin` | Полная копия `factory.bin` со стандартным именем OpenWrt | `8,126,464` байт (`7.75 МБ`) | `595b6380b825b547f6794378ab416411aeea512ebc1257e5a508e35e4145fc11` |
| `output/sysupgrade.bin` / `output/openwrt-23.05.5-ath79-generic-tplink_archer-c7-v1-squashfs-sysupgrade.bin` | **Обновление поверх уже установленной OpenWrt** (оставляет ~1.66 МБ свободного места под JFFS2 `/overlay` на 8 МБ флеш-памяти) | `6,423,351` байт (`6.12 МБ`) | `672bb6484ffca572f801931fa0ff96692deb5d740aea60d114d6cc44b4c3ed6a` |

---

## Что именно сделано для работы 5 ГГц (`QCA9880-AR1A hw1.0`)

1. **Извлечены оригинальные заводские микрокоды `QCA988X hw1.0` из стокового драйвера `umac.ko` TP-Link Archer C7 v1 (`scripts/extract_c7v1_fw.py`):**
   - Целевой микрокод `firmware.bin` (`189,476` байт, версия `10.1.389-eb9f329`).
   - Скрипт калибровки и инициализации `otp.bin` (`3,569` байт).
   - Калибровочные данные радио-тракта `board.bin` (`2,116` байт).
   - Упакованы в контейнеры `/lib/firmware/ath10k/QCA988X/hw1.0/firmware-5.bin` и `firmware-2.bin` (`189,792` байта) с заголовками `QCA-ATH10K` (`WMI 10.1`, `HTT 10.1`).
2. **Дизассемблирован заводской модуль `umac.ko` и создан патч ядра `patches/999-ath10k-restore-qca988x-hw1.0-support.patch`:**
   - Восстановлен профиль `QCA988X_HW_1_0_VERSION` (`0x4000002c`, `.hw_v1_workaround = true`, `.board_ext_size = 0`).
   - **`WAR_PCI_WRITE32` (`ath10k_pci_raw_write32`):** Перед каждой записью в MMIO-регистр PCIe под `spin_lock_irqsave` выполняются 3 холостых чтения `ioread32(ar_pci->mem + offset + 4)`, что предотвращает зависание шины PCIe в раннем кремнии `AR1A`.
   - **`WAR_CE_SRC_RING_WRITE_IDX_SET` (`ath10k_ce_src_ring_write_index_set`):** Для кольца `CE4` (`CDC_WAR_DATA_CE`) индекс передаётся через регистр `DST_WATERMARK` (`offset + 0x50`) с маской `0xceef0000 | write_index`, а для остальных колец Copy Engine (`CE0` BMI, `CE3` WMI, `CE7` Diag) под `local_irq_save` выполняется последовательность `1 -> 2x read -> write_index -> 0`.
   - **Безопасный сброс и порядок загрузки OTP:** Исключён `warm_reset` (используется `cold_reset` через `SOC_GLOBAL_RESET_ADDRESS`), а `otp.bin` запускается строго после загрузки `board.bin` в `hi_board_data` (с резервным адресом `0x00423900`).
3. **Защита от циклической перезагрузки (`bootloop`):**
   - Встроен `/etc/sysctl.d/99-ath10k-safe.conf` (`kernel.panic_on_oops=0`, `kernel.panic=0`) и стартовый скрипт `/etc/uci-defaults/99-archer-c7-v1-5g`.

---

## Инструкция по прошивке со стоковой прошивки TP-Link

1. Подключите компьютер к LAN-порту роутера **TP-Link Archer C7 v1** кабелем (не прошивайте по Wi-Fi).
2. Откройте веб-интерфейс заводской прошивки TP-Link (обычно `http://192.168.0.1` или `http://192.168.1.1`, логин/пароль `admin` / `admin`).
3. Перейдите в раздел **System Tools -> Firmware Upgrade** (*Системные инструменты -> Обновление ПО*).
4. Выберите файл **`output/factory.bin`** (используйте именно файл с коротким именем `factory.bin`, так как старый веб-интерфейс TP-Link может отклонять длинные имена файлов) и нажмите **Upgrade**.
5. Дождитесь завершения прошивки и перезагрузки роутера (~2–3 минуты).
6. Откройте в браузере **`http://192.168.1.1`** (веб-интерфейс OpenWrt LuCI, вход `root` без пароля), перейдите в **Network -> Wireless** и включите обе точки доступа (**2.4 ГГц** и **5 ГГц** `ArcherC7v1-5G`).
