import paramiko
import socket
import time

# 1. Check VPS tcpdump on port 51820 while router sends handshake
vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('203.0.113.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5.0)
sock.bind(('192.168.1.110', 0))
sock.connect(('192.168.1.1', 22))
t = paramiko.Transport(sock)
t.connect()
t.auth_none('root')
rtr = paramiko.SSHClient()
rtr._transport = t

# Start 4s tcpdump on VPS
_, v_out, v_err = vps.exec_command("timeout 4 tcpdump -ni eth0 -vvv udp port 51820 2>&1")
time.sleep(0.5)
# Trigger handshake from router
_, r_out, r_err = rtr.exec_command("ping -c 2 -W 1 -I awg0 10.66.66.1; ping -c 1 -W 1 203.0.113.1")
print("=== ROUTER PING ===")
print(r_out.read().decode())
print("=== VPS TCPDUMP ===")
print(v_out.read().decode())

rtr.close()
vps.close()
