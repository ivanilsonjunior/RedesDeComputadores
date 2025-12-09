# 🔐 Módulo de Criptografia --- Material de Apoio (IFRN)

Este diretório reúne exemplos práticos, código‑fonte, exercícios e
explicações didáticas sobre **Criptografia Simétrica**, **Criptografia
Assimétrica**, **Assinatura Digital**, **Hashing**, **ICP‑EDU** e
**PAdES**, totalmente alinhados às disciplinas de Segurança e Redes do
IFRN.

O objetivo é permitir que o aluno compreenda e utilize, na prática:

-   Comunicação segura\
-   Armazenamento criptografado\
-   Assinatura de mensagens e documentos\
-   Certificados digitais ICP‑Brasil / ICP‑EDU\
-   Hashes criptográficos e HMAC\
-   Algoritmos clássicos e modernos

------------------------------------------------------------------------

# 📁 Estrutura Geral do Diretório

    Criptografia/
    ├── README.md                 ← este arquivo (visão geral)
    ├── Simétrica/                ← cifragem com chave secreta
    ├── Assimétrica/              ← RSA, certificados e ICP‑EDU
    ├── Hash/                     ← hash, HMAC, avalanche, salt
    └── Antigos/                  ← códigos antigos / referência histórica

------------------------------------------------------------------------

# 🟦 1. Criptografia Simétrica (`Simétrica/`)

Mecanismos que utilizam **uma única chave secreta** para cifrar e
decifrar.

### Conteúdos disponíveis

-   **Cifra de César clássica** (`Basicos/cesar/`)
-   **Cifra de César avançada (3‑chaves / cíclica OO)**
    (`Cesar3Chaves/`)
-   **AES (ECB, CBC, GCM\*)**\
    \* *O arquivo `aes_gnm.py` é a implementação GCM (correção de
    nome).*
-   **Criptografia de arquivos** (`Arquivos/`)

### Pontos importantes abordados

-   Modos de operação de blocos (ECB, CBC, GCM)
-   Importância de IV e nonce
-   Por que **ECB é inseguro**
-   Segurança do AES‑GCM
-   Padding e tamanho de bloco
-   Diferença entre cifras clássicas e modernas

📌 Pasta: [`Simétrica/`](Simétrica/)

------------------------------------------------------------------------

# 🟩 2. Criptografia Assimétrica (`Assimétrica/`)

Mecanismos baseados em **par de chaves**:

🔑 **chave privada** (secreta)\
🔓 **chave pública** (distribuída livremente)

### Conteúdos disponíveis

-   Geração de chaves RSA
-   Cifra e decifra com RSA
-   Assinatura e verificação de mensagens
-   Handshake cliente/servidor (ExemploHandShake/)
-   **Integração completa com ICP‑EDU**
-   **Assinatura de PDFs no padrão PAdES (Adobe / SEI)**

### Novidades

-   Pasta `ICP-EDU/` com fluxo real de uso de certificado (p12 → PEM)
-   Scripts Python para assinar/verificar documentos
-   Scripts OpenSSL equivalentes
-   Submódulo `PDF/` para assinatura digital interna (PyHanko)

📌 Pasta: [`Assimétrica/`](Assimétrica/)

------------------------------------------------------------------------

# 🟥 3. Funções Hash e HMAC (`Hash/`)

Funções de hash criptográficas são usadas para:

-   Integridade de dados\
-   Armazenamento seguro de senhas\
-   Autenticação (HMAC)\
-   Efeito avalanche\
-   Hash de arquivos

### Conteúdos disponíveis

-   `sha256.py` --- hashing didático
-   `hmac.py` --- autenticação com chave
-   `senhaSalt.py` --- geração de senha com *salt*
-   `arquivo.py` --- hash de arquivos completos
-   `avalanche.py` --- demonstração do efeito avalanche

📌 Pasta: [`Hash/`](Hash/)

------------------------------------------------------------------------

# 🕰️ 4. Conteúdos Legados (`Antigos/`)

Esta pasta contém códigos antigos usados em versões prévias do módulo de
criptografia.\
Mantida apenas para referência histórica e comparação acadêmica.

📌 Pasta: [`Antigos/`](Antigos/)

------------------------------------------------------------------------

# 🏛️ 5. Integração com ICP‑EDU / ICP‑Brasil

O aluno aprende a utilizar **certificados reais** emitidos pela ICP‑EDU:

🔗 https://pessoal.icpedu.rnp.br/home

Conteúdo:

-   Conversão `.p12` → `.pem`
-   Assinatura digital de arquivos comuns
-   Assinatura digital **interna** de PDF (PAdES)
-   Validação por PyHanko e Adobe Reader
-   Fluxos reais usados em sistemas como SEI

📌 Pasta: [`Assimétrica/ICP-EDU/`](Assimétrica/ICP-EDU/)

------------------------------------------------------------------------

# 📘 6. Material para Salas de Aula

Este diretório foi otimizado para:

-   Projetos práticos de laboratório
-   Exercícios de criptografia aplicada
-   Aulas demonstrativas
-   Integração com disciplinas de Segurança, Redes e IoT
-   Estudo avançado com ferramentas modernas (cryptography, PyHanko,
    OpenSSL)

------------------------------------------------------------------------

# 🧪 7. Requisitos Recomendados

    Python 3.10+
    pip install cryptography pyhanko
    sudo apt install openssl

------------------------------------------------------------------------

# 🎓 8. Objetivos Educacionais

Ao finalizar este módulo, o aluno será capaz de:

-   Diferenciar simétrica × assimétrica × hashing
-   Usar AES corretamente
-   Gerar e manejar chaves RSA
-   Assinar e verificar mensagens
-   Emitir e usar certificados ICP‑EDU
-   Assinar PDFs no padrão PAdES
-   Validar assinaturas com ferramentas profissionais

------------------------------------------------------------------------

# 🤝 9. Contribuição

Pull requests com novos exemplos, algoritmos e melhorias são bem‑vindos.

------------------------------------------------------------------------

# 🏁 10. Licença

Material de uso **educacional**, livre para utilização em cursos,
projetos e atividades do IFRN.

------------------------------------------------------------------------

Material desenvolvido com foco didático para disciplinas de **Redes**,\
**Segurança da Informação**, **IoT** e **Sistemas Embarcados**.
