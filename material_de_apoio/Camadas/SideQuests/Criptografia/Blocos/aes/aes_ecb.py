from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
data = b"Mensagem secreta IoT"

padder = padding.PKCS7(128).padder()
padded_data = padder.update(data) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

decryptor = cipher.decryptor()
plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()

print("Texto original:", data)
print("Criptografado:", ciphertext)
print("Descriptografado:", plaintext)
