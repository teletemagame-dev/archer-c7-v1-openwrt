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

cmd = """
if ! grep -q "ip dscp set cs0" /etc/amnezia/watchdog.sh; then
    sed -i '/sleep 12/a \\    nft list chain inet fw4 mangle_postrouting 2>/dev/null | grep -q "203.0.113.1" || nft add rule inet fw4 mangle_postrouting ip daddr 203.0.113.1 ip dscp set cs0 2>/dev/null || true' /etc/amnezia/watchdog.sh
fi
for pid in $(ps | grep 'watchdog\\.sh' | grep -v grep | awk '{print $1}'); do
    kill -9 $pid 2>/dev/null || true
done
rmdir /var/run/amnezia_watchdog.lock 2>/dev/null || true
/etc/amnezia/watchdog.sh >/dev/null 2>&1 &
sleep 1
ps | grep -E 'dnsmasq|watchdog'
nft list chain inet fw4 mangle_postrouting
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
