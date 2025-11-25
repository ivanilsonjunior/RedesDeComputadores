#!/usr/bin/env python3
"""
Demonstração de BROADCAST em Python
Envio 1→todos usando UDP.
DIATINF — IFRN
"""

import socket

def servidor_broadcast():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(("0.0.0.0", 4000))
    print("Servidor BROADCAST aguardando em 0.0.0.0:4000...")
    while True:
        dados, addr = s.recvfrom(1024)
        print(f"[BROADCAST] Recebido de {addr}: {dados.decode()}")

def cliente_broadcast():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    msg = "Mensagem BROADCAST"
    s.sendto(msg.encode(), ("255.255.255.255", 4000))
    print("Enviado:", msg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "cliente":
        cliente_broadcast()
    else:
        servidor_broadcast()
