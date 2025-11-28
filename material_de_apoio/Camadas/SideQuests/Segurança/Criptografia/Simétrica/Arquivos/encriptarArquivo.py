from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

with open("dados.txt", "rb") as f:
    dados = f.read()

encrypted = cipher.encrypt(dados)

with open("dados.enc", "wb") as f:
    f.write(encrypted)

print("Arquivo criptografado")
print("Chave:", key.decode())
