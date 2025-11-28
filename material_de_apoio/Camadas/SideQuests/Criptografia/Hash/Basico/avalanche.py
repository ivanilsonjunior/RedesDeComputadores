import hashlib

msg1 = "seguranca"
msg2 = "Seguranca"  # apenas uma letra alterada

hash1 = hashlib.sha256(msg1.encode()).hexdigest()
hash2 = hashlib.sha256(msg2.encode()).hexdigest()

print("Mensagem 1:", msg1)
print("Hash 1:", hash1)

print("\nMensagem 2:", msg2)
print("Hash 2:", hash2)
