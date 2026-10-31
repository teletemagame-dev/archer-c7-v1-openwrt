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
sed -i 's/nft list sets inet fw4/nft list sets/g' /etc/amnezia/start_vpn.sh
ip addr show pppoe-wan 2>&1 || true
awg show
ip rule show
ping -c 2 -W 2 10.66.66.1 2>&1 || true
logread | grep amnezia | tail -n 10
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
