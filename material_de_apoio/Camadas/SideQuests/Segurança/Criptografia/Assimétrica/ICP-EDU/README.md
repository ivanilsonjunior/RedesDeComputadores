# 🏛️ ICP-EDU --- Certificados Digitais e Assinatura de Documentos

Esta pasta contém exemplos práticos de uso da **ICP-EDU**
(Infraestrutura de Chaves Públicas da Comunidade Acadêmica Federada da
RNP) para:

-   emitir e utilizar **certificados digitais pessoais**;
-   assinar digitalmente **arquivos genéricos** (ex.: `.txt`);
-   assinar digitalmente **PDFs** no padrão **PAdES** (via subpasta
    `PDF/`);
-   verificar assinaturas usando **Python**, **OpenSSL** e **PyHanko**.

O objetivo é aproximar o aluno de um cenário **real de PKI**, muito
próximo do que é utilizado em órgãos públicos, sistemas acadêmicos e
governo eletrônico.

------------------------------------------------------------------------

## 1. O que é a ICP-EDU?

A **ICP-EDU** é uma infraestrutura de chaves públicas voltada à
comunidade acadêmica brasileira, mantida pela RNP.\
Ela permite que **alunos, professores e técnicos** emitam **certificados
digitais pessoais**, normalmente vinculados ao e-mail institucional.

Características principais:

-   baseada no modelo de PKI (similar à ICP-Brasil);
-   emite certificados no padrão X.509;
-   permite autenticação e assinatura digital;
-   gratuito para a comunidade acadêmica vinculada.

Portal de emissão:\
➡️ `https://pessoal.icpedu.rnp.br/home`

------------------------------------------------------------------------

## 2. Fluxo Geral de Uso neste Módulo

1.  Emitir um certificado pessoal pela ICP-EDU (`.p12`);
2.  Converter o `.p12` para arquivos em formato **PEM**:
    -   `chave_privada.pem`
    -   `certificado_publico.pem`
3.  Usar esses arquivos para:
    -   assinar e verificar documentos de texto (scripts desta pasta);
    -   assinar e verificar PDFs (subpasta `PDF/`).

------------------------------------------------------------------------

## 3. Estrutura da Pasta `ICP-EDU/`

``` text
ICP-EDU/
├── README.md                        ← este arquivo
├── assinar_documento.py             ← assinatura digital de arquivos genéricos
├── verificar_assinatura.py          ← verificação de assinaturas
├── assinar_documento_openssl.sh     ← script bash com OpenSSL
├── verificar_assinatura_openssl.sh  ← script bash com OpenSSL
└── PDF/                             ← assinatura de PDF (PAdES, PyHanko)
    ├── assinar_pdf.py
    ├── verificar_pdf.py
    ├── config.yaml
    ├── FluxoAssinatura.png
    └── README.md
```

------------------------------------------------------------------------

## 4. Emissão do Certificado ICP-EDU

### 4.1 Acesso ao portal

1.  Acesse: `https://pessoal.icpedu.rnp.br/home`
2.  Autentique-se com sua credencial institucional (IFRN).
3.  Procure a opção de **"Emitir certificado pessoal"**.
4.  Siga o fluxo do portal até a emissão.

O certificado geralmente é baixado no formato:

``` text
meucertificado.p12
```

Esse arquivo `.p12` (PKCS#12) contém:

-   sua **chave privada** (protegida por senha);
-   seu **certificado digital**;
-   parte ou toda a **cadeia de certificação**.

------------------------------------------------------------------------

## 5. Conversão do `.p12` para PEM

Os scripts desta pasta trabalham com **arquivos PEM** separados:

-   `chave_privada.pem` --- contém APENAS a chave privada;
-   `certificado_publico.pem` --- contém APENAS o certificado público.

### 5.1 Extrair chave privada

``` bash
openssl pkcs12 -in meucertificado.p12 -out chave_privada.pem -nocerts -nodes
```

-   `-nocerts`: não extrai certificados, apenas a chave;
-   `-nodes`: não recriptografa a chave privada ao salvar (cuidado com
    segurança!).

### 5.2 Extrair certificado público

``` bash
openssl pkcs12 -in meucertificado.p12 -out certificado_publico.pem -clcerts -nokeys
```

-   `-clcerts`: extrai apenas o certificado de usuário;
-   `-nokeys`: não extrai a chave privada.

Depois disso, você terá:

``` text
chave_privada.pem
certificado_publico.pem
```

Esses arquivos serão usados pelos scripts em Python e OpenSSL.

------------------------------------------------------------------------

## 6. Assinatura Digital de Arquivos (Python)

### 6.1 Script `assinar_documento.py`

Função principal:\
Assinar o conteúdo de um arquivo (por exemplo, `documento.txt`) usando a
**chave privada** ICP-EDU em formato PEM.

Uso típico:

``` bash
python assinar_documento.py -k chave_privada.pem -i documento.txt -o assinatura.bin
```

Parâmetros:

-   `-k` / `--key`: caminho para a chave privada (`chave_privada.pem`);
-   `-i` / `--input`: arquivo a ser assinado (`documento.txt`);
-   `-o` / `--output`: arquivo de saída da assinatura (`assinatura.bin`,
    por padrão).

Fluxo interno:

1.  Lê a chave privada em PEM;
2.  Lê o conteúdo do arquivo de entrada em binário;
3.  Gera hash com SHA-256;
4.  Assina usando RSA + PKCS#1 v1.5;
5.  Grava a assinatura no arquivo especificado.

------------------------------------------------------------------------

## 7. Verificação de Assinatura (Python)

### 7.1 Script `verificar_assinatura.py`

Uso típico:

``` bash
python verificar_assinatura.py -c certificado_publico.pem -i documento.txt -s assinatura.bin
```

Parâmetros:

-   `-c` / `--cert`: certificado público em PEM
    (`certificado_publico.pem`);
-   `-i` / `--input`: arquivo original (`documento.txt`);
-   `-s` / `--signature`: arquivo de assinatura (`assinatura.bin`).

Fluxo interno:

1.  Lê o certificado público;
2.  Extrai a chave pública;
3.  Recalcula o hash do arquivo original;
4.  Verifica se a assinatura é válida para aquele conteúdo;
5.  Informa se a assinatura é **VÁLIDA** ou **INVÁLIDA**.

------------------------------------------------------------------------

## 8. Assinatura com OpenSSL (scripts `.sh`)

Além dos scripts Python, existem também scripts Bash que usam **OpenSSL
diretamente**:

### 8.1 `assinar_documento_openssl.sh`

Uso:

``` bash
chmod +x assinar_documento_openssl.sh
./assinar_documento_openssl.sh chave_privada.pem documento.txt assinatura.bin
```

Se `assinatura.bin` não for informado, esse será o nome padrão.

Internamente, o comando central é:

``` bash
openssl dgst -sha256 -sign chave_privada.pem -out assinatura.bin documento.txt
```

------------------------------------------------------------------------

### 8.2 `verificar_assinatura_openssl.sh`

Uso:

``` bash
chmod +x verificar_assinatura_openssl.sh
./verificar_assinatura_openssl.sh certificado_publico.pem documento.txt assinatura.bin
```

Internamente, o comando é:

``` bash
openssl dgst -sha256 -verify certificado_publico.pem -signature assinatura.bin documento.txt
```

------------------------------------------------------------------------

## 9. Assinatura de PDF (PAdES) --- Subpasta `PDF/`

A pasta `ICP-EDU/PDF/` estende o uso da ICP-EDU para **PDFs assinados
internamente**, no padrão PAdES, utilizando a biblioteca **PyHanko**.

Conteúdos principais:

-   `assinar_pdf.py` --- assina `documento.pdf` gerando
    `documento_assinado.pdf`;
-   `verificar_pdf.py` --- valida assinaturas internas do PDF;
-   `config.yaml` --- configuração de assinante para CLI `pyhanko sign`;
-   `FluxoAssinatura.png` --- diagrama do fluxo completo;
-   `README.md` --- explicação detalhada focada apenas em PDFs.

Recomenda-se consultar o `README.md` da pasta `PDF/` para detalhes
específicos sobre PAdES.

------------------------------------------------------------------------

## 10. Requisitos de Ambiente

Para utilizar tudo que está nesta pasta, recomenda-se:

``` bash
Python 3.10+
pip install cryptography pyhanko
sudo apt install openssl
```

Em distribuições Linux, pode ser necessário:

-   instalar certificados raiz da ICP-Brasil/ICP-EDU para validações
    avançadas;
-   configurar o repositório de certificados confiáveis (opcional,
    dependendo do uso).

------------------------------------------------------------------------

## 11. Objetivos Educacionais

Ao concluir as atividades relacionadas a esta pasta, o aluno deverá ser
capaz de:

-   entender a relação entre **certificados digitais**, chaves
    públicas/privadas e identidade;
-   emitir e utilizar um certificado pessoal na **ICP-EDU**;
-   assinar e verificar digitalmente arquivos genéricos;
-   compreender a estrutura de um arquivo `.p12` e sua conversão para
    `.pem`;
-   utilizar ferramentas de baixo nível (**OpenSSL**) e alto nível
    (**Python + cryptography + PyHanko**);
-   aplicar os conceitos em cenários reais:
    -   envio de arquivos assinados;\
    -   relatórios com assinatura digital;\
    -   PDFs com validade técnica e jurídica.

------------------------------------------------------------------------

## 12. Sugestão de Atividade Prática

1.  Emitir um certificado digital pessoal na ICP-EDU.\
2.  Converter o `.p12` em `chave_privada.pem` e
    `certificado_publico.pem`.\
3.  Criar um arquivo `relatorio.txt` com um pequeno texto.\
4.  Assinar o arquivo com `assinar_documento.py`.\
5.  Verificar a assinatura com `verificar_assinatura.py`.\
6.  Criar um `relatorio.pdf` e assiná-lo usando os scripts da pasta
    `PDF/`.\
7.  Verificar a assinatura do PDF com:
    -   `verificar_pdf.py`;\
    -   Adobe Reader (verificando a cadeia de confiança).

------------------------------------------------------------------------

Este módulo integra **conceitos teóricos de criptografia assimétrica**
com **casos reais de uso de certificados digitais** na comunidade
acadêmica, aproximando a disciplina de Segurança/Redes do contexto
profissional e governamental.
