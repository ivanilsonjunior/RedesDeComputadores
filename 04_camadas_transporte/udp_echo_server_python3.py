#!/usr/bin/env python3
"""
Servidor UDP (Camada de Transporte)

Objetivo didático:
    - Demonstrar comunicação sem conexão (connectionless).
    - Mostrar a ausência de confiabilidade no UDP.
    - Comparar com o servidor TCP.

Execução:
    $ python3 udp_echo_server_python3.py
"""

import socket

HOST = "0.0.0.0"
PORT = 5001

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    print(f"[+] Servidor UDP escutando em {HOST}:{PORT}")

    while True:
        dados, endereco = sock.recvfrom(1024)
        mensagem = dados.decode().strip()

        print(f"[>] Recebido de {endereco}: {mensagem}")

        # Envia o mesmo pacote de volta
        sock.sendto(dados, endereco)


if __name__ == "__main__":
    main()
