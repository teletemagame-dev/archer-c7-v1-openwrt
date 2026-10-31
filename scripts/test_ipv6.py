import socket
import time

def test_ipv6():
    print("Testing IPv6 TCP connection from PC...")
    t0 = time.time()
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.settimeout(5.0)
        # Try connecting to Google DNS IPv6 (2001:4860:4860::8888) or Cloudflare IPv6 (2606:4700:4700::1111)
        s.connect(('2606:4700:4700::1111', 53))
        dt = time.time() - t0
        print(f"IPv6 CONNECT SUCCESS in {dt*1000:.1f}ms")
        s.close()
    except Exception as e:
        dt = time.time() - t0
        print(f"IPv6 CONNECT FAILED after {dt*1000:.1f}ms: {e}")

test_ipv6()
