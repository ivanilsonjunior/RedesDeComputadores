from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("chave_privada.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), None)

mensagem = b"Mensagem autenticada"

assinatura = private_key.sign(
    mensagem,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("assinatura.sig", "wb") as f:
    f.write(assinatura)

print("Mensagem assinada")
