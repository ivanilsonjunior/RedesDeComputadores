from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

#############################
# Variables
#############################
HOST, PORT = "127.0.0.1", 8080
response =  b"HTTP/1.1 200 OK\n\n<html><head></head><body><h1>Pagina Padraum</h1><br><hr><p>Pagina de teste, esse servidor so envia isso... por enquanto...</p></body></html>"
#############################

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        try:
            conn, addr = sock.accept()
            req = conn.recv(1024).decode()
            print(req)
            conn.sendall(response)
            conn.close()
        except Exception as E:
            print(E)