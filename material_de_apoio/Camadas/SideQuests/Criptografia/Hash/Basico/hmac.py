import hmac
import hashlib

mensagem = b"mensagem transmitida pela rede"
chave = b"chave_compartilhada"

hmac_hash = hmac.new(chave, mensagem, hashlib.sha256).hexdigest()

print("HMAC:", hmac_hash)
