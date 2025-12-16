from cryptography.fernet import Fernet

key = input("Informe a chave: ").encode()
cipher = Fernet(key)

with open("dados.enc", "rb") as f:
    encrypted = f.read()

decrypted = cipher.decrypt(encrypted)

with open("dados_decriptado.txt", "wb") as f:
    f.write(decrypted)

print("Arquivo descriptografado")
