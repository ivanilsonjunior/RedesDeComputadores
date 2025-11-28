import hashlib

def gerar_hash_arquivo(nome_arquivo):
    sha256 = hashlib.sha256()

    with open(nome_arquivo, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha256.update(bloco)

    return sha256.hexdigest()

arquivo = "dados.txt"
print("Hash do arquivo:", gerar_hash_arquivo(arquivo))
