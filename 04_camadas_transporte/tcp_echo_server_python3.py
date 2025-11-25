#!/usr/bin/env python3
"""
Servidor TCP — Exemplo Didático (ECHO)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Este script implementa um servidor TCP simples, do tipo ECHO,
    que devolve ao cliente tudo o que ele enviar. Ele demonstra:

    - Criação de socket TCP
    - Associação (bind) a IP/porta
    - Modo de escuta (listen)
    - Aceitar conexões (accept)
    - Envio e recebimento de dados
    - Fechamento correto da conexão

Como executar:
    1) Execute este script:
        $ python3 tcp_echo_server_python3.py

    2) Em outra janela/terminal, conecte com:
        $ telnet localhost 5000
    OU
        $ nc localhost 5000

    3) Digite qualquer mensagem — o servidor irá devolver.

Relação com o conteúdo:
    Este código representa EXACTAMENTE o papel da Camada de Transporte:
    - uso do TCP
    - comunicação confiável
    - stream orientado a conexão
    - controle de fluxo
    - ausência de perdas (em tese)
"""

import socket

HOST = "0.0.0.0"   # Escuta em todos os endereços locais
PORT = 5000        # Porta de demonstração (padrão para laboratório)


def main():
    # Criação do socket TCP (SOCK_STREAM)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reusar rapidamente a porta após reiniciar o servidor
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print(f"[*] Iniciando servidor TCP em {HOST}:{PORT} ...")

    # Associação do socket a IP/porta
    servidor.bind((HOST, PORT))

    # Coloca o socket em modo de escuta (máximo de 5 clientes na fila)
    servidor.listen(5)
    print("[*] Servidor TCP em modo de escuta. Aguardando conexões...\n")

    while True:
        # Aceita conexão de um cliente
        conexao, endereco = servidor.accept()
        print(f"[+] Cliente conectado: {endereco}")

        # Loop para comunicação com o cliente
        while True:
            dados = conexao.recv(1024)   # Aguarda dados (até 1024 bytes)

            if not dados:
                # Cliente desconectou
                print(f"[-] Cliente desconectado: {endereco}\n")
                break

            print(f"[Recebido de {endereco}]: {dados.decode().strip()}")

            # Envia de volta o que recebeu (ECHO)
            conexao.sendall(dados)

        # Fecha socket do cliente
        conexao.close()


if __name__ == "__main__":
    main()
