"""
Servidor UDP — Jogo de Adivinhação (Didático)
Camada de Transporte — Redes de Computadores / ADS

Objetivo:
    Sorteia um número entre 0 e 10000 e recebe palpites via UDP.
    Para cada palpite recebido, responde ao cliente (sendto) se o
    número sorteado é maior, menor, ou se o cliente acertou.

Execução:
    $ python3 Servidor.py

Requer:
    Cliente.py desta mesma pasta, enviando palpites para a mesma porta.
"""

import socket
import random

HOST = ''              # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print("Esperando palpites na porta", orig)
numero = random.randint(0, 10000)

while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente, "Recebido", len(msg), "bytes:", msg.decode("utf-8"))

    try:
        palpite = int(msg.decode("utf-8"))
    except ValueError:
        udp.sendto(b"Palpite invalido, envie um numero inteiro.", cliente)
        continue

    if palpite == numero:
        udp.sendto(b"acertou!", cliente)
        print(cliente, "acertou!!!!!")
        udp.close()
        break
    elif palpite > numero:
        udp.sendto(b"menor", cliente)
        print(cliente, "mandou um palpite maior...")
    else:
        udp.sendto(b"maior", cliente)
        print(cliente, "mandou um palpite menor...")
