#!/usr/bin/env python3
"""
Ping simplificado usando socket UDP

Objetivo didático:
    - Simular a lógica do ping (envia pacote e mede tempo).
    - Não utiliza ICMP cru (necessita root).
    - Serve para explicar latência e RTT.
"""

import socket
import time

HOST = "8.8.8.8"
PORT = 33434  # porta arbitrária (como no traceroute)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    inicio = time.time()
    sock.sendto(b"teste", (HOST, PORT))

    try:
        sock.recvfrom(1024)
    except:
        pass

    fim = time.time()
    print(f"RTT aproximado: { (fim - inicio)*1000:.2f} ms")


if __name__ == "__main__":
    main()
