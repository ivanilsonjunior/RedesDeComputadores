#!/usr/bin/env python3
"""
Cliente TCP — Exemplo Didático (ECHO)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Este script implementa um cliente TCP que se conecta ao servidor
    ECHO e envia mensagens digitadas pelo usuário. Para cada mensagem
    enviada, o servidor devolve exatamente o mesmo conteúdo.

    Demonstra:
        - Criação de socket TCP
        - Conexão (connect) ao servidor
        - Envio (sendall) e recebimento (recv)
        - Fechamento ordenado

Como executar:
    1) Garanta que o servidor esteja rodando:
        $ python3 tcp_echo_server_python3.py

    2) Execute este cliente:
        $ python3 tcp_echo_client_python3.py

    3) Digite mensagens e observe o retorno (ECHO).

Relação com o estudo:
    Mostra a interação entre cliente/servidor na Camada de Transporte:
    - conexão orientada a fluxo
    - confiabilidade
    - envio/recebimento estruturado
"""

import socket

HOST = "127.0.0.1"   # Endereço do servidor
PORT = 5000          # Mesma porta definida no servidor


def main():

    # Criação do socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[*] Conectando ao servidor TCP {HOST}:{PORT} ...")
    sock.connect((HOST, PORT))
    print("[+] Conectado!\n")

    try:
        while True:
            mensagem = input("Digite uma mensagem (ou 'sair'): ")

            if mensagem.lower() == "sair":
                break

            # Envia mensagem ao servidor
            sock.sendall(mensagem.encode())

            # Aguarda resposta
            resposta = sock.recv(1024)

            print(f"[ECHO] {resposta.decode().strip()}\n")

    except KeyboardInterrupt:
        print("\n[-] Cliente encerrado pelo usuário.")

    finally:
        sock.close()
        print("[*] Conexão fechada.")


if __name__ == "__main__":
    main()
