#!/usr/bin/env python3
"""
Servidor TCP Concorrente com asyncio (Didático)
Camada de Transporte — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar a alternativa a threads apresentada na Unidade 3
    (04_camadas_transporte/03_servidores_concorrentes.md): uma única thread,
    um event loop, e uma coroutine (Task) por cliente conectado.

    Compare este arquivo com servidor_concorrente_threads.py: a lógica de
    atendimento é praticamente a mesma, mas aqui "ceder o controle" é
    explícito através de `await`, em vez de depender do escalonador do SO.

Execução:
    $ python3 servidor_concorrente_asyncio.py

Teste (em terminais separados, simultaneamente):
    $ python3 tcp_echo_client_python3.py
"""

import asyncio

HOST = "0.0.0.0"
PORT = 5000

contador_clientes = 0


async def atender_cliente(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """Uma Task independente por cliente. Não bloqueia as demais conexões."""
    global contador_clientes

    contador_clientes += 1
    numero_deste_cliente = contador_clientes

    endereco = writer.get_extra_info("peername")
    print(f"[+] Cliente {numero_deste_cliente} conectado: {endereco}")

    try:
        while True:
            dados = await reader.read(1024)
            if not dados:
                break

            resposta = dados + f" (cliente #{numero_deste_cliente})".encode("utf-8")
            writer.write(resposta)
            await writer.drain()
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"[-] Cliente {numero_deste_cliente} desconectado: {endereco}")


async def main():
    servidor = await asyncio.start_server(atender_cliente, HOST, PORT)

    enderecos = ", ".join(str(sock.getsockname()) for sock in servidor.sockets)
    print(f"[*] Servidor concorrente (asyncio) ouvindo em {enderecos}")
    print("[*] Uma única thread; cada cliente vira uma Task no event loop.\n")

    async with servidor:
        await servidor.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[*] Encerrando servidor...")
