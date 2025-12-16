# client_comentado.py
# ============================================
# CLIENTE TCP COM RSA + AES + HMAC
# --------------------------------------------
# Funções do cliente:
# - Carregar chave pública do servidor
# - Criar chaves de sessão
# - Realizar handshake seguro
# - Enviar mensagem criptografada
# ============================================

import socket
import json
import secrets
import binascii
import hmac
import hashlib

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding

SERVER = "127.0.0.1"
PORT = 6000

# Carrega a chave pública do servidor
def carregar_chave_publica():
    with open("server_public_key.pem", "rb") as f:
        return serialization.load_pem_public_key(f.read())

# Cifra dados usando RSA
def rsa_encrypt(chave, dados):
    return chave.encrypt(
        dados,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Cifra AES-CBC
def aes_encrypt(chave, dados):
    iv = secrets.token_bytes(16)
    padder = sym_padding.PKCS7(128).padder()
    padded = padder.update(dados) + padder.finalize()

    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv))
    encryptor = cipher.encryptor()
    return iv, encryptor.update(padded) + encryptor.finalize()

def main():
    chave_publica = carregar_chave_publica()

    aes_key = secrets.token_bytes(32)
    hmac_key = secrets.token_bytes(32)
    session_id = secrets.token_hex(16)

    segredo = aes_key + hmac_key + session_id.encode()
    blob = rsa_encrypt(chave_publica, segredo)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER, PORT))
        s.sendall(json.dumps({
            "handshake": binascii.hexlify(blob).decode()
        }).encode())
        s.recv(1024)

    iv, ct = aes_encrypt(aes_key, b"Ola servidor seguro!")
    seq = 1

    dados_hmac = session_id.encode() + seq.to_bytes(8, "big") + iv + ct
    mac = hmac.new(hmac_key, dados_hmac, hashlib.sha256).hexdigest()

    mensagem = {
        "session_id": session_id,
        "seq": seq,
        "iv": binascii.hexlify(iv).decode(),
        "ciphertext": binascii.hexlify(ct).decode(),
        "hmac": mac
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER, PORT))
        s.sendall(json.dumps(mensagem).encode())

if __name__ == "__main__":
    main()
