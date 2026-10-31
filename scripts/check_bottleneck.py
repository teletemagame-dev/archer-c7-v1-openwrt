import paramiko
import threading
import time
import urllib.request

# 1. Check VPS own network speed
vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('10.66.66.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("curl -s -w 'VPS Speed: %{speed_download} bytes/sec\\n' -o /dev/null 'https://speed.cloudflare.com/__down?bytes=50000000'")
vps_out = stdout.read().decode().strip()
vps_bps = float(vps_out.split(':')[1].split()[0])
print(f"1. VPS Own Download Speed: {vps_bps * 8 / 1_000_000:.1f} Mbps")
vps.close()

# 2. Check Router CPU usage during awg0 download
t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
rtr = paramiko.SSHClient()
rtr._transport = t

stop_flag = False
def load_vpn():
    while not stop_flag:
        try:
            req = urllib.request.Request("https://speed.cloudflare.com/__down?bytes=25000000", headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=6) as r:
                while not stop_flag and r.read(65536):
                    pass
        except Exception:
            break

threads = [threading.Thread(target=load_vpn) for _ in range(4)]
for th in threads:
    th.start()

time.sleep(2)
stdin, stdout, stderr = rtr.exec_command("top -b -n 1 | head -n 20")
print("2. Router CPU during VPN download:")
print(stdout.read().decode())
stop_flag = True
rtr.close()
