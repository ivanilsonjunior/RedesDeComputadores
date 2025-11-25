#!/usr/bin/env python3
"""
ICMP PING — Exemplo Didático com Raw Sockets
Camada de Rede — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar o funcionamento do protocolo ICMP na prática.
    O script envia ICMP Echo Request e aguarda Echo Reply.

Importante:
    Raw sockets exigem privilégios administrativos.
    Execute com:
        sudo python3 icmp_ping_python3.py

Conceitos reforçados:
    - ICMP Echo Request (tipo 8)
    - ICMP Echo Reply (tipo 0)
    - Cálculo de checksum
    - TTL, tempo de resposta (RTT)
    - Encapsulamento ICMP → IP

Uso:
    $ sudo python3 icmp_ping_python3.py
    Host: 8.8.8.8
"""

import socket
import os
import struct
import time


def checksum(dados):
    """
    Cálculo de checksum para ICMP (RFC 1071).
    Soma de 16 bits + complemento de 1.
    """
    soma = 0
    tamanho = len(dados)
    i = 0

    while tamanho > 1:
        soma += (dados[i] << 8) + dados[i + 1]
        i += 2
        tamanho -= 2

    if tamanho > 0:
        soma += dados[i] << 8

    soma = (soma >> 16) + (soma & 0xFFFF)
    soma += (soma >> 16)

    return ~soma & 0xFFFF


def criar_pacote_icmp(seq=1):
    tipo = 8        # Echo Request
    codigo = 0
    identificador = os.getpid() & 0xFFFF

    cabecalho = struct.pack("!BBHHH", tipo, codigo, 0, identificador, seq)
    carga = b"IFRN_DIATINF_REDES"

    chksum = checksum(cabecalho + carga)
    cabecalho = struct.pack("!BBHHH", tipo, codigo, chksum, identificador, seq)

    return cabecalho + carga


def ping(host, seq):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    pacote = criar_pacote_icmp(seq)

    inicio = time.time()
    sock.sendto(pacote, (host, 1))

    sock.settimeout(2)

    try:
        resposta, endereco = sock.recvfrom(1024)
        fim = time.time()
    except socket.timeout:
        print(f"Timeout: sem resposta de {host}")
        return

    rtt = (fim - inicio) * 1000

    print(f"Resposta de {endereco[0]}: seq={seq} RTT={rtt:.2f} ms")


def main():
    host = input("Host: ").strip()

    print(f"\nPING {host} (usando ICMP RAW)\n")

    seq = 1
    while True:
        try:
            ping(host, seq)
            seq += 1
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break


if __name__ == "__main__":
    main()
