#!/usr/bin/env python3
"""
Demonstração de UNICAST em Python
Envio 1→1 usando UDP.
DIATINF — IFRN
"""

import socket

def servidor_unicast():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", 5000))
    print("Servidor UNICAST aguardando em 0.0.0.0:5000...")
    while True:
        dados, addr = s.recvfrom(1024)
        print(f"[UNICAST] Recebido de {addr}: {dados.decode()}")

def cliente_unicast(destino="127.0.0.1"):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "Mensagem UNICAST"
    s.sendto(msg.encode(), (destino, 5000))
    print("Enviado:", msg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "cliente":
        cliente_unicast()
    else:
        servidor_unicast()
