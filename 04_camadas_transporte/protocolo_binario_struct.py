#!/usr/bin/env python3
"""
Protocolo Binário com struct (Didático)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Aplicar os conceitos da Unidade 4 (04_camadas_transporte/04_representacao_dados_struct.md)
    na construção de um protocolo de aplicação próprio: um cabeçalho binário
    fixo (struct), com flags (bit a bit) e um payload de tamanho variável.

Formato do cabeçalho (6 bytes, network byte order):
    +---------+---------+----------------+----------------+
    | Versão  | Flags   | Identificador  | Tam. Payload   |
    | 1 byte  | 1 byte  | 2 bytes        | 2 bytes        |
    +---------+---------+----------------+----------------+
    | Payload (UTF-8, tamanho variável)                    |
    +-------------------------------------------------------+

Flags (bit a bit):
    bit 0 (0x01) — MAIUSCULO: servidor responde o texto em maiúsculas.
    bit 1 (0x02) — INVERTER : servidor responde o texto invertido.
    As duas podem ser combinadas (OR) na mesma mensagem.

Execução:
    Servidor:
        $ python3 protocolo_binario_struct.py
    Cliente:
        $ python3 protocolo_binario_struct.py cliente
"""

import socket
import struct
import sys

HOST = "127.0.0.1"
PORT = 5050

FORMATO_CABECALHO = "!BBHH"  # versão, flags, identificador, tamanho do payload
TAMANHO_CABECALHO = struct.calcsize(FORMATO_CABECALHO)

VERSAO = 1
MAIUSCULO = 1 << 0
INVERTER = 1 << 1


def empacotar(identificador, flags, texto):
    """Monta uma mensagem completa (cabeçalho + payload) a partir dos campos da aplicação."""
    payload = texto.encode("utf-8")
    cabecalho = struct.pack(FORMATO_CABECALHO, VERSAO, flags, identificador, len(payload))
    return cabecalho + payload


def recv_exato(conexao, tamanho):
    """
    recv() pode devolver menos bytes do que o pedido (TCP entrega um fluxo,
    não mensagens prontas — ver 02_api_sockets.md, seção 5.6). Este laço
    garante receber exatamente `tamanho` bytes antes de continuar.
    """
    dados = b""
    while len(dados) < tamanho:
        pedaco = conexao.recv(tamanho - len(dados))
        if not pedaco:
            return None
        dados += pedaco
    return dados


def receber_mensagem(conexao):
    """Lê um cabeçalho de tamanho fixo e, em seguida, o payload de tamanho variável."""
    cabecalho = recv_exato(conexao, TAMANHO_CABECALHO)
    if cabecalho is None:
        return None

    versao, flags, identificador, tamanho_payload = struct.unpack(FORMATO_CABECALHO, cabecalho)
    payload = recv_exato(conexao, tamanho_payload)
    if payload is None:
        return None

    return versao, flags, identificador, payload.decode("utf-8")


def processar(flags, texto):
    """Aplica as flags da requisição para gerar o texto de resposta do servidor."""
    if flags & MAIUSCULO:
        texto = texto.upper()
    if flags & INVERTER:
        texto = texto[::-1]
    return texto


def servidor():
    escuta = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escuta.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    escuta.bind((HOST, PORT))
    escuta.listen()
    print(f"[*] Servidor do protocolo binário ouvindo em {HOST}:{PORT}")

    while True:
        conexao, endereco = escuta.accept()
        print(f"[+] Cliente conectado: {endereco}")

        with conexao:
            while True:
                mensagem = receber_mensagem(conexao)
                if mensagem is None:
                    break

                versao, flags, identificador, texto = mensagem
                print(f"    recebido: id={identificador} flags={flags:#04x} texto={texto!r}")

                resposta = processar(flags, texto)
                conexao.sendall(empacotar(identificador, flags, resposta))

        print(f"[-] Cliente desconectado: {endereco}")


def cliente():
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.connect((HOST, PORT))
    print(f"[*] Conectado ao servidor em {HOST}:{PORT}\n")

    identificador = 0
    try:
        while True:
            texto = input("Mensagem (ou 'sair'): ")
            if texto.lower() == "sair":
                break

            flags = 0
            if input("Responder em MAIÚSCULAS? (s/N): ").strip().lower() == "s":
                flags |= MAIUSCULO
            if input("Responder INVERTIDO? (s/N): ").strip().lower() == "s":
                flags |= INVERTER

            identificador += 1
            conexao.sendall(empacotar(identificador, flags, texto))

            mensagem = receber_mensagem(conexao)
            if mensagem is None:
                print("[-] Servidor encerrou a conexão.")
                break

            _, _, id_resposta, texto_resposta = mensagem
            print(f"[<] resposta (id={id_resposta}): {texto_resposta}\n")
    finally:
        conexao.close()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cliente":
        cliente()
    else:
        servidor()
