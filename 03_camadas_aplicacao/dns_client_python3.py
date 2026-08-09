#!/usr/bin/env python3
"""
Cliente DNS simples (Didático)
Camada de Aplicação — Redes de Computadores / ADS

Objetivo:
    - Demonstrar consulta DNS manual via UDP.
    - Montar um pacote DNS simples (tipo A).
    - Interpretar a resposta bruta e extrair o(s) endereço(s) IPv4 retornado(s).
    - Explicar a estrutura do protocolo na prática.

Execução:
    $ python3 dns_client_python3.py
"""

import socket
import random
import struct

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


def pular_nome(pacote, offset):
    """
    Avança o offset além de um campo NAME do DNS, seguindo ponteiros
    de compressão (RFC 1035, seção 4.1.4) quando presentes.
    """
    while True:
        tamanho = pacote[offset]

        if tamanho == 0:               # fim do nome
            offset += 1
            break

        if (tamanho & 0xC0) == 0xC0:   # ponteiro de compressão (2 bytes)
            offset += 2
            break

        offset += 1 + tamanho          # pula label (tamanho + conteúdo)

    return offset


def parsear_resposta(pacote):
    """
    Interpreta o cabeçalho e a Answer Section de uma resposta DNS,
    extraindo os endereços IPv4 (registros tipo A) retornados.
    """
    ancount = struct.unpack("!H", pacote[6:8])[0]

    # Pula cabeçalho (12 bytes) e a Question Section (nome + QTYPE + QCLASS)
    offset = pular_nome(pacote, 12) + 4

    enderecos = []
    for _ in range(ancount):
        offset = pular_nome(pacote, offset)  # NAME da resposta

        tipo, _classe, ttl, rdlength = struct.unpack("!HHIH", pacote[offset:offset + 10])
        offset += 10

        rdata = pacote[offset:offset + rdlength]
        offset += rdlength

        if tipo == 1 and rdlength == 4:      # Tipo A = endereço IPv4
            ip = ".".join(str(b) for b in rdata)
            enderecos.append((ip, ttl))

    return enderecos


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

        enderecos = parsear_resposta(resposta)
        if enderecos:
            print("\n[+] Endereços IPv4 (registros tipo A) encontrados:")
            for ip, ttl in enderecos:
                print(f"    {ip}   (TTL={ttl}s)")
        else:
            print("\n[-] Nenhum registro tipo A encontrado na resposta.")

    except socket.timeout:
        print("[-] Tempo de resposta esgotado!")

    sock.close()


if __name__ == "__main__":
    main()
