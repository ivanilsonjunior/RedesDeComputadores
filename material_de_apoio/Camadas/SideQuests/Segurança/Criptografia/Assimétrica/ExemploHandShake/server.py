# server_comentado.py
# ============================================
# SERVIDOR TCP COM RSA + AES + HMAC
# --------------------------------------------
# Funções deste servidor:
# - Receber handshake cifrado com RSA
# - Extrair chaves de sessão AES + HMAC
# - Receber mensagens criptografadas
# - Validar integridade com HMAC
# ============================================

import socket
import json
import os
import hmac
import hashlib
import binascii

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding

HOST = "0.0.0.0"
PORT = 6000

# Estrutura que armazena sessões ativas:
# session_id -> (aes_key, hmac_key, seq_esperado)
sessoes = {}

# Carrega a chave privada do servidor
def carregar_chave_privada():
    with open("server_private_key.pem", "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

# Decifra dados usando RSA-OAEP
def rsa_decrypt(chave_privada, dados):
    return chave_privada.decrypt(
        dados,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Calcula HMAC-SHA256
def calcular_hmac(chave, dados):
    return hmac.new(chave, dados, hashlib.sha256).hexdigest()

# Descriptografa AES-CBC
def aes_decrypt(chave, iv, ciphertext):
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = sym_padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()

def main():
    chave_privada = carregar_chave_privada()
    print("Servidor iniciado...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            print("Conexão de:", addr)

            data = conn.recv(65536)
            mensagem = json.loads(data.decode())

            # =====================
            # PROCESSO DE HANDSHAKE
            # =====================
            if "handshake" in mensagem:
                blob = binascii.unhexlify(mensagem["handshake"])
                segredo = rsa_decrypt(chave_privada, blob)

                aes_key = segredo[:32]
                hmac_key = segredo[32:64]
                session_id = segredo[64:].decode()

                sessoes[session_id] = (aes_key, hmac_key, 1)
                conn.sendall(b"{"status": "OK"}")
                conn.close()
                continue

            # ======================
            # MENSAGEM NORMAL
            # ======================
            session_id = mensagem["session_id"]
            seq = mensagem["seq"]

            aes_key, hmac_key, esperado = sessoes[session_id]

            # Verifica replay
            if seq != esperado:
                conn.close()
                continue

            iv = binascii.unhexlify(mensagem["iv"])
            ciphertext = binascii.unhexlify(mensagem["ciphertext"])

            dados_hmac = session_id.encode() + seq.to_bytes(8, "big") + iv + ciphertext
            if not hmac.compare_digest(
                calcular_hmac(hmac_key, dados_hmac),
                mensagem["hmac"]
            ):
                conn.close()
                continue

            texto = aes_decrypt(aes_key, iv, ciphertext).decode()
            print("Mensagem segura recebida:", texto)

            sessoes[session_id] = (aes_key, hmac_key, esperado + 1)
            conn.close()

if __name__ == "__main__":
    main()
