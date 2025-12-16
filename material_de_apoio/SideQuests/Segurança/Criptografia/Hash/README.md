# 🧮 Criptografia --- Hash, HMAC e Integridade de Dados

Este diretório reúne **exemplos práticos e educativos** de funções de
hash criptográfico, HMAC e verificação de integridade de dados, com
enfoque no uso pedagógico para aulas de Segurança, Redes ou IoT.

## 📚 Objetivos e Justificativas

-   Apresentar **funções hash criptográficas** como ferramentas de
    integridade de dados e "impressão digital" de mensagens/arquivos.\
-   Demonstrar **HMAC** (Hash‑Based Message Authentication Code) como
    mecanismo para garantir **integridade + autenticidade**, usando
    hash + chave secreta compartilhada.\
-   Permitir testes práticos de salting de senhas, hashing de arquivos,
    verificação de integridade e avalanche de hash --- ilustrando
    vulnerabilidades e vantagens.\
-   Servir como base didática para uso em sistemas embarcados, IoT ou
    aplicações de redes, com código em Python e fácil adaptação.
Funções hash criptográficas são usadas para **garantir a integridade dos dados**,
verificando se uma informação foi alterada durante armazenamento ou transmissão.

Diferente da criptografia:
- Hash não usa chave
- Hash não é reversível
- Hash não esconde informações

Principais Características:
- Mesma entrada gera sempre o mesmo hash
- Saída de tamanho fixo
- Pequena alteração gera grande mudança (efeito avalanche)
- Impossível reverter o hash para a mensagem original
- Resistência a colisões

## Algoritmos
### ❌ Obsoletos (não usar)
- MD5
- SHA-1



### ✅ Recomendados
- SHA-256
- SHA-512
- SHA-3

Neste material utilizamos **SHA-256**.

## Hash × Criptografia

| Hash | Criptografia Simétrica |
|------|------------------------|
| Não usa chave | Usa chave |
| Não reversível | Reversível |
| Integridade | Confidencialidade |

---

## Aplicações em Redes e IoT
- Verificação de integridade de mensagens
- Autenticação de dispositivos
- Atualização segura de firmware
- HTTPS, MQTT seguro, TLS


## 🔎 Fundamentos Teóricos

-   **Função hash criptográfica**: transforma dados de tamanho
    arbitrário em um valor fixo ("digest/hash"), de forma
    determinística, irreversível (one‑way) e com forte sensibilidade a
    alterações nos dados.\
-   **Propriedades importantes**: pre‑image resistance, second pre‑image
    resistance, resistência a colisões.\
-   **Usos típicos**: verificação de integridade, autenticação simples,
    impressão digital de arquivos, comparação de dados, salting de
    senhas.\
-   **HMAC**: mecanismo baseado em hash + chave secreta, garantindo
    integridade e autenticidade.\
-   Comparação: Hash simples → integridade; HMAC → integridade +
    autenticidade.

## 📂 Organização dos Exemplos

    Hash/
    ├── Basico/
    │   ├── sha256.py
    │   ├── hmac.py
    │   ├── senhaSalt.py
    │   ├── avalanche.py
    │   ├── arquivo.py
    │   └── dados.txt
    └── README.md

### Exemplos e suas finalidades

-   **`sha256.py`** --- cálculo de SHA‑256.\
-   **`hmac.py`** --- geração de HMAC.\
-   **`senhaSalt.py`** --- hashing de senhas com salt.\
-   **`avalanche.py`** --- demonstração do efeito avalanche.\
-   **`arquivo.py`** --- hashing de arquivos.

## ✅ Como Utilizar / Testar

``` bash
python3 nome_do_script.py
```

## 📖 Extensões Pedagógicas

-   Comparação entre algoritmos hash.\
-   Discussão sobre ataques (colisão, pre‑image, length‑extension).\
-   Uso de hash em IoT e sistemas embarcados.\
-   Construção de autenticação simples via HMAC.

## 🎓 Contextualização Acadêmica

Este material permite ao aluno relacionar:\
- fundamentos matemáticos → comportamento prático dos algoritmos,\
- teoria da segurança → implementação real,\
- integridade/autenticidade → mecanismos práticos como HMAC,\
- boas práticas → segurança em ambientes restritos como IoT.