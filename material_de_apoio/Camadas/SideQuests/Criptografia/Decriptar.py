from Cryptodome.Util.Padding import unpad

dados_decifrados = cipher.decrypt(mensagem_cifrada)
dados_decifrados = unpad(dados_decifrados, bloco) # Remove o preenchimento
print(dados_decifrados.decode()) # Converte de volta para string