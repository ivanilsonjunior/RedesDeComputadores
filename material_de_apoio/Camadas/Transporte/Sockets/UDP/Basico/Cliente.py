"""
Cliente UDP — Jogo de Adivinhação (Didático)
Camada de Transporte — Redes de Computadores / ADS

Objetivo:
    Envia palpites (números inteiros) ao Servidor.py desta mesma pasta,
    que sorteou um número entre 0 e 10000, e mostra a resposta do servidor
    (maior / menor / acertou).

Execução:
    $ python3 Cliente.py

Requer:
    Servidor.py rodando na mesma porta (5005).
"""

import socket

HOST = 'localhost'   # Endereco IP do Servidor
PORT = 5005          # Mesma porta definida em Servidor.py

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

try:
    while True:
        palpite = input("Seu palpite (0-10000, ou 'sair'): ")
        if palpite.lower() == "sair":
            break

        udp.sendto(palpite.encode(), dest)
        resposta, _ = udp.recvfrom(1024)
        print("Servidor respondeu:", resposta.decode())

        if resposta.decode() == "acertou!":
            break
except KeyboardInterrupt:
    print("\nEncerrando...")
finally:
    udp.close()
