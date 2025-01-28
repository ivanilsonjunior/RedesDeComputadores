from Cryptodome.Cipher import AES 
from Cryptodome.Util.Padding import pad

dados = 'Mensagem secreta'.encode("utf-8") # Conversão para bytes
bloco = 16 # Tamanho do bloco AES
dados = pad(dados, bloco) # Preenchimento para garantir que os dados correspondam ao tamanho do bloco
cipher = AES.new(chave, AES.MODE_CBC) # Inicia o cifrador AES no modo CBC
mensagem_cifrada = cipher.encrypt(dados)