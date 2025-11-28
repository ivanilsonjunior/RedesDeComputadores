import hashlib

mensagem = "Redes de Computadores e IoT"

hash_sha256 = hashlib.sha256(mensagem.encode()).hexdigest()

print("Mensagem original:", mensagem)
print("Hash SHA-256:", hash_sha256)
