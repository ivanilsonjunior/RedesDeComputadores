def cifrar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + chave) % 26 + base)
        else:
            resultado += char
    return resultado


def decifrar(texto, chave):
    return cifrar(texto, -chave)


if __name__ == "__main__":
    mensagem = "Redes e IoT"
    chave = 3

    criptografado = cifrar(mensagem, chave)
    descriptografado = decifrar(criptografado, chave)

    print("Mensagem original:", mensagem)
    print("Criptografada:", criptografado)
    print("Descriptografada:", descriptografado)
