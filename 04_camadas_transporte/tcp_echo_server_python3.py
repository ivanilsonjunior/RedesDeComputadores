#!/usr/bin/env python3
"""
Servidor de eco TCP (Camada de Transporte)

Objetivo didático:
    - Demonstrar o funcionamento básico do TCP.
    - Mostrar a ideia de porta, conexão e fluxo confiável.
    - A cada mensagem recebida, o servidor devolve (eco) a mesma mensagem.

Como usar:
    1. Execute este servidor:
        $ python3 tcp_echo_server_python3.py
    2. Em outro terminal, use o cliente:
        $ python3 tcp_echo_client_python3.py
    3. Digite mensagens no cliente e observe o comportamento.
"""

import socket

HOST = "0.0.0.0"   # Escuta em todas as interfaces
PORT = 5000        # Porta TCP escolhida para o serviço de eco


def main() -> None:
    """Função principal do servidor de eco TCP."""
    # Cria o socket TCP (SOCK_STREAM)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reuso rápido da porta após encerrar o servidor
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Associa o socket ao endereço e porta
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"[*] Servidor de eco TCP escutando em {HOST}:{PORT}")

    while True:
        print("[*] Aguardando conexão de um cliente...")
        conexao, endereco = servidor.accept()
        print(f"[+] Cliente conectado: {endereco}")

        # Usa o with para garantir fechamento da conexão
        with conexao:
            while True:
                dados = conexao.recv(1024)
                if not dados:
                    print(f"[-] Cliente {endereco} encerrou a conexão.")
                    break

                mensagem = dados.decode("utf-8").strip()
                print(f"[>] Recebido de {endereco}: {mensagem}")

                resposta = f"ECO: {mensagem}\n"
                conexao.sendall(resposta.encode("utf-8"))


if __name__ == "__main__":
    main()
