import socket, time
from Sistema import Sistema
from threading import Thread

class Servidor:
    soc : socket
    sis = Sistema()
    def __init__(self, ip:str, porta:int) -> None:
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipPorta = (ip, porta)
        self.soc.bind(self.ipPorta)

    
    def ligar(self) -> None:
        self.soc.listen()
        publicador = Thread(target=self.publicarCoiso())
        publicador.start()
        while True:
            cliente, address = self.soc.accept()
            msg = cliente.recv(128).decode("utf-8")
            retorno = str(self.sis.comando(msg))
            print("retorno: ", retorno)
            cliente.send(bytes(retorno,"utf-8"))
            cliente.close()
    
    def publicarCoiso(self) -> None:
        interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
        allips = [ip[-1][0] for ip in interfaces]
        msg = str(self.ipPorta).encode("utf-8")
        while True:
            for ip in allips:
                print(f'Publicando em {ip}')
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.bind((ip,0))
                sock.sendto(msg, ("255.255.255.255", 5005))
                sock.close()
            time.sleep(60)

def main():
    server = Servidor("0.0.0.0",8888)
    server.ligar()

if __name__ == "__main__":
    main()
        
