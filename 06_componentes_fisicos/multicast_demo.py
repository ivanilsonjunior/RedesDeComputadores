#!/usr/bin/env python3
"""
Demonstração de MULTICAST em Python
Envio 1→grupo usando UDP + IGMP.
DIATINF — IFRN
"""

import socket
import struct

GRUPO = "224.1.1.1"
PORTA = 3000

def servidor_multicast():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", PORTA))

    mreq = struct.pack("4sl", socket.inet_aton(GRUPO), socket.INADDR_ANY)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(f"Servidor MULTICAST ouvindo no grupo {GRUPO}:{PORTA}...")
    while True:
        dados, addr = s.recvfrom(1024)
        print(f"[MULTICAST] Mensagem de {addr}: {dados.decode()}")

def cliente_multicast():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    msg = "Mensagem MULTICAST"
    s.sendto(msg.encode(), (GRUPO, PORTA))
    print("Enviado:", msg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "cliente":
        cliente_multicast()
    else:
        servidor_multicast()
