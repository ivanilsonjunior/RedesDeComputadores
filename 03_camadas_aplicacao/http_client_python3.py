#!/usr/bin/env python3
"""
Cliente HTTP simples (Camada de Aplicação)

Objetivo didático:
    - Demonstrar como funciona um GET HTTP "manual".
    - Usar sockets para enviar e receber dados formatados em HTTP.
    - Explicar como funciona a camada de aplicação sobre TCP.

Este código se conecta a um servidor HTTP na porta 80
e solicita o recurso "/" (página inicial).
"""

import socket

HOST = "example.com"
PORT = 80

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[*] Conectando a {HOST}:{PORT}")
        s.connect((HOST, PORT))

        requisicao = (
            "GET / HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            "Connection: close\r\n\r\n"
        )

        print("[*] Enviando requisição HTTP...")
        s.sendall(requisicao.encode())

        resposta = b""
        while True:
            dados = s.recv(4096)
            if not dados:
                break
            resposta += dados

    print("[*] Resposta completa recebida:\n")
    print(resposta.decode(errors="ignore"))


if __name__ == "__main__":
    main()
