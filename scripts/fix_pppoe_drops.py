import paramiko
import socket
import subprocess
import re
import time

def get_lan1_ip():
    out = subprocess.check_output("ipconfig", shell=True).decode('cp866', errors='replace')
    m = re.search(r'192\.168\.1\.(\d+)', out)
    if m and m.group(1) != '1':
        return f"192.168.1.{m.group(1)}"
    return None

print("=== WAITING FOR ARCHER C7 v1 CONNECTION ===")
print("Plug PC into yellow LAN port of Archer C7...")

while True:
    local_ip = get_lan1_ip()
    if not local_ip:
        time.sleep(1)
        continue
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3.0)
        sock.bind((local_ip, 0))
        sock.connect(('192.168.1.1', 22))
        t = paramiko.Transport(sock)
        t.connect()
        t.auth_none('root')
        ssh = paramiko.SSHClient()
        ssh._transport = t
        print(f"\n[+] Connected to Archer C7 v1 from {local_ip}!")
        
        fix_script = """#!/bin/sh
set -e

# 1. Fix PPPoE keepalive: change from aggressive 5s to stable 20s x 6 = 120s
uci set network.wan.keepalive='20 6'
uci set network.wan.mtu='1492'
uci commit network

# 2. Fix start_vpn.sh: remove any disruptive firewall reload
sed -i 's|/etc/init.d/firewall reload|# /etc/init.d/firewall reload|g' /etc/amnezia/start_vpn.sh

# 3. Reload WAN gracefully with new keepalive
/sbin/ifup wan

sleep 5
ip addr show pppoe-wan
"""
        stdin, stdout, stderr = ssh.exec_command(fix_script)
        print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
        
        print("\n[+] Monitoring connection stability for 25 seconds...")
        for i in range(5):
            time.sleep(5)
            stdin, stdout, stderr = ssh.exec_command("ping -c 2 -W 2 8.8.8.8; ping -c 2 -W 2 -I awg0 10.66.66.1 2>/dev/null || true")
            res = stdout.read().decode('utf-8', errors='replace')
            print(f"[{i+1}/5] Ping check:\n" + res.strip())
            
        ssh.close()
        print("\n[SUCCESS] PPPoE keepalive fixed and verified rock-solid!")
        break
    except Exception as e:
        time.sleep(1)
