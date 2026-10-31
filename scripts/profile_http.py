import socket
import ssl
import time
import urllib.request

sites = [
    "https://www.google.com",
    "https://api.ipify.org",
    "https://instagram.com",
    "https://twitter.com",
    "https://youtube.com",
    "https://github.com",
    "https://ya.ru"
]

def profile_url(url):
    parsed = urllib.parse.urlparse(url)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    
    # 1. DNS
    t0 = time.time()
    try:
        ip = socket.gethostbyname(host)
    except Exception as e:
        print(f"[{host}] DNS ERROR: {e}")
        return
    t_dns = time.time() - t0
    
    # 2. TCP connect
    t0 = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(6.0)
    s.bind(('192.168.1.110', 0))
    try:
        s.connect((ip, port))
    except Exception as e:
        print(f"[{host} ({ip})] TCP CONNECT ERROR: {e}")
        s.close()
        return
    t_tcp = time.time() - t0
    
    # 3. TLS Handshake
    t0 = time.time()
    if parsed.scheme == "https":
        ctx = ssl.create_default_context()
        try:
            ss = ctx.wrap_socket(s, server_hostname=host)
        except Exception as e:
            print(f"[{host} ({ip})] TLS HANDSHAKE ERROR: {e}")
            s.close()
            return
    else:
        ss = s
    t_tls = time.time() - t0
    
    # 4. HTTP GET and TTFB
    t0 = time.time()
    req = f"GET {parsed.path or '/'} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n"
    ss.sendall(req.encode())
    first_byte = ss.recv(1)
    t_ttfb = time.time() - t0
    
    # Rest of response
    body = first_byte
    while True:
        try:
            chunk = ss.recv(4096)
            if not chunk:
                break
            body += chunk
        except Exception:
            break
    ss.close()
    t_total = t_dns + t_tcp + t_tls + t_ttfb
    print(f"[{host:<22}] DNS: {t_dns*1000:>5.1f}ms | TCP: {t_tcp*1000:>5.1f}ms | TLS: {t_tls*1000:>5.1f}ms | TTFB: {t_ttfb*1000:>5.1f}ms | Total: {t_total*1000:>5.1f}ms | Size: {len(body)} bytes")

import urllib.parse
for site in sites:
    profile_url(site)
