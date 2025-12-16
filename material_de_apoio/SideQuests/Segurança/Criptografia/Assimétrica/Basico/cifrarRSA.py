from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("chave_publica.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

mensagem = b"Mensagem secreta pela rede"

cifrada = public_key.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("mensagem.cif", "wb") as f:
    f.write(cifrada)

print("Mensagem cifrada")
