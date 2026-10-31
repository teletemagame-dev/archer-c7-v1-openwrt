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
rmmod ath10k_pci 2>/dev/null || true
rmmod ath10k_core 2>/dev/null || true
sleep 1
insmod /lib/modules/5.15.167/ath10k_core.ko
insmod /lib/modules/5.15.167/ath10k_pci.ko
sleep 3
dmesg | grep -i ath10k | tail -n 20
ls -la /sys/class/ieee80211/
/sbin/wifi reload
sleep 3
iwinfo
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
