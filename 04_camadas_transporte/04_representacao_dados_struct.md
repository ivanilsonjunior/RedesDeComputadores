# Unidade 4 — Representação de Dados e Programação de Protocolos com Python
Material adaptado do curso **Programação para Redes (NCT)** — DIATINF/IFRN

> Pré-requisito: [`03_servidores_concorrentes.md`](03_servidores_concorrentes.md). Esta unidade fecha o ciclo: depois de saber comunicar-se via sockets (Unidade 2) e atender vários clientes (Unidade 3), falta saber **construir e interpretar o conteúdo binário** das mensagens — a base de qualquer protocolo de aplicação próprio. Veja a aplicação prática em [`protocolo_binario_struct.py`](protocolo_binario_struct.py), e compare com o parsing manual de um protocolo real em [`../03_camadas_aplicacao/dns_client_python3.py`](../03_camadas_aplicacao/dns_client_python3.py).

**Objetivo geral**: compreender como informações são representadas, serializadas, transmitidas e interpretadas em uma rede, culminando na capacidade de montar e interpretar campos binários de um protocolo com o módulo `struct`.

---

## 1. Da informação aos bytes

Aplicações de rede trabalham com textos, números, endereços IP — mas nada disso é transmitido "como é apresentado ao usuário". No nível mais fundamental, tudo vira **bits**, organizados por protocolos em campos de tamanhos definidos.

### 1.1 Bit: a unidade fundamental

Um **bit** assume só dois valores: `0` ou `1`. Com **n bits**, é possível representar **2ⁿ** combinações:

| Bits | Combinações |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 4 | 16 |
| 8 | 256 |
| 16 | 65.536 |
| 32 | 4.294.967.296 |

### 1.2 Byte e octeto

Um grupo de **8 bits** é um **byte** (também chamado **octeto** em documentação de protocolos). Um endereço IPv4 como `192.168.1.10` tem 4 octetos × 8 bits = **32 bits**:

```
192       168       1         10
11000000  10101000  00000001  00001010
```

### 1.3 – 1.4 Sistema binário e representação de um byte completo

Cada posição de um número binário representa uma potência de 2. Para `110101`:

```
Bit       1  1  0  1  0  1
Potência  2⁵ 2⁴ 2³ 2² 2¹ 2⁰
Valor     32 16 8  4  2  1
```

Somando os bits ativos: `32+16+4+1 = 53`, ou seja `110101₂ = 53₁₀`. Em Python: `bin(53)` → `'0b110101'`. Se o campo tem exatamente 8 bits, complete com zeros à esquerda: `f"{53:08b}"` → `'00110101'` (`08b`: representar em **b**inário, largura **8**, preenchendo com **0**).

### 1.5 Valores representáveis por N bits (inteiros sem sinal)

| Tamanho | Menor valor | Maior valor |
|---|---|---|
| 8 bits | 0 | 255 |
| 16 bits | 0 | 65.535 |
| 32 bits | 0 | 4.294.967.295 |

É por isso que um octeto de IPv4 vai de 0 a 255, e uma porta TCP/UDP (campo de 16 bits) vai de 0 a 65535.

### 1.6 – 1.7 Sistema hexadecimal

Representações binárias ficam longas rapidamente, então é comum usar **hexadecimal** (base 16: `0-9`, `A-F`, onde `A=10 ... F=15`). Cada dígito hex representa exatamente **4 bits**, então um byte = exatamente **2 dígitos hex**:

```
00110101 → 3 5 → 0x35
11111111 → 0xFF → 255
```

Em Python, `0x35`, `0b110101` e `53` são só **formas diferentes de escrever o mesmo valor**:

```python
a = 53
b = 0x35
print(a == b)          # True
print(bin(a), hex(a))  # 0b110101  0x35
```

### 1.8 Formatação em Python

```python
valor = 53
print(f"Decimal: {valor}")
print(f"Binário: {valor:08b}")       # 00110101
print(f"Hexadecimal: {valor:02x}")   # 35
print(f"Binário com prefixo: {valor:#010b}")
print(f"Hex com prefixo: {valor:#04x}")
```

### 1.9 Agrupando bits e relação bits ↔ bytes ↔ hex

```
8 bits  → 1 byte  → 2 dígitos hex
16 bits → 2 bytes → 4 dígitos hex
32 bits → 4 bytes → 8 dígitos hex
```

Vale memorizar — aparece o tempo todo na leitura/construção de estruturas binárias.

### 1.10 Inteiros com e sem sinal

Até aqui só vimos **inteiros sem sinal**. Para representar negativos, usa-se **complemento de dois**. Com 8 bits, um inteiro **com sinal** vai de `-128` a `127`. A mesma sequência `11111111` pode significar `255` (sem sinal) ou `-1` (com sinal, complemento de dois) — **os bits sozinhos não dizem nada**; é a especificação do protocolo que define como interpretá-los.

### 1.11 Bits como campos de protocolo

Um único byte pode conter vários campos menores. Exemplo hipotético:

```
+---+---+---+-----------+
| A | B | C |  CÓDIGO   |
+---+---+---+-----------+
 1   1   1   5 bits
```

`10100101` não é "só" o número 165 — pode significar `A=1, B=0, C=1, Código=00101`, dependendo do protocolo. Para isolar, testar e modificar bits individuais desses campos, usam-se as **operações bit a bit** (seção 2).

### 1.12 Do valor apresentado ao valor transmitido

`f"{porta:016b}"` é só uma **representação textual** para visualização — ainda não são os bytes que de fato seriam transmitidos. O caminho completo que esta unidade percorre é:

```
informação → valor → representação binária → bytes → estrutura de protocolo → rede
```

---

## 2. Operações bit a bit

Campos de protocolo raramente são "só um número" — costumam combinar opções/flags em um único byte ou palavra. Os operadores **bit a bit** (*bitwise*) atuam diretamente sobre os bits de um inteiro (diferente dos operadores lógicos `and`/`or`, que trabalham com verdadeiro/falso):

| Operação | Operador |
|---|---|
| AND | `&` |
| OR | `\|` |
| XOR | `^` |
| NOT | `~` |
| Deslocamento à esquerda | `<<` |
| Deslocamento à direita | `>>` |

### 2.1 AND (`&`) — 1 só quando ambos são 1

```python
a = 0b1100
b = 0b1010
print(f"{a & b:04b}")  # 1000
```
Útil para **selecionar** determinados bits de um valor.

### 2.2 OR (`|`) — 1 quando pelo menos um é 1

```python
print(f"{0b1100 | 0b1010:04b}")  # 1110
```
Útil para **ativar** bits sem alterar os demais.

### 2.3 XOR (`^`) — 1 quando os bits são diferentes

```python
print(f"{0b1100 ^ 0b1010:04b}")  # 0110
```
Propriedade útil: aplicar XOR duas vezes com a mesma máscara **restaura** o valor original — por isso XOR serve para **alternar** (toggle) o estado de um bit.

### 2.4 NOT (`~`) — inverte todos os bits

Cuidado: inteiros Python **não têm tamanho fixo**. `~0b00001111` não dá `11110000` como se esperaria de um byte — dá um número negativo (representação interna sem limite de bits). Para restringir a 8 bits, aplique uma máscara:

```python
valor = 0b00001111
resultado = (~valor) & 0xFF
print(f"{resultado:08b}")  # 11110000
```

### 2.5 – 2.6 Deslocamento de bits (`<<` e `>>`)

Para inteiros não negativos, deslocar à esquerda equivale a multiplicar por 2 (por posição); deslocar à direita equivale a dividir por 2:

```python
print(1 << 0, 1 << 1, 1 << 2, 1 << 3)  # 1 2 4 8
```

### 2.7 – 2.8 Máscaras de bits e teste de um bit

Uma **máscara** seleciona/modifica posições específicas. Para testar o bit de posição `n` (numerada da direita para a esquerda, começando em 0):

```python
mascara = 1 << n
if valor & mascara:
    print("Bit ativado")
```

### 2.9 – 2.11 Ativar, desativar e alternar um bit

| Operação | Expressão |
|---|---|
| Testar bit `n` | `valor & (1 << n)` |
| Ativar bit `n` | `valor \|= (1 << n)` |
| Desativar bit `n` | `valor &= ~(1 << n)` |
| Alternar bit `n` | `valor ^= (1 << n)` |

### 2.12 Flags

Uma **flag** é tipicamente um bit que indica se uma característica está ativa. Exemplo com 4 flags em um byte:

```python
ACK      = 1 << 0
ERRO     = 1 << 1
URGENTE  = 1 << 2
RESPOSTA = 1 << 3

flags = ACK | URGENTE       # 00000101
if flags & ACK:
    print("ACK ativada")
```

### 2.13 Flags em protocolos reais — exemplo com DNS

Isso não é só didático: o cabeçalho DNS tem um campo de 16 bits com várias flags, entre elas **RD (Recursion Desired)**:

```python
RD = 1 << 8          # 0000000100000000
flags = 0
flags |= RD
if flags & RD:
    print("Recursão solicitada")
```

Ou seja: campos que a especificação chama de "opções" ou "flags" são, na mensagem real, apenas bits em posições predefinidas.

### 2.14 – 2.15 Extraindo e construindo campos com máscara + deslocamento

Um byte dividido em `TIPO` (4 bits altos) e `CÓDIGO` (4 bits baixos):

```python
valor = 0b10110110

codigo = valor & 0b00001111          # 6
tipo   = (valor >> 4) & 0b00001111   # 11

# caminho inverso — construir o byte a partir de tipo/código
valor = (tipo << 4) | codigo         # 10110110
```

O padrão `(valor >> deslocamento) & mascara` para extrair, e `(campo << deslocamento) | outro_campo` para construir, é **extremamente comum** na leitura/escrita de estruturas binárias reais.

---

## 3. Bytes em Python

Ao enviar/receber dados pela rede, o que chega à interface de sockets é sempre uma **sequência de bytes** — não texto, não números "soltos". É essencial distinguir três tipos em Python: `str` (texto), `bytes` (sequência imutável de bytes) e `bytearray` (sequência **mutável** de bytes).

### 3.1 – 3.2 `str` x `bytes`, literais

```python
texto = "IFRN"          # str
dados = b"IFRN"         # bytes — objeto DIFERENTE, mesmo "parecendo igual"
print(texto == dados)   # False

dados2 = b"\x01\x02\xff\x10"   # 4 bytes escritos em hex: valores 1, 2, 255, 16
print(len(dados2))             # 4
```

### 3.3 Um byte vale de 0 a 255

```python
dados = bytes([0, 1, 2, 53, 255])   # a partir de uma lista de inteiros
bytes([300])                        # ValueError: 300 não cabe em 1 byte
```

### 3.4 – 3.6 Indexação e slicing — uma diferença importante

```python
dados = b"\x01\x02\xff\x10"
dados[0]        # 1        (int!)
dados[-1]       # 16       (índice negativo, como em listas)
dados[1:3]      # b'\x02\xff'  (bytes! slicing preserva o tipo)
type(dados[0])   # <class 'int'>
type(dados[1:2]) # <class 'bytes'>
```

**Indexar um único elemento retorna `int`; fatiar (`slice`) retorna `bytes`.** Essa diferença é crucial ao extrair campos de mensagens recebidas.

### 3.7 Percorrendo bytes

```python
for valor in b"\x01\x02\xff\x10":
    print(f"{valor:02x}")   # 01 02 ff 10
```

### 3.8 – 3.9 Conversões: `hex()` e `bytes.fromhex()`

```python
dados = b"\x01\x02\xff\x10"
dados.hex()          # '0102ff10'
dados.hex(" ")        # '01 02 ff 10'
bytes.fromhex("01 02 ff 10")  # b'\x01\x02\xff\x10' (espaços são opcionais)
```

### 3.10 A partir de lista de inteiros

```python
bytes([1, 2, 255, 16]).hex()   # '0102ff10' — mesmo conteúdo de b"\x01\x02\xff\x10"
```

### 3.11 Concatenação e repetição

```python
mensagem = b"\x01\x02" + b"\xaa\xbb"     # 01 02 aa bb
zeros = b"\x00" * 8                       # 8 bytes zerados
```

### 3.12 – 3.13 `bytes` é imutável; `bytearray` é mutável

```python
dados = b"\x01\x02\x03"
dados[1] = 0xff        # TypeError: 'bytes' object does not support item assignment

editavel = bytearray(b"\x01\x02\x03")
editavel[1] = 0xff
bytes(editavel).hex()  # '01ff03' — bytearray → bytes ao final
```

Fluxo típico ao montar/editar uma estrutura: `bytes → bytearray (edita) → bytes`.

### 3.14 `bytes` e texto

```python
b"ABC".hex()   # '414243' — os caracteres também têm um valor numérico (ASCII/UTF-8)
```

### 3.15 Construindo uma pequena estrutura binária

Uma mensagem hipotética de 4 bytes — `Versão | Tipo | Flags | Código`:

```python
versao, tipo, flags, codigo = 1, 2, 5, 10
mensagem = bytes([versao, tipo, flags, codigo])
mensagem.hex(" ")   # '01 02 05 0a'

# interpretar de volta
print(mensagem[0], mensagem[1], mensagem[2], mensagem[3])  # 1 2 5 10
```

Combinando com flags da Seção 2:

```python
ACK, URGENTE = 1 << 0, 1 << 2
flags = ACK | URGENTE
mensagem = bytes([1, 2, flags, 10])
if mensagem[2] & ACK:
    print("ACK ativada")
```

`bits → flags → byte → mensagem`: é exatamente esse encadeamento de ideias que constrói um protocolo.

---

## 4. Texto, caracteres e codificação

`str` e `bytes` **não são equivalentes**, e a conversão entre eles exige uma **codificação de caracteres** — a regra que associa cada caractere a um ou mais bytes.

```
caractere → codificação → número(s) → byte(s)
```

### 4.1 – 4.3 ASCII e seus limites

**ASCII** define códigos para letras, dígitos e pontuação (`A=65=0x41`, `0=48=0x30`, etc.). Funciona bem para inglês, mas não cobre `ç`, `ã`, `€`, `你` etc. — `"ação".encode("ascii")` gera erro.

### 4.4 – 4.5 Unicode e UTF-8

**Unicode** define um code point abstrato para cada caractere (`A → U+0041`). **UTF-8** define *como* codificar esses code points em bytes, usando **quantidade variável** de bytes por caractere — caracteres ASCII continuam ocupando 1 byte; outros podem ocupar 2, 3 ou 4.

```python
"IFRN".encode("utf-8").hex()     # 4946524e — igual ao ASCII
"ação".encode("utf-8")            # mais bytes que caracteres (alguns usam >1 byte)
```

### 4.6 Caracteres ≠ bytes

```python
len("ação")                  # 4 (caracteres)
len("ação".encode("utf-8"))  # >4 (bytes) — não são necessariamente iguais!
```

Isso importa muito em protocolos que têm um campo de "comprimento": **sempre calcule o tamanho depois de `.encode()`**, nunca assuma que é igual a `len()` da string.

### 4.7 – 4.9 `encode()` / `decode()` e a necessidade de conhecer a codificação

```python
dados = "IFRN".encode("utf-8")   # str → bytes
texto = dados.decode("utf-8")    # bytes → str
```

O protocolo (ou a especificação da aplicação) precisa definir qual codificação usar — decodificar com a codificação errada produz lixo ou erro.

### 4.11 ASCII e UTF-8 coincidem para caracteres simples

```python
"DNS".encode("ascii") == "DNS".encode("utf-8")   # True
```
Por isso protocolos textuais antigos (baseados em ASCII) continuam compatíveis com clientes UTF-8 modernos, desde que usem só caracteres básicos.

### 4.16 Comprimento em caracteres x em bytes — regra prática

```python
nome = "www.ifrn.edu.br"
dados = nome.encode("ascii")
tamanho_para_o_protocolo = len(dados)   # NÃO len(nome)
```

### 4.19 Exemplo integrado: campo `tamanho + nome`

```python
nome = "IFRN"
nome_bytes = nome.encode("ascii")
mensagem = bytes([len(nome_bytes)]) + nome_bytes   # 04 49 46 52 4e

# desempacotando
tamanho = mensagem[0]
nome_recebido = mensagem[1:1 + tamanho].decode("ascii")   # "IFRN"
```

```
string → encode() → bytes → comprimento + conteúdo → mensagem
mensagem → slicing → bytes → decode() → string
```

Essa lógica se repete constantemente na construção de protocolos reais (ver o parsing de DNS em [`../03_camadas_aplicacao/dns_client_python3.py`](../03_camadas_aplicacao/dns_client_python3.py), que usa exatamente essa técnica para extrair os campos de nome de uma resposta).

---

## 5. Inteiros, bytes e ordem dos bytes

Falta conectar duas ideias: como transformar um `int` do Python em uma sequência de bytes de **tamanho e ordem bem definidos** — e vice-versa.

### 5.1 Python não tem inteiro de tamanho fixo

Diferente de C (`uint8`, `uint16`, `int32`...), o `int` do Python cresce livremente. Por isso, ao serializar, **você** precisa dizer quantos bytes usar.

### 5.2 – 5.6 Big-endian x little-endian

Um valor de 16 bits como `0x1234` pode ser escrito em dois bytes de duas formas:

| Ordem | Bytes |
|---|---|
| **Big-endian** (byte mais significativo primeiro) | `12 34` |
| **Little-endian** (byte menos significativo primeiro) | `34 12` |

O **valor lógico é o mesmo** — só a ordem de armazenamento/transmissão muda. Se emissor e receptor não combinarem a mesma ordem, `12 34` pode virar `0x1234` de um lado e `0x3412` do outro.

### 5.7 – 5.9 *Network byte order*

Nos protocolos TCP/IP, a convenção é transmitir campos multibyte em **network byte order = big-endian**. Uma porta como `8080` (`0x1f90`) aparece na rede como `1f 90`.

### 5.10 – 5.14 `int.to_bytes()`

```python
valor = 0x1234
valor.to_bytes(2, "big")      # b'\x12\x34'
valor.to_bytes(2, "little")   # b'\x34\x12'

(53).to_bytes(1, "big").hex()   # '35'
(53).to_bytes(4, "big").hex()   # '00000035' (mesmo valor, mais bytes reservados)

(256).to_bytes(1, "big")   # OverflowError: 256 não cabe em 1 byte

(-1).to_bytes(1, "big", signed=True).hex()    # 'ff' (complemento de dois)
```

### 5.15 – 5.17 `int.from_bytes()` — o caminho inverso

```python
int.from_bytes(b"\x12\x34", "big")     # 4660 (0x1234)
int.from_bytes(b"\x12\x34", "little")  # 13330 (0x3412)
```

**Os bytes não mudam — só a regra de interpretação muda.** Reforça a ideia central da unidade: bytes não carregam significado por si mesmos; é a especificação do protocolo que diz como lê-los.

```python
# ida e volta preservando o valor, desde que use a mesma ordem dos dois lados
dados = (8080).to_bytes(2, "big")
int.from_bytes(dados, "big")   # 8080
```

### 5.18 – 5.19 Extraindo e construindo campos de uma mensagem

Mensagem hipotética `Versão(1B) | Tipo(1B) | Porta(2B) | Dados(...)`:

```python
mensagem = bytes.fromhex("01 02 00 35 aa bb")

versao = mensagem[0]
tipo   = mensagem[1]
porta  = int.from_bytes(mensagem[2:4], "big")   # 53
dados  = mensagem[4:]                            # b'\xaa\xbb'

# construindo de volta
mensagem2 = (
    bytes([versao]) + bytes([tipo]) + porta.to_bytes(2, "big") + dados
)
```

### 5.20 – 5.23 Campos de 16/32 bits, IPv4 e portas TCP/UDP

- Campo de **16 bits** (porta): `valor.to_bytes(2, "big")`, intervalo 0–65535.
- Campo de **32 bits**: `valor.to_bytes(4, "big")`.
- Um endereço **IPv4** é, no nível binário, 4 octetos — `bytes([192, 168, 1, 10]).hex()` → `'c0a8010a'`.

### 5.24 Texto x binário para o mesmo valor

```python
porta = 53
str(porta).encode("ascii").hex()  # '3533' — os CARACTERES "5" e "3" em ASCII
porta.to_bytes(2, "big").hex()    # '0035' — o NÚMERO 53 em binário de 16 bits
```
São representações **completamente diferentes** do mesmo valor — o protocolo define qual delas usar.

### 5.25 Calculando o número mínimo de bytes (campos de tamanho variável)

```python
valor = 100000
bytes_necessarios = (valor.bit_length() + 7) // 8
```
Útil quando o protocolo usa comprimento variável; em campos de tamanho fixo, use sempre o tamanho definido na especificação.

---

## 6. Estruturas binárias com `struct`

Construir cada campo manualmente com `to_bytes()`/`from_bytes()` funciona, mas fica repetitivo à medida que a estrutura cresce. O módulo `struct` (biblioteca padrão) resolve isso descrevendo **toda a estrutura de uma vez**.

```python
import struct
```

### 6.1 – 6.2 `pack()` / `unpack()` — serialização e desserialização

```
valores Python → pack() → bytes → rede/arquivo → bytes → unpack() → valores Python
```

### 6.3 – 6.5 String de formato

```python
struct.pack("!BBHI", versao, tipo, identificador, comprimento)
```

| Caractere | Significado |
|---|---|
| `!` | *network byte order* (big-endian) — use sempre este para protocolos de rede |
| `B` | inteiro sem sinal de **1 byte** (0–255) |
| `H` | inteiro sem sinal de **2 bytes** (0–65535) |
| `I` | inteiro sem sinal de **4 bytes** (0–4294967295) |

`"!BBHI"` descreve 1+1+2+4 = **8 bytes**, na ordem exata dos parâmetros passados.

### 6.6 Primeiro exemplo

```python
dados = struct.pack("!H", 0x1234)
dados.hex()   # '1234'
```

### 6.7 – 6.10 Empacotando vários campos e comparando com o manual

```python
cabecalho = struct.pack("!BBHI", 1, 2, 0x1234, 1024)
cabecalho.hex(" ")   # '01 02 12 34 00 00 04 00'
```

Equivalente manual (mais verboso):

```python
dados = bytes([1]) + bytes([2]) + (0x1234).to_bytes(2, "big") + (1024).to_bytes(4, "big")
```

### 6.11 – 6.12 `unpack()`

```python
dados = bytes.fromhex("12 34 01 00")
id_transacao, flags = struct.unpack("!HH", dados)   # (4660, 256)
```

O formato precisa **corresponder exatamente** aos bytes — `"!HH"` (4 bytes) interpreta como dois inteiros de 16 bits; `"!I"` (também 4 bytes) interpretaria os *mesmos bytes* como um único inteiro de 32 bits. Os bytes não mudam; a interpretação, sim.

### 6.13 – 6.14 `calcsize()` — descobrindo o tamanho de um formato

```python
struct.calcsize("!HH")     # 4
struct.calcsize("!BBHI")   # 8
```

Muito útil para separar cabeçalho de payload por *slicing*:

```python
formato = "!BBHI"
tamanho = struct.calcsize(formato)
cabecalho, payload = mensagem[:tamanho], mensagem[tamanho:]
versao, tipo, identificador, comprimento = struct.unpack(formato, cabecalho)
```

### 6.17 Combinando `struct` com flags (bit a bit)

`struct` resolve a **serialização**; os operadores bit a bit (Seção 2) continuam necessários para **montar/interpretar** as flags dentro de um campo:

```python
ACK, ERRO, URGENTE = 1 << 0, 1 << 1, 1 << 2
flags = ACK | URGENTE

cabecalho = struct.pack("!BBH", 1, flags, 0x1234)
versao, flags_lidas, identificador = struct.unpack("!BBH", cabecalho)
if flags_lidas & ACK:
    print("ACK ativada")
```

### 6.18 – 6.19 Cabeçalho + payload de tamanho variável

```python
tipo, flags, identificador, payload = 1, 0, 25, b"IFRN"

cabecalho = struct.pack("!BBHH", tipo, flags, identificador, len(payload))
mensagem = cabecalho + payload

# do lado do receptor
formato = "!BBHH"
tamanho = struct.calcsize(formato)
tipo, flags, identificador, tamanho_payload = struct.unpack(formato, mensagem[:tamanho])
payload_recebido = mensagem[tamanho : tamanho + tamanho_payload]
```

### 6.21 `pack()` não converte texto sozinho

`struct` não sabe transformar `str` em `bytes` — codifique antes:

```python
nome_bytes = "IFRN".encode("ascii")
# só então incorpore nome_bytes na mensagem (concatenando ou com formato "Ns" do struct)
```

### 6.22 – 6.24 Prefixos de ordem de bytes

| Prefixo | Significado |
|---|---|
| `!` | network byte order (big-endian) — **use este para protocolos de rede** |
| `>` | big-endian |
| `<` | little-endian |

Para os formatos numéricos vistos aqui, `!` e `>` produzem o mesmo resultado; `!` é preferido em programação de redes por deixar explícita a intenção.

### 6.25 O valor precisa caber no formato

```python
struct.pack("!B", 256)   # struct.error: 256 não cabe em 1 byte (B vai até 255)
```

### 6.26 – 6.27 Exemplo: por que o cabeçalho DNS tem 12 bytes

Um cabeçalho DNS começa com 6 campos de 16 bits (ID, flags, QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT):

```python
formato = "!HHHHHH"
struct.calcsize(formato)   # 12 — exatamente o tamanho do cabeçalho DNS
```

Isso conecta diretamente com o parsing manual de DNS em [`../03_camadas_aplicacao/dns_client_python3.py`](../03_camadas_aplicacao/dns_client_python3.py), que lê esse mesmo cabeçalho (ali usando `struct.unpack("!H", ...)` byte a byte via slicing) antes de percorrer a *Answer Section*.

### 6.28 – 6.29 Funções de serialização/desserialização reutilizáveis

```python
def criar_cabecalho(versao, flags, identificador, tamanho):
    return struct.pack("!BBHH", versao, flags, identificador, tamanho)

def ler_cabecalho(dados):
    return struct.unpack("!BBHH", dados)
```

Encapsular `pack`/`unpack` em funções nomeadas é a base de qualquer implementação de protocolo próprio — ver a aplicação completa desse padrão em [`protocolo_binario_struct.py`](protocolo_binario_struct.py).

---

## Resumo da Unidade 4

- `n` bits representam `2ⁿ` valores; 8 bits = 1 byte = 2 dígitos hex.
- Operadores bit a bit (`& | ^ ~ << >>`) testam, ativam, desativam e alternam bits/flags dentro de um campo.
- `str` ≠ `bytes`: use `.encode()`/`.decode()` com uma codificação combinada entre as partes (tipicamente UTF-8); `len()` de string ≠ `len()` dos bytes codificados.
- `int.to_bytes(n, ordem)` / `int.from_bytes(dados, ordem)` convertem entre inteiro e bytes, respeitando **tamanho** e **ordem de bytes** (`"big"` = network byte order, padrão dos protocolos TCP/IP).
- `struct.pack(formato, ...)` / `struct.unpack(formato, dados)` descrevem uma estrutura binária inteira de uma vez (`!BBHI` etc.), evitando concatenar campo a campo manualmente; `struct.calcsize()` ajuda a separar cabeçalho de payload.

Com essas quatro unidades você tem o ciclo completo: **modelo cliente/servidor → API de sockets → concorrência → construção de protocolos binários**. Para exercitar tudo junto, veja [`exercicios_avancados.md`](exercicios_avancados.md).
