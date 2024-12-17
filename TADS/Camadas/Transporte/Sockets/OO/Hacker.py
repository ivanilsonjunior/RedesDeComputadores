import socket
from ast import literal_eval as make_tuple
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 5005))
    while True:
        data, addr = sock.recvfrom(1024)
        print(data, " recebido de", addr) # data = b"('0.0.0.0', 8888)" 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tup = make_tuple(data.decode())
        s.connect((addr[0], tup[1]))
        s.send("/google".encode("utf-8"))
except KeyboardInterrupt:
    print("Fechando...")