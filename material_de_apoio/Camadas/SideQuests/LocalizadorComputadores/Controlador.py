import socket
import threading
import time

BROADCAST_PORT = 50000


class ClientInfo:
    def __init__(self, ip, tcp_port):
        self.ip = ip
        self.tcp_port = tcp_port
        self.last_seen = time.time()
        self.last_msg = ""
        self.mac = None

    def update(self, msg):
        self.last_msg = msg
        self.last_seen = time.time()

    def __repr__(self):
        age = round(time.time() - self.last_seen, 1)
        return (f"{self.ip}:{self.tcp_port} | MAC={self.mac} | "
                f"UltimaMsg='{self.last_msg}' | {age}s atrás")


class DiscoveryServer:
    def __init__(self):
        self.clients = {}      # chave: (ip, tcp_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", BROADCAST_PORT))

    # ----------------------------------------------------------------
    # ESCUTA BROADCASTS
    # ----------------------------------------------------------------
    def listen_broadcasts(self):
        print(f"[Servidor] Ouvindo broadcasts na porta {BROADCAST_PORT}...")

        while True:
            data, addr = self.sock.recvfrom(1024)
            msg = data.decode()
            ip = addr[0]

            print(f"[Broadcast de {ip}] {msg}")

            if msg.startswith("DISCOVER_REQUEST"):
                tcp_port = int(msg.split("=")[1])
                key = (ip, tcp_port)

                # cadastra usando chave composta
                if key not in self.clients:
                    self.clients[key] = ClientInfo(ip, tcp_port)
                    print(f"[Novo cliente] {ip}:{tcp_port}")

                # atualiza keepalive
                self.clients[key].update(msg)

                # envia resposta UDP
                self.sock.sendto("DISCOVER_RESPONSE".encode(), addr)

    # ----------------------------------------------------------------
    # SOLICITA MAC via TCP
    # ----------------------------------------------------------------
    def ask_mac_tcp(self, key):
        """
        key = (ip, tcp_port)
        """
        if key not in self.clients:
            print("Cliente não encontrado!")
            return

        ip, port = key
        print(f"[Servidor] Conectando via TCP em {ip}:{port} ...")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))

            sock.send(b"GET_MAC")
            response = sock.recv(1024).decode()
            sock.close()

            if response.startswith("MAC_ADDRESS;"):
                mac = response.split(";")[1]
                self.clients[key].mac = mac
                print(f"[MAC recebido via TCP] {ip}:{port} => {mac}")

        except Exception as e:
            print(f"Erro ao conectar via TCP: {e}")

    # ----------------------------------------------------------------
    # MENU COM match-case
    # ----------------------------------------------------------------
    def menu(self):
        while True:
            print("\n=== MENU SERVIDOR ===")
            print("1 - Listar clientes")
            print("2 - Solicitar MAC de um cliente (TCP)")
            print("3 - Solicitar MAC de todos clientes (TCP)")
            print("0 - Sair")
            op = input("> ")

            match op:
                case "1":
                    print("\n--- CLIENTES ---")
                    for key, info in self.clients.items():
                        print(f"{key} -> {info}")

                case "2":
                    ip = input("Digite o IP: ")
                    port = int(input("Digite a porta TCP do cliente: "))
                    self.ask_mac_tcp((ip, port))

                case "3":
                    for key in self.clients:
                        self.ask_mac_tcp(key)

                case "0":
                    exit()

                case _:
                    print("Opção inválida.")

    def start(self):
        threading.Thread(target=self.listen_broadcasts, daemon=True).start()
        self.menu()


if __name__ == "__main__":
    DiscoveryServer().start()
