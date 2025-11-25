#!/usr/bin/env python3
"""
Servidor UDP — Exemplo Didático (ECHO)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Este servidor UDP recebe datagramas de clientes e devolve
    exatamente o mesmo conteúdo (ECHO), ilustrando:

    - Criação de socket UDP
    - Funcionamento sem conexão (connectionless)
    - Recebimento via recvfrom()
    - Envio via sendto()
    - Ausência de confirmação/garantia de entrega

Como executar:
    1) Execute este servidor:
        $ python3 udp_echo_server_python3.py

    2) Em outra janela/terminal, use o cliente:
        $ python3 udp_echo_client_python3.py

    OU envie manualmente:
        $ echo "teste" | nc -u 127.0.0.1 6000

Relação com o estudo:
    Demonstra as características do UDP:
        - Sem conexão
        - Sem confiabilidade
        - Sem controle de fluxo
        - Sem garantia de chegada
"""

import socket

HOST = "0.0.0.0"
PORT = 6000


def main():
    # Criação do socket UDP (SOCK_DGRAM)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Associação à porta local
    servidor.bind((HOST, PORT))

    print(f"[*] Servidor UDP iniciado em {HOST}:{PORT}")
    print("[*] Aguardando datagramas...\n")

    while True:
        # Recebe datagrama e endereço de origem
        dados, endereco = servidor.recvfrom(1024)

        print(f"[Recebido de {endereco}]: {dados.decode().strip()}")

        # Envia de volta (ECHO)
        servidor.sendto(dados, endereco)


if __name__ == "__main__":
    main()
