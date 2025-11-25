import socket
import webbrowser
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 5555))
    while True:
        data, addr = sock.recvfrom(1024)
        comando = data.decode()   
        if comando.split(" ")[0] == "quit":
            if comando[1] == "123":
                sock.sendto(b"Fechando...", addr)
                print("Fechando...")
                sock.close()
                break
        if comando == "pagina":
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            url = "https://laica.ifrn.edu.br/"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        if comando.split("")[0] == "whoru":
            sock.sendto(b"Estou aqui", addr)
except KeyboardInterrupt:
    print("Fechando...")
