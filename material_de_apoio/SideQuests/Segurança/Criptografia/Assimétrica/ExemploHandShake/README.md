# 🔐 Handshake Completo: RSA + AES + HMAC via Socket

Este material demonstra um **protocolo criptográfico completo**, implementado em Python,
com foco didático para a disciplina de **Redes de Computadores / Segurança / IoT**.

O exemplo utiliza:
- **Criptografia Assimétrica (RSA)** para troca segura de chaves
- **Criptografia Simétrica (AES)** para confidencialidade
- **HMAC-SHA256** para integridade e autenticação
- **Sockets TCP** para comunicação em rede

⚠️ **Aviso importante**
Este código é **educacional** e **não substitui TLS/SSL em produção**.

---

## 🧠 Visão Geral do Protocolo

### 1️⃣ Geração de chaves (servidor)
- O servidor gera um par de chaves **RSA 2048 bits**.
- A **chave pública** é compartilhada com os clientes.
- A **chave privada** permanece apenas no servidor.

---

### 2️⃣ Handshake seguro (RSA)
1. O cliente gera:
   - `aes_key` → chave simétrica AES-256
   - `hmac_key` → chave secreta para HMAC-SHA256
   - `session_id` → identificador da sessão
2. Esses dados são concatenados e **cifrados com RSA-OAEP** usando a chave pública do servidor.
3. O servidor decifra usando sua chave privada RSA.
4. A sessão segura é estabelecida.

✅ Nenhum segredo é transmitido em texto plano.

---

### 3️⃣ Comunicação segura
Após o handshake:

- As mensagens são cifradas com **AES-CBC**
- Um **HMAC-SHA256** é calculado sobre:

```
session_id || seq || iv || ciphertext
```

- Um **número de sequência (`seq`)** previne ataques de replay

📌 Estratégia usada: **Encrypt-then-MAC** (boa prática criptográfica)

---

## 📁 Estrutura do Projeto

```
ExemploHandShake/
│
├── README.md
├── gera_rsa_keys.py
├── server.py
└── client.py
```

---

## 📦 Arquivos

| Arquivo | Função |
|-------|--------|
| `gera_rsa_keys.py` | Gera o par de chaves RSA do servidor |
| `server.py` | Servidor TCP que realiza o handshake e valida mensagens |
| `client.py` | Cliente que estabelece sessão segura e envia dados |

---

## ▶️ Como Executar

### 1️⃣ Instalar dependência
```bash
pip install cryptography
```

### 2️⃣ Gerar chaves RSA (uma única vez)
```bash
python gera_rsa_keys.py
```

Arquivos criados:
- `server_private_key.pem`
- `server_public_key.pem`

---

### 3️⃣ Iniciar o servidor
```bash
python server.py
```

---

### 4️⃣ Executar o cliente
```bash
python client.py "Mensagem segura de teste"
```

---

## 🔍 Conceitos Trabalhados

- Criptografia híbrida
- Troca segura de chaves
- Integridade e autenticação de mensagens
- Prevenção de replay
- Uso correto de IV
- Separação entre confidencialidade e integridade

---

## 🧑‍🏫 Uso Pedagógico

Indicado para:
- Redes de Computadores
- Segurança da Informação
- Segurança para IoT
- Aulas práticas e laboratórios

💡 Exercícios sugeridos:
- Substituir AES-CBC + HMAC por AES-GCM
- Implementar controle de sessão persistente
- Analisar falhas removendo o HMAC
- Comparar com TLS

---

🔐 Material educacional