import hashlib
import os

senha = b"senha123"
salt = os.urandom(16)

hash_senha = hashlib.pbkdf2_hmac(
    'sha256',
    senha,
    salt,
    100000
)

print("Salt:", salt)
print("Hash da senha:", hash_senha)
