import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5551))
#full_msg = ''

cmd = input("Insira o comando: ")

s.send(cmd.encode("utf-8"))

#while True:
msg = s.recv(1024)
#    if len(msg) <= 0:
#        break
#    full_msg += msg.decode("utf-8")

print("Mensagem:", msg.decode("utf-8"))
