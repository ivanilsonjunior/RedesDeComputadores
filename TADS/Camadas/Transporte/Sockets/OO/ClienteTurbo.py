import socket
from threading import Thread
import time



class Cliente:
    servidores = {}

    def __init__(self) -> None:
        self.publicador = Thread(target=self.escutarServidores())
        self.publicador.setblocking(False)
        self.publicador.start()
        print("Executador Iniciado...")

    def escutarServidores(self):
        print("Esperando servidores...")
        HOST = ''              # Endereco IP do Servidor
        PORT = 5005            # Porta que o Servidor esta
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (HOST, PORT)
        udp.bind(orig)
        while True:
            msg, cliente = udp.recvfrom(1024)
            tupla = eval(msg.decode("utf-8"))
            #print (cliente, "Recebido ", len(msg), "bytes: ",  cliente[0],":",c, "as", int(time()))
            self.servidores[cliente[0]] = {"porta": cliente[0], "lastPing":int(time.time())}

    def showServers(self):
        print(self.servidores)


def main():
    print("teste")
    c = Cliente()
    print("teste")
    while True:
        c.showServers()
        time.sleep(30)


if __name__ == "__main__":
    main()