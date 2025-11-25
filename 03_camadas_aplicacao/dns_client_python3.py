#!/usr/bin/env python3
"""
Cliente DNS simples (Didático)
Camada de Aplicação — Redes de Computadores / ADS

Objetivo:
    - Demonstrar consulta DNS manual via UDP.
    - Montar um pacote DNS simples (tipo A).
    - Explicar a estrutura do protocolo na prática.

Execução:
    $ python3 dns_client_python3.py
"""

import socket
import random

DNS_SERVER = "8.8.8.8"     # Servidor DNS do Google
DNS_PORT = 53              # Porta padrão DNS
DOMINIO = "google.com"     # Domínio para consulta

def montar_pacote_dns(dominio):
    """
    Monta um pacote DNS simples:
    - ID aleatório
    - Flags: consulta recursiva
    - QDCOUNT = 1
    - Nome do domínio codificado
    - Tipo A (0x0001)
    - Classe IN (0x0001)
    """

    # ID aleatório
    tid = random.randint(0, 65535)

    # Cabeçalho DNS (12 bytes)
    flags = 0x0100            # Consulta padrão, recursiva
    qdcount = 1               # 1 pergunta
    ancount = 0
    nscount = 0
    arcount = 0

    header = (
        tid.to_bytes(2, "big") +
        flags.to_bytes(2, "big") +
        qdcount.to_bytes(2, "big") +
        ancount.to_bytes(2, "big") +
        nscount.to_bytes(2, "big") +
        arcount.to_bytes(2, "big")
    )

    # Corpo da consulta
    body = b""
    for parte in dominio.split("."):
        body += bytes([len(parte)])
        body += parte.encode()

    body += b"\x00"          # Fim do nome
    body += b"\x00\x01"      # Tipo A
    body += b"\x00\x01"      # Classe IN

    return tid, header + body


def main():
    tid, pacote = montar_pacote_dns(DOMINIO)

    # Criar socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    print(f"[*] Enviando consulta DNS para {DNS_SERVER}: {DOMINIO}")
    sock.sendto(pacote, (DNS_SERVER, DNS_PORT))

    try:
        resposta, _ = sock.recvfrom(512)
        print("[+] Resposta recebida!\n")

        print("Resposta bruta (hex):")
        print(resposta.hex())

    except socket.timeout:
        print("[-] Tempo de resposta esgotado!")

    sock.close()


if __name__ == "__main__":
    main()
