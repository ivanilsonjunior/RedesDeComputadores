from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)

nonce = os.urandom(12)
data = b"Mensagem segura para IoT"
aad = b"header"

ciphertext = aesgcm.encrypt(nonce, data, aad)
plaintext = aesgcm.decrypt(nonce, ciphertext, aad)

print("Original:", data)
print("Descriptografado:", plaintext)
