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

print("Ready! Waiting for you to plug PC and ISP cables into Archer C7 v1...")
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
        print(f"=== CONNECTED TO ARCHER C7 v1 ({local_ip}) ===")
        
        stdin, stdout, stderr = ssh.exec_command("""
        echo "--- 1. Wi-Fi Status ---"
        iwinfo | grep -E 'ESSID|Channel|Tx-Power'
        echo "--- 2. WAN Cable & PPPoE Link ---"
        swconfig dev switch0 port 1 get link
        ip addr show pppoe-wan 2>/dev/null || echo "PPPoE not connected yet"
        echo "--- 3. Running start_vpn.sh ---"
        /etc/amnezia/start_vpn.sh
        echo "--- 4. Tunnel & Routing Status ---"
        awg show
        ip rule show
        echo "--- 5. Internet Connectivity Check ---"
        ping -c 2 -W 2 8.8.8.8 2>&1 || true
        ping -c 2 -W 2 -I awg0 10.66.66.1 2>&1 || true
        """)
        out = stdout.read().decode('utf-8', errors='replace')
        print(out)
        ssh.close()
        break
    except Exception as e:
        time.sleep(1)
