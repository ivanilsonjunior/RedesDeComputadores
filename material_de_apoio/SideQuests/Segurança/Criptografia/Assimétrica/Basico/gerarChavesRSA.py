from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gera par de chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serializa chave privada
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Serializa chave pública
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("chave_privada.pem", "wb") as f:
    f.write(pem_private)

with open("chave_publica.pem", "wb") as f:
    f.write(pem_public)

print("Chaves RSA geradas")
