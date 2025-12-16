import socket
import threading
import random
import time
import uuid

BROADCAST_PORT = 50000
BROADCAST_ADDR = "<broadcast>"
BROADCAST_DELAY = 5


class Client:
    def __init__(self):
        self.tcp_port = random.randint(20000, 40000)
        self.running = True
        self.mac = self.get_local_mac()

    def get_local_mac(self):
        mac_int = uuid.getnode()
        return ":".join(f"{(mac_int >> 8*i) & 0xff:02x}" for i in reversed(range(6)))

    # -----------------------------------------------------------
    # UDP: broadcast de descoberta
    # -----------------------------------------------------------
    def send_broadcast(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        while self.running:
            msg = f"DISCOVER_REQUEST;PORT={self.tcp_port}"
            sock.sendto(msg.encode(), (BROADCAST_ADDR, BROADCAST_PORT))
            print(f"[Broadcast enviado] {msg}")
            time.sleep(BROADCAST_DELAY)

    # -----------------------------------------------------------
    # TCP: servidor interno para responder comandos
    # -----------------------------------------------------------
    def tcp_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", self.tcp_port))
        sock.listen(5)

        print(f"[Cliente] Servidor TCP escutando na porta {self.tcp_port}...")

        while self.running:
            conn, addr = sock.accept()
            print(f"[TCP] Conexão recebida de {addr}")

            data = conn.recv(1024).decode()

            if data == "GET_MAC":
                response = f"MAC_ADDRESS;{self.mac}"
                conn.send(response.encode())
                print(f"[MAC enviado via TCP] {self.mac}")

            conn.close()

    def main_logic(self):
        while self.running:
            time.sleep(5)

    def start(self):
        print(f"[Cliente] TCP_PORT={self.tcp_port}  |  MAC={self.mac}")

        threading.Thread(target=self.send_broadcast, daemon=True).start()
        threading.Thread(target=self.tcp_server, daemon=True).start()

        self.main_logic()


if __name__ == "__main__":
    Client().start()
