#!/usr/bin/env python3
"""
Servidor TCP Concorrente com Threads (Didático)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar os conceitos da Unidade 3 (04_camadas_transporte/03_servidores_concorrentes.md):
    - accept() cria um socket novo por cliente;
    - uma thread por cliente atende sem bloquear a aceitação de novos clientes;
    - um recurso compartilhado (contador de clientes atendidos) protegido por Lock,
      evitando condição de corrida entre as threads.

Comandos aceitos pelo cliente (ver tcp_echo_client_python3.py para se conectar):
    Qualquer texto -> o servidor devolve o mesmo texto (eco) e informa
                       quantos clientes já foram atendidos no total.

Execução:
    $ python3 servidor_concorrente_threads.py

Teste (em terminais separados, simultaneamente):
    $ python3 tcp_echo_client_python3.py
"""

import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

# Recurso compartilhado entre todas as threads de atendimento.
contador_clientes = 0
lock_contador = threading.Lock()


def atender_cliente(conexao, endereco):
    """Executada em uma thread própria para cada cliente conectado."""
    global contador_clientes

    with lock_contador:
        contador_clientes += 1
        numero_deste_cliente = contador_clientes

    print(f"[+] Cliente {numero_deste_cliente} conectado: {endereco}")

    try:
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break

            resposta = dados + f" (cliente #{numero_deste_cliente})".encode("utf-8")
            conexao.sendall(resposta)
    finally:
        conexao.close()
        print(f"[-] Cliente {numero_deste_cliente} desconectado: {endereco}")


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"[*] Servidor concorrente (threads) ouvindo em {HOST}:{PORT}")
    print("[*] A thread principal só aceita conexões; quem atende é sempre uma nova thread.\n")

    try:
        while True:
            conexao, endereco = servidor.accept()
            thread = threading.Thread(
                target=atender_cliente,
                args=(conexao, endereco),
                daemon=True,
            )
            thread.start()
    except KeyboardInterrupt:
        print("\n[*] Encerrando servidor...")
    finally:
        servidor.close()


if __name__ == "__main__":
    main()
