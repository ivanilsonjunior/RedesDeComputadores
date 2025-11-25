#!/usr/bin/env python3
"""
Cliente UDP (Camada de Transporte)

Objetivo didático:
    - Enviar datagramas para um servidor UDP.
    - Mostrar que não existe confirmação de entrega automática.
    - Comparar com o cliente TCP.

Execução:
    $ python3 udp_echo_client_python3.py
"""

import socket

SERVIDOR = "127.0.0.1"
PORTA = 5001

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input("> ")
        if msg.lower() == "sair":
            break

        sock.sendto(msg.encode(), (SERVIDOR, PORTA))
        dados, _ = sock.recvfrom(1024)
        print("[<] Eco:", dados.decode().strip())


if __name__ == "__main__":
    main()
