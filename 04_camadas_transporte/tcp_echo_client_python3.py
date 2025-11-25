#!/usr/bin/env python3
"""
Cliente de eco TCP (Camada de Transporte)

Objetivo didático:
    - Demonstrar como um cliente se conecta a um servidor TCP.
    - Enviar dados e receber a resposta de volta.
"""

import socket

SERVIDOR = "127.0.0.1"  # Endereço do servidor (localhost)
PORTA = 5000            # Porta TCP do servidor de eco


def main() -> None:
    """Função principal do cliente de eco TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print(f"[*] Conectando a {SERVIDOR}:{PORTA}...")
        sock.connect((SERVIDOR, PORTA))
        print("[+] Conectado! Digite mensagens (ou 'sair' para encerrar).")

        while True:
            msg = input("> ")
            if msg.lower() == "sair":
                print("[*] Encerrando cliente.")
                break

            sock.sendall((msg + "\n").encode("utf-8"))
            dados = sock.recv(1024)
            print(f"[<] Resposta do servidor: {dados.decode('utf-8').strip()}")


if __name__ == "__main__":
    main()
