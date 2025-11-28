# gera_rsa_keys_comentado.py
# ============================================
# GERAÇÃO DE CHAVES RSA (SERVIDOR)
# --------------------------------------------
# Este script gera um par de chaves RSA (2048 bits)
# que será utilizado pelo servidor:
# - Chave PRIVADA: usada para decifrar o handshake
# - Chave PÚBLICA: compartilhada com os clientes
#
# Conceitos abordados:
# - Criptografia assimétrica
# - RSA
# - Serialização em PEM
# ============================================

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Função responsável por criar e salvar as chaves
def gerar_chaves():
    # Gera a chave privada RSA
    # public_exponent=65537 é padrão seguro
    # key_size=2048 é o mínimo recomendado atualmente
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Serializa a chave privada para o formato PEM
    pem_privada = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Gera a chave pública correspondente
    public_key = private_key.public_key()

    # Serializa a chave pública para PEM
    pem_publica = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Salva os arquivos em disco
    with open("server_private_key.pem", "wb") as f:
        f.write(pem_privada)

    with open("server_public_key.pem", "wb") as f:
        f.write(pem_publica)

    print("Chaves RSA geradas com sucesso!")

# Executa o código apenas se o arquivo for chamado diretamente
if __name__ == "__main__":
    gerar_chaves()
