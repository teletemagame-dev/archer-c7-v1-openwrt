import socket
import struct

def parse_dns_response(server, domain):
    import random
    txid = random.randint(1, 65535)
    header = txid.to_bytes(2, 'big') + b'\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
    question = b''
    for part in domain.split('.'):
        question += len(part).to_bytes(1, 'big') + part.encode('ascii')
    question += b'\x00\x00\x01\x00\x01'
    packet = header + question

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2.0)
    s.bind(('192.168.1.110', 0))
    s.sendto(packet, (server, 53))
    data, addr = s.recvfrom(2048)
    s.close()

    # parse answers
    ancount = int.from_bytes(data[6:8], 'big')
    # skip question
    idx = 12
    while data[idx] != 0:
        idx += 1 + data[idx]
    idx += 5 # skip 00, qtype, qclass
    ips = []
    for _ in range(ancount):
        if idx >= len(data):
            break
        # name pointer or label
        if (data[idx] & 0xc0) == 0xc0:
            idx += 2
        else:
            while data[idx] != 0:
                idx += 1 + data[idx]
            idx += 1
        rtype, rclass, ttl, rdlen = struct.unpack('>HHIH', data[idx:idx+10])
        idx += 10
        if rtype == 1 and rdlen == 4:
            ip = socket.inet_ntoa(data[idx:idx+4])
            ips.append(ip)
        idx += rdlen
    return ips

for d in ["instagram.com", "twitter.com", "rutracker.org", "store.steampowered.com", "ya.ru"]:
    ips = parse_dns_response("192.168.1.1", d)
    print(f"{d:<25} -> {ips}")
