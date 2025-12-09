# 🔐 Criptografia Simétrica --- Material de Apoio

A criptografia simétrica é um dos pilares fundamentais da segurança da informação.
Ela utiliza **uma única chave secreta** para cifrar e decifrar dados, oferecendo alto desempenho e sendo amplamente aplicada em:

-   redes de computadores (TLS, VPNs, WPA2/WPA3);
-   armazenamento seguro (criptografia de disco);
-   sistemas embarcados e IoT;
-   criptografia de arquivos e backups;
-   protocolos industriais e de tempo real.

Este diretório contém exemplos acadêmicos, demonstrativos e práticos
para compreender desde cifras clássicas até algoritmos modernos como
AES.

------------------------------------------------------------------------

# 📁 Estrutura da Pasta `Simétrica/`

    Simétrica/
    ├── README.md               ← este arquivo
    ├── Basicos/
    │   ├── cesar/
    │   │   ├── cesar.py
    │   │   └── README.md
    │   └── cesar_ciclica/
    │       ├── cyclic_cesar.py
    │       └── README.md
    ├── Blocos/
    │   └── aes/
    │       ├── aes_ecb.py
    │       ├── aes_cbc.py
    │       ├── aes_gnm.py
    │       └── README.md
    └── Arquivos/
        ├── encriptarArquivo.py
        ├── decriptarArquivo.py
        └── README.md

Cada módulo cobre um nível diferente de abstração:
**cifras didáticas → criptografia real de blocos → criptografia aplicada a arquivos.**

------------------------------------------------------------------------

# 🔎 1. Conceitos Centrais da Criptografia Simétrica

A criptografia simétrica opera com uma única chave **K**:

-   Cifragem: `C = EK(P)`
-   Decifragem: `P = DK(C)`

Onde:

-   **P**: plaintext (mensagem original)
-   **C**: ciphertext (mensagem cifrada)
-   **EK()**: função de cifragem usando K
-   **DK()**: função de decifragem usando K

### Propriedades desejáveis

-   Difusão e confusão
-   Avalanche
-   Resistência a ataques estatísticos
-   Chaves suficientemente grandes
-   Modos de operação corretos

------------------------------------------------------------------------

# 🟦 2. Cifras Didáticas --- `Basicos/`

Esta seção inclui implementações **pedagógicas**, úteis para entender os
princípios básicos de como textos podem ser transformados por cifras.

## 2.1 Cifra de César (clássica)

-   Uma das cifras mais antigas do mundo.
-   Usa deslocamento fixo no alfabeto.
-   Insegura, mas excelente para fins didáticos.

📌 Arquivo: `Basicos/cesar/cesar.py`

## 2.2 Cifra de César Cíclica (Orientada a Objetos)

Implementação moderna criada para este repositório:

-   chave composta por vários deslocamentos (ex.: `[1,2,3]`);
-   deslocamentos aplicados ciclicamente;
-   suporta decifragem usando deslocamento inverso;
-   estruturada em **classe** (`CyclicCaesarCipher`);
-   útil para comparar cifras clássicas vs. modernas.

📌 Pasta: `Basicos/cesar_ciclica/`

------------------------------------------------------------------------

# 🟧 3. Criptografia de Blocos --- `Blocos/aes/`

O AES (Advanced Encryption Standard) é o algoritmo de criptografia
simétrica mais utilizado no mundo.

Características:

-   Blocos de **128 bits**
-   Chaves de **128 / 192 / 256 bits**
-   Seguro e eficiente
-   Usado em TLS, VPNs, Wi-Fi (WPA2/WPA3), 5G, bancos, governo

## 3.1 Modos de Operação

AES puro cifra apenas blocos fixos.
Para trabalhar com dados maiores, são usados modos de operação:

### **ECB --- Electronic Codebook**

-   Cada bloco é cifrado independentemente.
-   **INSEGURO**, pois mantém padrões.
-   Usado aqui apenas para fins didáticos.

📌 Arquivo: `aes_ecb.py`

------------------------------------------------------------------------

### **CBC --- Cipher Block Chaining**

-   Cada bloco depende do bloco anterior.
-   Usa IV (vetor de inicialização).
-   Muito mais seguro que ECB.

📌 Arquivo: `aes_cbc.py`

------------------------------------------------------------------------

### **GCM --- Galois Counter Mode**

-   Oferece **confidencialidade + integridade** (AEAD).
-   Utilizado em TLS 1.2+, SSH, VPNs modernas.
-   Requer nonce único por chave.

📌 Arquivo: `aes_gnm.py`

------------------------------------------------------------------------

# 🟨 4. Criptografia de Arquivos --- `Arquivos/`

Scripts para cifrar e decifrar arquivos completos (`.txt`, `.pdf`,
`.bin`, etc.) usando AES.

-   Utilizam chave e IV gerados por funções seguras.
-   Boa introdução à criptografia aplicada.
-   Permitem experimentação com arquivos reais.

Scripts:

-   `encriptarArquivo.py`
-   `decriptarArquivo.py`

📌 Pasta: `Simétrica/Arquivos/`

------------------------------------------------------------------------

# 📘 5. Comparação das Abordagens

  ---------------------------------------------------------------------------
  Tipo                     Exemplos               Segurança   Objetivo
                                                              didático
  ------------------------ ---------------------- ----------- ---------------
  Cifras clássicas         César, César Cíclica   ❌ baixa    aprender
                                                              conceitos

  Cifras modernas (AES)    CBC, GCM               ✅ alta     uso
                                                              profissional

  Criptografia de arquivos AES + arquivos reais   ✅ alta     prática
                                                              aplicada
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

# 🧪 6. Requisitos para Executar os Exemplos

    Python 3.10+
    pip install cryptography
    sudo apt install openssl

Para testes com arquivos grandes, recomenda-se:

-   boa entropia (geração de chaves seguras);
-   cuidado com o armazenamento da chave;
-   NÃO reutilizar IV/nonce no AES-GCM.

------------------------------------------------------------------------

# 🎓 7. Objetivos de Aprendizagem

O aluno deve ser capaz de:

-   distinguir cifras de substituição, fluxo e blocos;
-   entender por que ECB é inseguro;
-   usar CBC corretamente com IV único;
-   usar GCM para garantir confidencialidade + integridade;
-   aplicar cifras em arquivos reais;
-   compreender diferenças entre cifras clássicas e modernas.

------------------------------------------------------------------------

# 🤝 8. Sugestões de Atividades

-   Implementar uma cifra própria baseada em deslocamentos.
-   Comparar ECB vs CBC visualmente com uma imagem.
-   Criptografar um arquivo e enviá-lo para outro aluno decifrar.
-   Criar APIs simples que cifram mensagens usando AES.
-   Medir tempos de execução do AES com diferentes tamanhos de chave.

------------------------------------------------------------------------

Este material fornece bases sólidas para disciplinas de **Redes**,
**Segurança**, **Sistemas Embarcados**, **IoT** e **Criptografia
Aplicada**.
