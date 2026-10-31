import socket
import time
import subprocess

def test_dns(domain, server):
    t0 = time.time()
    res = subprocess.run(["nslookup", domain, server], capture_output=True, text=True)
    dt = time.time() - t0
    print(f"[{domain} via {server}] {dt:.3f}s")
    for line in res.stdout.splitlines():
        if "Address" in line or "Name" in line or "can't find" in line:
            print("  ", line)

test_dns("instagram.com", "192.168.1.1")
test_dns("twitter.com", "192.168.1.1")
test_dns("youtube.com", "192.168.1.1")
test_dns("facebook.com", "192.168.1.1")
test_dns("rutracker.org", "192.168.1.1")
test_dns("notion.so", "192.168.1.1")
test_dns("openai.com", "192.168.1.1")
