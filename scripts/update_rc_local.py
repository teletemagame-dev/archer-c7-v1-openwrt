import paramiko
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5.0)
sock.bind(('192.168.1.110', 0))
sock.connect(('192.168.1.1', 22))
t = paramiko.Transport(sock)
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

rc_local = """#!/bin/sh
# Ensure QCA9880-AR1A (hw1.0) 5GHz, 2.4GHz Wi-Fi, and AmneziaWG Split-Tunnel start on boot

(
    sysctl -w kernel.panic_on_oops=0 kernel.panic=0 >/dev/null 2>&1 || true
    
    # Wait for system to fully settle and PCIe power/clock to stabilize (25s)
    sleep 25

    if ! lsmod | grep -q '^ath10k_pci'; then
        insmod /lib/modules/*/ath10k_core.ko 2>/dev/null || modprobe ath10k_core 2>/dev/null || true
        insmod /lib/modules/*/ath10k_pci.ko 2>/dev/null || modprobe ath10k_pci 2>/dev/null || true
        sleep 5
    fi

    # Trigger wifi reload if phy0 is present
    if [ -d /sys/class/ieee80211/phy0 ]; then
        /sbin/wifi reload >/dev/null 2>&1 || true
        sleep 3
    fi

    /etc/amnezia/start_vpn.sh >/tmp/amnezia_vpn.log 2>&1 || true
    /etc/amnezia/watchdog.sh >/dev/null 2>&1 &
) &

exit 0
"""

stdin, stdout, stderr = ssh.exec_command("cat > /etc/rc.local")
stdin.write(rc_local)
stdin.channel.shutdown_write()
stdout.read()

stdin, stdout, stderr = ssh.exec_command("chmod +x /etc/rc.local; cat /etc/rc.local")
print(stdout.read().decode())
ssh.close()
