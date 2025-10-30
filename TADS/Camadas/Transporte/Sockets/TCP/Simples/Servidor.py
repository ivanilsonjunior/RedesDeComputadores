import socket
porta=4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", porta))
s.listen(1)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
msg = clientsocket.recv(100)
mensagem = msg.decode("utf-8")
print (f"Recebido: {mensagem}")
resposta = "Obrigado por falar comigo"
clientsocket.send(bytes(str(resposta),"utf-8"))
clientsocket.close()
s.close()