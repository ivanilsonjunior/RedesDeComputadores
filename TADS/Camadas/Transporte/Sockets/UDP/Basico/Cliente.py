import socket
HOST = 'localhost'  # Endereco IP do Servidor
PORT = 22222            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = "10.10.10.10 10.10.10.1 26"
udp.sendto (msg.encode(), dest)
udp.close()
