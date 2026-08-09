import socket
porta = 4444
servidor = "127.0.0.1"  # troque pelo IP do servidor se rodar em outra máquina
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((servidor, porta))
msg = input("Qual a Mensagem? > ")
s.send(msg.encode("utf-8"))
resposta = s.recv(1024)
print("Resposta:", resposta.decode("utf-8"))