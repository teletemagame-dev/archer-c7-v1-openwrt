import paramiko
import time

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
nft delete table netdev vpn_tag 2>/dev/null || true
nft add table netdev vpn_tag
nft 'add chain netdev vpn_tag ing_lan1 { type filter hook ingress device "eth1.3" priority -100; policy accept; meta mark set 0x66 counter; }'
nft 'add chain netdev vpn_tag ing_wifi { type filter hook ingress device "wlan_vpn" priority -100; policy accept; meta mark set 0x66 counter; }'
nft insert rule inet fw4 mangle_prerouting meta mark 0x66 counter
sleep 1
nft list table netdev vpn_tag
nft list chain inet fw4 mangle_prerouting
"""

stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
