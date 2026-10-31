import socket
import urllib.request
import time

def test_url(url):
    print(f"Testing {url}...")
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=6) as r:
            data = r.read(1024)
            print(f"  SUCCESS in {time.time()-t0:.2f}s, status: {r.status}, read {len(data)} bytes")
    except Exception as e:
        print(f"  FAILED in {time.time()-t0:.2f}s: {e}")

test_url("https://www.speedtest.net")
test_url("https://speedtest.net")
print("DNS www.speedtest.net:", socket.gethostbyname("www.speedtest.net"))
