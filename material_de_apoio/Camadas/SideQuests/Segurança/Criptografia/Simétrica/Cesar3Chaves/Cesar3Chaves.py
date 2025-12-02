class Cifrador:
    """
    Implementa uma cifra baseada em César com deslocamentos cíclicos.
    """

    def __init__(self, key):
        if not isinstance(key, (list, tuple)) or not all(isinstance(i, int) for i in key):
            raise ValueError("A chave deve ser uma lista de inteiros.")
        self.key = list(key)

    def _shift_char(self, char, deslocamento):
        """Desloca um único caractere respeitando maiúsculas/minúsculas."""
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + deslocamento) % 26 + base)
        return char

    def encrypt(self, text):
        """Criptografa o texto usando a chave cíclica."""
        resultado = []
        k = len(self.key)
        idx = 0

        for char in text:
            if char.isalpha():
                desloc = self.key[idx % k]
                novo = self._shift_char(char, desloc)
                resultado.append(novo)
                idx += 1
            else:
                resultado.append(char)

        return "".join(resultado)

    def decrypt(self, text):
        """Descriptografa o texto desfazendo os deslocamentos."""
        resultado = []
        k = len(self.key)
        idx = 0

        for char in text:
            if char.isalpha():
                desloc = -self.key[idx % k]
                novo = self._shift_char(char, desloc)
                resultado.append(novo)
                idx += 1
            else:
                resultado.append(char)

        return "".join(resultado)


# ------------------------------
# Exemplo de uso
# ------------------------------
if __name__ == "__main__":
    chave = [1, 2, 3]
    cipher = Cifrador(chave)

    texto = "banana"
    cifrado = cipher.encrypt(texto)
    decifrado = cipher.decrypt(cifrado)

    print("Texto original :", texto)
    print("Texto cifrado  :", cifrado)
    print("Texto decifrado:", decifrado)
