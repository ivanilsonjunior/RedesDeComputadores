# 📘 ICP-EDU: Assinatura Digital com Certificados Acadêmicos

## 🔐 1. Introdução

Este módulo apresenta um exemplo **real** de uso de criptografia
assimétrica utilizando certificados digitais emitidos pela **ICP-EDU**,
a Infraestrutura de Chaves Públicas da Comunidade Acadêmica Federada da
RNP.

O objetivo é que o aluno:

✔ gere seu próprio certificado digital ICP-EDU\
✔ entenda a cadeia de certificação (PKI)\
✔ converta o certificado para uso em Python / OpenSSL\
✔ assine digitalmente um documento\
✔ verifique a assinatura

------------------------------------------------------------------------

## 🏛️ 2. O que é a ICP-EDU?

A **ICP-EDU** é uma autoridade certificadora (AC) voltada para a
comunidade acadêmica brasileira:

🔗 https://pessoal.icpedu.rnp.br/home

Ela permite que alunos, professores e servidores emitam **certificados
pessoais gratuitos**, validados pela instituição.

------------------------------------------------------------------------

## 🔄 5. Convertendo o certificado

### Extrair chave privada

    openssl pkcs12 -in meucertificado.p12 -out chave_privada.pem -nocerts -nodes

### Extrair certificado público

    openssl pkcs12 -in meucertificado.p12 -out certificado_publico.pem -clcerts -nokeys

------------------------------------------------------------------------

## ✍️ Assinar documento (OpenSSL)

    openssl dgst -sha256 -sign chave_privada.pem -out assinatura.bin documento.txt

------------------------------------------------------------------------

## 🔍 Verificar assinatura (OpenSSL)

    openssl dgst -sha256 -verify certificado_publico.pem -signature assinatura.bin documento.txt

------------------------------------------------------------------------

## 🐍 Assinar em Python

``` python
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def assinar_documento(caminho_privada, arquivo):
    with open(caminho_privada, "rb") as f:
        chave = load_pem_private_key(f.read(), password=None)

    with open(arquivo, "rb") as f:
        dados = f.read()

    assinatura = chave.sign(
        dados,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    with open("assinatura.bin", "wb") as f:
        f.write(assinatura)
```

------------------------------------------------------------------------

## 🐍 Verificar assinatura em Python

``` python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def verificar_assinatura(cert_publico, arquivo, assinatura_arquivo):
    with open(cert_publico, "rb") as f:
        public_key = load_pem_public_key(f.read())

    with open(arquivo, "rb") as f:
        dados = f.read()

    with open(assinatura_arquivo, "rb") as f:
        assinatura = f.read()

    public_key.verify(
        assinatura,
        dados,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
```

------------------------------------------------------------------------

## 🧪 Exercício Final

1.  Emitir certificado na ICP-EDU\
2.  Converter para PEM\
3.  Assinar um documento\
4.  Verificar usando Python e OpenSSL
