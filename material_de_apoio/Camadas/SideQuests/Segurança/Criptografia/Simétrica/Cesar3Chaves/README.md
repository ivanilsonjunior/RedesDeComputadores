# 📘 Cifra de César Cíclica (Versão Avançada / Polialfabética)

Este módulo apresenta uma variação da clássica **Cifra de César**, mas
utilizando **deslocamentos múltiplos e cíclicos**, semelhante a um
mecanismo polialfabético simplificado.\
A implementação foi escrita 100% em Python e estruturada sob o paradigma
**orientado a objetos (OO)**.

------------------------------------------------------------------------

# 🔐 1. O que é a Cifra de César Cíclica?

A cifra original de César aplica um **único deslocamento fixo** (ex.:
+3) a todas as letras.\
Aqui, implementamos uma versão mais robusta:

-   A chave é uma **lista cíclica de inteiros**
-   Pode incluir valores **positivos ou negativos**
-   Cada letra usa um deslocamento diferente
-   Quando a chave termina, ela **reinicia**
-   Apenas letras são cifradas; demais caracteres são preservados

------------------------------------------------------------------------

# 🧠 2. Teoria da Cifra (Formulação Matemática)

Converter o caractere para 0--25:

x = ord(char) - base

Operação de cifra:

E(x) = (x + k_i) mod 26

Operação de decifra:

D(x) = (x - k_i) mod 26

A chave é cíclica:

k_i = key\[i mod len(key)\]

------------------------------------------------------------------------

# 🔁 3. Exemplo Didático

Mensagem: `banana`\
Chave: `[1, 2, 3]`

Resultado cifrado: `ccqbpd`

------------------------------------------------------------------------

# 🏗️ 4. Implementação Orientada a Objetos

``` python
class Cifrador:
    def __init__(self, key):
        if not isinstance(key, (list, tuple)) or not all(isinstance(i, int) for i in key):
            raise ValueError("A chave deve ser uma lista de inteiros.")
        self.key = list(key)

    def _shift_char(self, char, deslocamento):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + deslocamento) % 26 + base)
        return char

    def encrypt(self, text):
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
```

------------------------------------------------------------------------

# 🧪 5. Exemplo de Uso

``` python
cipher = Cifrador([1, 2, 3])

msg = "banana"
enc = cipher.encrypt(msg)
dec = cipher.decrypt(enc)

print(enc)  # ccqbpd
print(dec)  # banana
```

------------------------------------------------------------------------

# 📦 6. Integração no Repositório

Sugestão:

Simétrica/ └── Basicos/ └── cesar_ciclica/ ├── cyclic_cesar.py └──
README.md

------------------------------------------------------------------------

# 🔎 7. Limitações e Extensões

✔ Funciona com letras (A--Z, a--z)\
✔ Chaves com qualquer tamanho\
✔ Deslocamentos negativos\
✔ Uso educacional

Possíveis extensões: - suporte a acentuação\
- CLI\
- testes automatizados\
- controlador de arquivos

------------------------------------------------------------------------

# 🎓 8. Conclusão

Uma cifra intermediária entre César simples e Vigenère, ideal para
ensino de criptografia simétrica e modularidade.

------------------------------------------------------------------------
