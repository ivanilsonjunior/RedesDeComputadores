import socket
HOST = ''              # Endereco IP do Servidor
PORT = 22222            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print ("Esperando conexões na porta",orig)
i = 0
while True:
    msg, cliente = udp.recvfrom(1024)
    print (cliente, len(msg))
udp.close()
