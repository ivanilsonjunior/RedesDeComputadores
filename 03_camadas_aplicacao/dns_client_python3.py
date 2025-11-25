#!/usr/bin/env python3
"""
Cliente DNS simples (UDP)

Objetivo didático:
    - Construir um pacote DNS manualmente.
    - Enviar via UDP para um resolvedor DNS.
    - Mostrar como funciona a camada de aplicação sobre UDP.

Limitações:
    - Consulta tipo A (IPv4)
    - Sem suporte a múltiplas respostas ou compressão de nomes
"""

import socket
import random

DNS_SERVER = "8.8.8.8"
DNS_PORT = 53

def montar_consulta(nome):
    tid = random.randint(0, 65535)
    flags = 0x0100  # consulta recursiva
    qdcount = 1

    header = tid.to_bytes(2, "big") + flags.to_bytes(2, "big")
    header += qdcount.to_bytes(2, "big") + b"\x00\x00\x00\x00"

    body = b""
    for parte in nome.split("."):
        body += bytes([len(parte)]) + parte.encode()
    body += b"\x00"      # fim do nome
    body += b"\x00\x01"  # tipo A
    body += b"\x00\x01"  # classe IN

    return header + body, tid

def main():
    dominio = "google.com"
    pacote, tid = montar_consulta(dominio)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(pacote, (DNS_SERVER, DNS_PORT))

    print("[*] Enviando consulta DNS para", dominio)
    resposta, _ = sock.recvfrom(512)

    print("[*] Resposta bruta:\n", resposta.hex())


if __name__ == "__main__":
    main()
