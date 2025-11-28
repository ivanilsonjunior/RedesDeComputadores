from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("chave_publica.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

with open("assinatura.sig", "rb") as f:
    assinatura = f.read()

mensagem = b"Mensagem autenticada"

try:
    public_key.verify(
        assinatura,
        mensagem,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Assinatura válida ✅")
except:
    print("Assinatura inválida ❌")
