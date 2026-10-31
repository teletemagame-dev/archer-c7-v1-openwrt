import socket
import subprocess
import time
import paramiko

print("=== PC IPCONFIG ===")
print(subprocess.check_output("ipconfig /all", shell=True).decode("cp866", errors="replace"))

sock = socket.create_connection(("192.168.1.1", 22), timeout=5)
t = paramiko.Transport(sock)
t.start_client()
try:
    t.auth_none("root")
except Exception:
    t.auth_password("root", "")

def run_ssh(cmd):
    chan = t.open_session()
    chan.exec_command(cmd)
    out = b""
    while not chan.exit_status_ready():
        if chan.recv_ready():
            out += chan.recv(4096)
        time.sleep(0.05)
    while chan.recv_ready():
        out += chan.recv(4096)
    chan.close()
    return out.decode("utf-8", errors="replace")

print(run_ssh("""
uname -a
echo "=== UPTIME ==="
uptime
echo "=== NETWORK ==="
uci show network
echo "=== DHCP ==="
uci show dhcp
echo "=== WIRELESS ==="
uci show wireless
echo "=== IWINFO ==="
iwinfo
echo "=== PCI DEVICES ==="
for d in /sys/bus/pci/devices/*; do
    echo "$d: vendor=$(cat $d/vendor 2>/dev/null) device=$(cat $d/device 2>/dev/null) enable=$(cat $d/enable 2>/dev/null)"
done
echo "=== LSMOD ATH ==="
lsmod | grep -E 'ath|mac80211|cfg80211'
echo "=== CRASH SENTINEL ==="
ls -la /etc/ath10k* /lib/modules/*/ath10k* /etc/rc.local 2>&1
echo "=== DMESG PCI/ATH10K ==="
dmesg | grep -iE 'ath10k|pci|0000:|wlan|radio'
"""))
t.close()
