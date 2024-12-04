import socket
import sys

def main():
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    allips = [ip[-1][0] for ip in interfaces]

    msg = str.encode(sys.argv[1]) if len(sys.argv) > 1 else b'Teste'
    for ip in allips:
        print(f'Enviando para {ip}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((ip,0))
        sock.sendto(msg, ("255.255.255.255", 5005))
        sock.close()


main()
