import time
import urllib.request
import socket
import ssl
from concurrent.futures import ThreadPoolExecutor

def download_chunk(url, host_ip=None, timeout=10):
    t0 = time.time()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    total = 0
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            while True:
                data = resp.read(65536)
                if not data:
                    break
                total += len(data)
                if time.time() - t0 > 6.0:
                    break
    except Exception as e:
        pass
    dt = time.time() - t0
    return total, dt

def test_multi(url, label, workers=4):
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(download_chunk, url) for _ in range(workers)]
        total_bytes = sum(f.result()[0] for f in futs)
    dt = time.time() - t0
    mbps = (total_bytes * 8) / (dt * 1_000_000)
    print(f"[{label}] Downloaded {total_bytes/1_000_000:.2f} MB in {dt:.2f}s -> {mbps:.1f} Mbps")

print("Testing Direct ISP (RU bypass) speed vs VPN (awg0) speed...")
# 1. Direct RU speed (Yandex mirror / Selectel)
test_multi("https://mirror.yandex.ru/ubuntu/ls-lR.gz", "RU Direct (mirror.yandex.ru)", workers=4)

# 2. VPN speed (Cloudflare speedtest via awg0)
test_multi("https://speed.cloudflare.com/__down?bytes=25000000", "VPN awg0 (speed.cloudflare.com)", workers=4)
