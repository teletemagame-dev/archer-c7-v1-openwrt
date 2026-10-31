import socket
import ssl
import http.client
import subprocess
import paramiko

def fetch_via_lan1(host, path="/", use_https=True, port=None):
    # Resolve via router DNS (192.168.1.1) or system DNS bound to 192.168.1.110
    ip = socket.gethostbyname(host)
    if port is None:
        port = 443 if use_https else 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(8)
    s.bind(('192.168.1.110', 0))
    s.connect((ip, port))
    if use_https:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(s, server_hostname=host)
    req = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: curl/8.0\r\nConnection: close\r\n\r\n"
    s.sendall(req.encode())
    resp = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        resp += chunk
    s.close()
    header, _, body = resp.partition(b"\r\n\r\n")
    status_line = header.split(b"\r\n")[0].decode('utf-8', errors='replace')
    return ip, status_line, body.decode('utf-8', errors='replace').strip()[:200]

print("1. Testing International IP check via LAN 1 (api.ipify.org -> should be 203.0.113.1 VPN):")
ip, status, body = fetch_via_lan1("api.ipify.org", "/")
print(f"   api.ipify.org ({ip}) -> {status} | External IP: {body}")

print("\n2. Testing International IP check via LAN 1 (ifconfig.me -> should be 203.0.113.1 VPN):")
ip, status, body = fetch_via_lan1("ifconfig.me", "/ip")
print(f"   ifconfig.me ({ip}) -> {status} | External IP: {body}")

print("\n3. Testing International site via LAN 1 (www.google.com):")
ip, status, body = fetch_via_lan1("www.google.com", "/")
print(f"   www.google.com ({ip}) -> {status}")

print("\n4. Testing .ru domain via LAN 1 (ya.ru -> should bypass VPN):")
ip, status, body = fetch_via_lan1("ya.ru", "/")
print(f"   ya.ru ({ip}) -> {status}")

print("\n5. Testing Russian IP check service (icanhazip.com vs 2ip / yandex internetometer):")
ip, status, body = fetch_via_lan1("yandex.ru", "/internet/")
print(f"   yandex.ru/internet ({ip}) -> {status}")

print("\n6. Testing Steam (store.steampowered.com -> should bypass VPN & populate @vpn_bypass_dyn):")
ip, status, body = fetch_via_lan1("store.steampowered.com", "/")
print(f"   store.steampowered.com ({ip}) -> {status}")

# Check router nftables @vpn_bypass_dyn and awg0 counters
t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t
stdin, stdout, stderr = ssh.exec_command("nft list set inet fw4 vpn_bypass_dyn; awg show")
print("\n=== ROUTER @vpn_bypass_dyn & AWG0 ===")
print(stdout.read().decode('utf-8', errors='replace'))
ssh.close()
