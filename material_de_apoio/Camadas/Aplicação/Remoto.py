"""
Servidor de controle remoto via UDP broadcast (Didático)
Camada de Aplicação — Redes de Computadores / ADS

Objetivo:
    Demonstrar um "servidor de comandos" simples que escuta broadcast UDP
    e reage a comandos de texto. Note que NÃO há autenticação real: a senha
    de "quit" é fixa e enviada em texto puro — isso é proposital, para
    discutir por que esse desenho é inseguro (ver material_de_apoio/
    SideQuests/Segurança/Criptografia/).

Comandos aceitos:
    pagina       -> abre uma URL no Chrome
    whoru        -> responde "Estou aqui"
    quit <senha> -> encerra o servidor se a senha for "123"

Execução:
    $ python3 Remoto.py
"""

import socket
import webbrowser

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 5555))
    while True:
        data, addr = sock.recvfrom(1024)
        comando = data.decode()
        partes = comando.split(" ")

        if partes[0] == "quit":
            if len(partes) > 1 and partes[1] == "123":
                sock.sendto(b"Fechando...", addr)
                print("Fechando...")
                sock.close()
                break
        elif comando == "pagina":
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            url = "https://laica.ifrn.edu.br/"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        elif comando == "whoru":
            sock.sendto(b"Estou aqui", addr)
except KeyboardInterrupt:
    print("Fechando...")
