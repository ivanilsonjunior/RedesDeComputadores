# 🔑 Criptografia Assimétrica --- Material de Apoio

Esta pasta reúne exemplos práticos, scripts e explicações sobre
**criptografia assimétrica**, com foco em:

-   Conceito de **par de chaves** (pública/privada)
-   Algoritmo **RSA** (básico e aplicado)
-   **Assinatura digital** de mensagens e arquivos
-   Handshake simplificado cliente/servidor
-   Integração com a **ICP-EDU** (RNP) e a ICP-Brasil
-   Assinatura digital de **PDFs (PAdES)**

O objetivo é oferecer uma visão **teórica sólida** e **prática aplicada** para disciplinas de Segurança, Redes e Sistemas Distribuídos do IFRN.

------------------------------------------------------------------------

## 1. Visão Geral da Criptografia Assimétrica

Na criptografia assimétrica, cada usuário possui um **par de chaves**:

-   **Chave privada (sk)**: mantida em segredo, usada para **decifrar** e **assinar**.
-   **Chave pública (pk)**: distribuída livremente, usada para **cifrar** e **verificar assinaturas**.

Duas propriedades fundamentais:

1.  O que é cifrado com a *chave pública* só pode ser decifrado com a *chave privada*.
2.  O que é assinado com a *chave privada* pode ser verificado com a *chave pública*.

Isso viabiliza:

-   comunicação segura sem chave pré-compartilhada
-   autenticação de origem
-   não repúdio (assinaturas digitais)
-   infraestrutura de chaves públicas (PKI)

------------------------------------------------------------------------

## 2. RSA --- Ideia Geral

O RSA é um dos algoritmos assimétricos mais estudados.

### 2.1. Geração de chaves (resumo conceitual)

1.  Escolher dois primos grandes: p e q
2.  Calcular n = p · q
3.  Calcular φ(n) = (p − 1)(q − 1)
4.  Escolher um expoente público e tal que 1 \< e \< φ(n) e mdc(e, φ(n)) = 1
5.  Calcular d como o inverso modular de e em relação a φ(n):
    d ≡ e⁻¹ (mod φ(n))

-   **Chave pública**: (n, e)
-   **Chave privada**: (n, d)

### 2.2. Cifragem e decifragem (visão matemática)

Dado um bloco de mensagem m (0 ≤ m \< n):

-   **Cifragem**: c = m\^e mod n
-   **Decifragem**: m = c\^d mod n

Na prática, bibliotecas cuidam de:

-   padding seguro (PKCS#1, OAEP)
-   blocos de dados
-   geração de primos grandes

------------------------------------------------------------------------

## 3. Estrutura da Pasta `Assimétrica/`

A organização geral é:

``` text
Assimétrica/
├── README.md               ← este arquivo
├── Basico/
│   ├── gerarChavesRSA.py   ← geração de chave RSA (didático)
│   ├── cifrarRSA.py        ← cifragem com chave pública
│   └── decifrarRSA.py      ← decifragem com chave privada
├── Assinatura/
│   ├── assinarMensagem.py  ← assinatura de mensagem simples
│   └── verificarAssinatura.py
├── ExemploHandShake/
│   ├── gera_rsa_keys.py
│   ├── client.py
│   ├── server.py
│   └── README.md
└── ICP-EDU/
    ├── assinar_documento.py
    ├── verificar_assinatura.py
    ├── PDF/
    │   ├── assinar_pdf.py
    │   ├── verificar_pdf.py
    │   └── README.md
    └── README.md
```

Cada subdiretório corresponde a um nível de complexidade e aplicação.

------------------------------------------------------------------------

## 4. Módulo Básico --- `Basico/`

### 4.1 Objetivo didático

Os scripts em `Basico/` têm foco **pedagógico**, para que o aluno:

-   visualize o fluxo de geração de chaves
-   entenda que RSA não é "mágica", mas **aritmética modular**
-   execute cifragem/decifragem em textos curtos ou dados simples

### 4.2 Scripts típicos

-   `gerarChavesRSA.py`
    -   Gera um par de chaves (pública e privada) em formatos simples ou PEM.
    -   Pode usar bibliotecas como `cryptography` ou `PyCryptodome`.
-   `cifrarRSA.py`
    -   Lê a chave pública
    -   Converte texto em bytes
    -   Cifra usando RSA + padding adequado
    -   Grava o resultado em um arquivo ou imprime em base64
-   `decifrarRSA.py`
    -   Lê a chave privada
    -   Decifra o ciphertext
    -   Recupera o texto original

------------------------------------------------------------------------

## 5. Assinatura Digital --- `Assinatura/`

### 5.1 Conceito

Assinar digitalmente é aplicar uma operação com a **chave privada** sobre um resumo (hash) da mensagem, de forma que qualquer pessoa, com a **chave pública**, possa verificar:

-   se a mensagem foi alterada\
-   se foi realmente emitida pelo detentor da chave privada

Fluxo típico:

1.  Calcular `h = H(m)` (hash criptográfico da mensagem m).
2.  Calcular assinatura `s = f_priv(h)` (ex.: s = h\^d mod n em RSA).
3.  Verificação: recomputar `h' = H(m)` e validar se `f_pub(s) == h'`.

### 5.2 Scripts

-   `assinarMensagem.py`
    -   Lê uma mensagem (texto ou arquivo).
    -   Calcula hash (por exemplo, SHA‑256).
    -   Assina com a chave privada usando RSA + padding adequado.
    -   Grava a assinatura em arquivo (ex.: `assinatura.bin`).
-   `verificarAssinatura.py`
    -   Lê a mensagem original e a assinatura.
    -   Recalcula o hash da mensagem.
    -   Usa a chave pública para verificar a assinatura.
    -   Informa se a assinatura é VÁLIDA ou INVÁLIDA.

------------------------------------------------------------------------

## 6. Handshake Simplificado --- `ExemploHandShake/`

Este diretório simula um **handshake criptográfico** entre cliente e
servidor.

### 6.1 Objetivos

-   Entender como chaves assimétricas podem ser usadas para:
    -   trocar segredos de forma segura
    -   autenticar a identidade das partes
-   Fazer um paralelo com protocolos reais (TLS, SSH, etc.), de maneira simplificada.

### 6.2 Arquivos principais

-   `gera_rsa_keys.py`
    -   Gera o par de chaves usadas no exemplo.
-   `server.py` e `client.py`
    -   Ilustram um fluxo onde o servidor envia sua chave pública
    -   O cliente usa essa chave para cifrar um segredo
    -   O servidor decifra com sua chave privada
    -   Podem ser estendidos para incluir assinatura e verificação de desafios

Mais detalhes de uso e execução estão no `ExemploHandShake/README.md`.

------------------------------------------------------------------------

## 7. Integração com ICP-EDU --- `ICP-EDU/`

Esta é uma das partes mais importantes e práticas do módulo.

### 7.1 O que é ICP-EDU?

A **ICP-EDU** é uma infraestrutura de chaves públicas voltada à comunidade acadêmica, vinculada à RNP, permitindo que alunos, docentes e técnicos emitam **certificados digitais pessoais** compatíveis com a ICP-Brasil.

-   Portal: https://pessoal.icpedu.rnp.br/home\
-   Formato típico recebido: `.p12` (contendo chave privada, certificado e cadeia)

### 7.2 Conteúdos desta pasta

-   Conversão de `.p12` para formatos `.pem` (chave privada e certificado público)
-   Assinatura digital de arquivos genéricos (ex.: `.txt`) usando:
    -   **OpenSSL** (linha de comando)
    -   **Python (`cryptography`)**
-   Verificação de assinaturas com a chave pública do certificado
-   Integração com fluxo de atividades da disciplina (ex.: aluno assina um relatório, código, ou declaração).

Scripts principais:

-   `assinar_documento.py`
-   `verificar_assinatura.py`
-   Scripts `.sh` com comandos OpenSSL (quando apropriado)
-   `README.md` com explicação passo a passo

------------------------------------------------------------------------

## 8. Assinatura Real de PDF (PAdES) --- `ICP-EDU/PDF/`

A subpasta `PDF/` leva a aplicação a um nível profissional:

-   Utiliza a biblioteca **PyHanko** em Python
-   Assina internamente o PDF no padrão **PAdES**
-   Resultados compatíveis com:
    -   Adobe Acrobat/Reader
    -   Sistemas que seguem ICP-Brasil/ETSI

### 8.1 Arquivos típicos

-   `assinar_pdf.py`
    -   Usa a chave privada e o certificado (ICP-EDU) para assinar `documento.pdf`.
    -   Gera `documento_assinado.pdf`.
-   `verificar_pdf.py`
    -   Usa PyHanko para inspecionar e validar as assinaturas internas do PDF.
-   `config.yaml`
    -   Configuração para uso da CLI `pyhanko sign`.
-   `README.md`
    -   Explica PAdES, fluxo de assinatura, validação e exercícios         propostos.

Esta parte do material aproxima o aluno da realidade de: - documentos assinados em sistemas oficiais (SEI, gov.br, etc.)\
- padrões modernos de assinatura digital e PKI.

------------------------------------------------------------------------

## 9. Requisitos de Ambiente

Para executar os exemplos desta pasta, recomenda-se:

``` bash
Python 3.10+
pip install cryptography pyhanko
sudo apt install openssl
```

Dependendo da distribuição, pode ser necessário instalar certificados de raiz da ICP-Brasil/ICP-EDU para validações avançadas.

------------------------------------------------------------------------

## 10. Objetivos de Aprendizagem

Ao estudar e praticar com o conteúdo desta pasta, o aluno deve ser capaz de:

-   Entender o modelo de par de chaves (pública/privada)
-   Compreender a lógica básica do RSA
-   Diferenciar cifragem e assinatura digital
-   Gerar e usar chaves RSA em scripts Python
-   Assinar e verificar mensagens e arquivos
-   Emitir e utilizar certificados ICP-EDU
-   Assinar PDFs com validade técnica e jurídica (PAdES)
-   Relacionar esses conceitos a protocolos reais (TLS, HTTPS, SSH, etc.)

------------------------------------------------------------------------

## 11. Sugestões de Uso em Sala de Aula

-   Atividades de laboratório com:
    -   geração de chaves
    -   cifragem de pequenos textos
    -   assinatura de arquivos `.txt`
    -   assinatura de PDFs com PyHanko
-   Trabalhos práticos:
    -   cada aluno assina digitalmente um relatório em PDF
    -   validação cruzada entre alunos (verificação da assinatura uns
        dos outros)
-   Integração com disciplinas de:
    -   Segurança da Informação
    -   Redes de Computadores
    -   Auditoria e Compliance Digital

------------------------------------------------------------------------

Este material foi desenvolvido para ser **reutilizável, extensível e alinhado com a prática profissional**, mantendo o foco didático para os cursos do IFRN.
