#!/usr/bin/env python3
"""
Cliente UDP — Exemplo Didático (ECHO)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar um cliente UDP simples que envia datagramas para um
    servidor ECHO e recebe a resposta. Ilustra:

        - Uso de sockets UDP (SOCK_DGRAM)
        - Envio sem conexão (sendto)
        - Recebimento via recvfrom
        - Possibilidade de perda de pacotes
        - Ausência de retransmissão (responsabilidade da aplicação)

Como executar:
    1) Certifique-se de que o servidor UDP está rodando:
        $ python3 udp_echo_server_python3.py

    2) Execute este cliente:
        $ python3 udp_echo_client_python3.py

    3) Digite mensagens e veja o retorno.
"""

import socket

HOST = "127.0.0.1"   # Servidor (localhost)
PORT = 6000          # Mesma porta do servidor


def main():

    # Criação do socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"[*] Cliente UDP iniciado. Enviando mensagens para {HOST}:{PORT}\n")

    try:
        while True:
            mensagem = input("Digite uma mensagem (ou 'sair'): ")

            if mensagem.lower() == "sair":
                break

            # Envia datagrama
            sock.sendto(mensagem.encode(), (HOST, PORT))

            # Tenta receber resposta do servidor
            try:
                sock.settimeout(2)  # UDP pode perder pacotes
                dados, _ = sock.recvfrom(1024)
                print(f"[ECHO] {dados.decode().strip()}\n")
            except socket.timeout:
                print("[-] Resposta não recebida (possível perda de pacote)\n")

    except KeyboardInterrupt:
        print("\n[-] Cliente interrompido pelo usuário.")

    finally:
        sock.close()
        print("[*] Cliente finalizado.")


if __name__ == "__main__":
    main()
