import socket
import psutil
import webbrowser

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5551))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    msg = clientsocket.recv(12)
    comando = msg.decode("utf-8")
    if comando == "/help":
        clientsocket.send(bytes("Ajuda Requisitada: \n\t /mem para ver a memoria\n\t /off para desligar\n\t /hd espaço em disco ","utf-8"))
    elif comando == "/mem":
        resposta = psutil.virtual_memory()
        clientsocket.send(bytes(str(resposta),"utf-8"))
    elif comando == "/hd":
        resposta = psutil.disk_usage("c:\\")
        clientsocket.send(bytes(str(resposta),"utf-8"))
    elif comando == "/google":
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        url = "https://laica.ifrn.edu.br/"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        clientsocket.send(bytes("Abrindo URL","utf-8"))
    elif comando == "/off":
        resposta = "Desligando o servidor"
        clientsocket.send(bytes(str(resposta),"utf-8"))
        clientsocket.close()
        s.close()
    else:
        clientsocket.send(bytes("Comando Inválido, /help para ajuda.","utf-8"))
    clientsocket.close()
