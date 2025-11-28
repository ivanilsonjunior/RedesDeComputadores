# 📦 Criptografia --- Material de Apoio

**Disciplina: Segurança / Redes / IoT**\
Repositório com exemplos práticos de criptografia em Python, organizados
por temas: **simétrica, assimétrica, hash/HMAC e assinaturas digitais**.

------------------------------------------------------------------------

## 📁 Estrutura do Diretório

    Criptografia
    ├── Antigos/
    ├── Assimétrica/
    │   ├── Assinatura/
    │   ├── Basico/
    │   ├── ExemploHandShake/
    │   └── README.md
    ├── Hash/
    │   ├── Basico/
    │   └── README.md
    ├── Simétrica/
    │   ├── Arquivos/
    │   ├── Basicos/
    │   └── Blocos/
    └── README.md   ← (este arquivo)

A seguir, uma descrição clara de cada módulo.

------------------------------------------------------------------------

## 🔐 1. Criptografia Simétrica (`Simétrica/`)

Implementações que utilizam **a mesma chave para cifrar e decifrar**.

### 📂 `Simétrica/Arquivos/`

Scripts para **encriptação e decriptação de arquivos** completos. -
`encriptarArquivo.py`\
- `decriptarArquivo.py`

### 📂 `Simétrica/Basicos/cesar/`

Implementação clássica do **Cifra de César**: - `cesar.py`

### 📂 `Simétrica/Blocos/aes/`

Exemplos com **AES** em diferentes modos de operação: - `aes_ecb.py` ---
Electronic Codebook\
- `aes_cbc.py` --- Cipher Block Chaining\
- `aes_gnm.py` --- *Provavelmente AES-GCM, verifique o nome do arquivo*\
- `README.md` --- explicação dos modos

------------------------------------------------------------------------

## 🔑 2. Criptografia Assimétrica (`Assimétrica/`)

Exemplos com **chaves públicas/privadas**, RSA e assinaturas digitais.

### 📂 `Basico/`

Implementações fundamentais do RSA: - `gerarChavesRSA.py` --- gera par
de chaves\
- `cifrarRSA.py` --- cifra com chave pública\
- `decifrarRSA.py` --- decifra com chave privada

### 📂 `Assinatura/`

Demonstração de **assinatura digital** com RSA: - `assinarMensagem.py`\
- `verificarAssinatura.py`

### 📂 `ExemploHandShake/`

Mini protocolo estilo "handshake TLS simplificado": - `client.py` ---
cliente RSA\
- `server.py` --- servidor RSA\
- `gera_rsa_keys.py` --- gera chaves da demo\
- `README.md` --- explicação do protocolo

### 📄 README geral

O arquivo principal dentro de `Assimétrica/` explica os conceitos
básicos antes dos exemplos.

------------------------------------------------------------------------

## 🧮 3. Hashes, HMAC e Integridade (`Hash/`)

Exemplos práticos de funções hash, avalanche, salting e HMAC.

### 📂 `Hash/Basico/`

Scripts incluídos: - `sha256.py` --- cálculo de SHA-256\
- `hmac.py` --- HMAC com chave\
- `senhaSalt.py` --- salting de senhas\
- `avalanche.py` --- demonstração do efeito avalanche\
- `arquivo.py` --- hash de arquivos\
- `dados.txt` --- arquivo de teste

### 📄 README

Explicação geral do módulo de hash.

------------------------------------------------------------------------

## 📜 4. Antigos (`Antigos/`)

Versões anteriores dos scripts, mantidas por histórico e comparação: -
`Completo.py` - `Encrptar.py` - `Decriptar.py` - `GerarChave.py`

------------------------------------------------------------------------

## ▶️ Como Executar

Requer **Python 3** + bibliotecas padrão (a maioria sem dependências
externas).\
Alguns scripts podem exigir `pycryptodome`:

``` bash
pip install pycryptodome
```

Para executar qualquer arquivo:

``` bash
python3 nome_do_script.py
```

------------------------------------------------------------------------

## 🎯 Objetivo Didático

Este conjunto de códigos serve como base prática para:

-   Aulas de Segurança em IoT\
-   Demonstrações de cifragem em sistemas embarcados / transmissões
    inseguras\
-   Explicações sobre modos de operação do AES\
-   Visualização do efeito avalanche e hashing de arquivos\
-   Demonstrações completas de handshake assimétrico

------------------------------------------------------------------------

## 🤝 Contribuições

Sinta-se livre para:

-   Abrir PRs com melhorias\
-   Adicionar novos exemplos (ex.: ECC, ChaCha20, Argon2...)\
-   Corrigir nomenclaturas e comentários\
-   Propor exercícios práticos para os alunos

------------------------------------------------------------------------

## 📄 Licença

Material educacional produzido para fins didáticos nas disciplinas do
IFRN.\
Uso livre com atribuição.