import socket
from Sistema import Sistema
class Servidor:
    soc : socket
    sis = Sistema()
    def __init__(self, ip:str, porta:int) -> None:
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind((ip, porta))
    
    def ligar(self) -> None:
        self.soc.listen()
        while True:
            cliente, address = self.soc.accept()
            msg = cliente.recv(128).decode("utf-8")
            retorno = self.sis.comando(msg)
            cliente.send(bytes(retorno,"utf-8"))
            cliente.close()
def main():
    server = Servidor("127.0.0.1",8888)
    server.ligar()

if __name__ == "__main__":
    main()
        
