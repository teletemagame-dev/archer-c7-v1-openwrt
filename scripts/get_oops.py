import socket
import time
import paramiko

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
echo "=== MODULE SECTIONS ==="
head -n 20 /sys/module/ath10k_pci/sections/.text /sys/module/ath10k_core/sections/.text 2>&1
echo "=== FULL DMESG FROM 110s ==="
dmesg | awk '/\\[  11[0-9]\\./,0'
echo "=== RC.LOCAL ==="
cat /etc/rc.local
echo "=== RESOLV.CONF & DNSMASQ ==="
head -n 50 /etc/resolv.conf /tmp/resolv.conf* /var/etc/dnsmasq.conf.* 2>&1
"""))
t.close()
