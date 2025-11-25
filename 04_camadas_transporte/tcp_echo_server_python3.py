#!/usr/bin/env python3
"""
Servidor de Eco TCP (Camada de Transporte)

Objetivo didático:
    Este código demonstra:
    - Como criar um socket TCP.
    - Como o servidor aceita conexões (three-way handshake).
    - Como é o fluxo de envio/recebimento de dados.
    - Conceitos fundamentais como porta, conexão, fluxo e eco.

Como executar:
    $ python3 tcp_echo_server_python3.py

Relação com o modelo TCP/IP:
    Aplicação    → sua lógica (eco)
    Transporte   → TCP (este script)
    Rede         → IP (camada inferior)
"""

import socket

HOST = "0.0.0.0"
PORT = 5000

def main():
    # Cria o socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reusar a porta rapidamente
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Associa o socket ao endereço e porta
    servidor.bind((HOST, PORT))

    # Coloca o socket em modo de escuta (aguardando clientes)
    servidor.listen()

    print(f"Servidor TCP escutando em {HOST}:{PORT}")

    while True:
        # Aguarda um cliente
        conexao, endereco = servidor.accept()
        print(f"[+] Cliente conectado: {endereco}")

        with conexao:
            # Loop para comunicação
            while True:
                dados = conexao.recv(1024)

                # Sem dados = cliente encerrou
                if not dados:
                    print("[-] Cliente desconectou.")
                    break

                mensagem = dados.decode().strip()
                print(f"Recebido: {mensagem}")

                resposta = f"ECO: {mensagem}\n"
                conexao.sendall(resposta.encode())


if __name__ == "__main__":
    main()