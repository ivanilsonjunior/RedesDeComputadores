import socket
porta=4444
servidor = "192.168.56.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((servidor, porta))
msg = input("Qual a Mensagem? > ")
s.send(msg.encode("utf-8"))
resposta = s.recv(1024)
print("Resposta:", resposta.decode("utf-8"))