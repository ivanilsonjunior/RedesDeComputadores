import socket
import random
HOST = ''              # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print ("Esperando conexões na porta",orig)
i = 0
numero = random.randint(0,10000)
while True:
    msg, cliente = udp.recvfrom(1024)
    try:
        palpine = int(msg.decode("utf-8"))
    except:
        pass
    if (palpine == numero):
        udp.close()
        print (cliente, "acertou!!!!!")
        break
    if (palpine > numero):
        print (cliente, "mandou um palpite maior...")
    if (palpine < numero):
        print (cliente, "mandou um palpite menor...")
    print (cliente, "Recebido ", len(msg), "bytes: ", msg.decode("utf-8") )
