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

print("Listening for Archer C7 v1 (192.168.1.1)...")
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
        print(f"Connected to 192.168.1.1 from {local_ip}!")
        
        stdin, stdout, stderr = ssh.exec_command("""
        echo "=== WI-FI STATUS ==="
        iwinfo
        echo "=== AWG0 STATUS ==="
        awg show
        echo "=== IP RULES ==="
        ip rule show
        echo "=== WAN PING ==="
        ping -c 2 -W 2 8.8.8.8
        echo "=== VPN PING ==="
        ping -c 2 -W 2 -I awg0 10.66.66.1 2>&1 || true
        """)
        print(stdout.read().decode('utf-8', errors='replace'))
        ssh.close()
        break
    except Exception as e:
        time.sleep(1)
