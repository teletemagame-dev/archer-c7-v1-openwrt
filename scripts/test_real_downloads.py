import urllib.request
import time

urls = [
    ("YouTube", "https://www.youtube.com"),
    ("Google", "https://www.google.com"),
    ("Twitter", "https://twitter.com"),
    ("Instagram", "https://www.instagram.com"),
    ("ChatGPT", "https://chatgpt.com"),
    ("GitHub", "https://github.com"),
    ("Ya.ru", "https://ya.ru")
]

for name, url in urls:
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            dt = time.time() - t0
            print(f"[{name:<10}] {resp.status} OK | Size: {len(data)/1024:>6.1f} KB | Time: {dt:>5.2f}s | Speed: {len(data)*8/(dt*1_000_000):>5.2f} Mbps")
    except Exception as e:
        dt = time.time() - t0
        print(f"[{name:<10}] FAILED after {dt:.2f}s: {e}")
