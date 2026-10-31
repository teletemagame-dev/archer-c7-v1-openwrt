import socket
import time

def query_dns(server, domain="ya.ru", timeout=2.0):
    # Construct standard DNS query for A record
    import random
    txid = random.randint(1, 65535)
    # Header: ID, Flags=0x0100 (standard query), QDCOUNT=1, ANCOUNT=0, NSCOUNT=0, ARCOUNT=0
    header = txid.to_bytes(2, 'big') + b'\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
    # Question
    question = b''
    for part in domain.split('.'):
        question += len(part).to_bytes(1, 'big') + part.encode('ascii')
    question += b'\x00\x00\x01\x00\x01' # QTYPE=A (1), QCLASS=IN (1)
    packet = header + question

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    s.bind(('192.168.1.110', 0))
    t0 = time.time()
    try:
        s.sendto(packet, (server, 53))
        data, addr = s.recvfrom(2048)
        dt = time.time() - t0
        s.close()
        return f"{dt*1000:.1f}ms (from {addr[0]})"
    except socket.timeout:
        s.close()
        return f"TIMEOUT (> {timeout}s)"
    except Exception as e:
        s.close()
        return f"ERR: {e}"

servers = ["192.168.1.1", "77.88.8.8", "8.8.8.8", "1.1.1.1", "1.0.0.1"]
domains = ["ya.ru", "instagram.com", "google.com", "youtube.com", "twitter.com"]

for d in domains:
    print(f"--- Domain: {d} ---")
    for srv in servers:
        ans = query_dns(srv, d)
        print(f"  {srv:<15}: {ans}")
