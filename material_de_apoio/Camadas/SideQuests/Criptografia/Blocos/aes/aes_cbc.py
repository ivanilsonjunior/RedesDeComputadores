from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
iv = os.urandom(16)
data = b"Seguranca em Redes e IoT"

padder = padding.PKCS7(128).padder()
padded = padder.update(data) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded) + encryptor.finalize()

decryptor = cipher.decryptor()
plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()

print("Descriptografado:", plaintext)
