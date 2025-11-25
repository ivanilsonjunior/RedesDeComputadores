#!/usr/bin/env python3
"""
Cliente TCP (Camada de Transporte)

Objetivo didático:
    - Conectar-se a um servidor TCP.
    - Enviar mensagens e aguardar a resposta.
    - Demonstrar como funciona o fluxo confiável do TCP.

Execução:
    $ python3 tcp_echo_client_python3.py
"""

import socket

SERVIDOR = "127.0.0.1"
PORTA = 5000

def main():
    # Cria socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[*] Conectando a {SERVIDOR}:{PORTA}...")
    sock.connect((SERVIDOR, PORTA))
    print("[+] Conectado! Digite mensagens.\n")

    while True:
        msg = input("> ")
        if msg.lower() == "sair":
            print("[*] Cliente encerrado.")
            break

        sock.sendall((msg + "\n").encode())
        resposta = sock.recv(1024)
        print("[<] Resposta:", resposta.decode().strip())

    sock.close()


if __name__ == "__main__":
    main()
