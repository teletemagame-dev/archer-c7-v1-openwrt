import paramiko
import socket
import urllib.request

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
ps | grep dnsmasq
netstat -ulpn | grep :53 || ss -ulpn | grep :53
nft list chain inet fw4 mangle_prerouting
nft list chain inet fw4 dstnat
awg show
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print("=== ROUTER STATE ===")
print(stdout.read().decode('utf-8', errors='replace'))
print(stderr.read().decode('utf-8', errors='replace'))
ssh.close()
