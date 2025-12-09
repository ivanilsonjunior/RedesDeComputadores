# 🔐 Módulo de Criptografia --- Material de Apoio (IFRN)

Este diretório reúne exemplos práticos, código-fonte, exercícios e
explicações didáticas sobre **Criptografia Simétrica**, **Criptografia
Assimétrica**, **Assinatura Digital**, **Hashing**, **ICP-EDU**, e
**PAdES**, organizados conforme as trilhas de Segurança e Redes do IFRN.

O objetivo deste material é fornecer ao aluno um conjunto sólido de
ferramentas e conceitos para compreender, testar e aplicar técnicas
reais de criptografia utilizadas em sistemas modernos, incluindo:

-   Comunicação segura\
-   Armazenamento criptografado\
-   Assinatura de mensagens e documentos\
-   Certificados digitais ICP-Brasil / ICP-EDU\
-   Hashes criptográficos e HMAC\
-   Algoritmos clássicos e modernos

------------------------------------------------------------------------

# 📁 Estrutura Geral do Diretório

    Criptografia/
    ├── README.md                ← este arquivo (visão geral)
    ├── Simétrica/               ← cifragem com chave secreta
    ├── Assimétrica/             ← RSA, certificados e ICP-EDU
    └── Hash/                    ← funções de hash, HMAC e avalanche

------------------------------------------------------------------------

# 🟦 1. Criptografia Simétrica (`Simétrica/`)

Mecanismos que utilizam **uma única chave secreta** para cifrar e
decifrar.

### Conteúdos disponíveis:

-   **Cifra de César (básica e avançada/cíclica OO)**\
-   **AES (ECB, CBC, GCM)**\
-   **Criptografia de arquivos (streaming e blocos)**\
-   **Exemplos práticos com Python e OpenSSL**

### Pontos importantes abordados:

-   Modos de operação de blocos\
-   Importância do IV e nonce\
-   Segurança do AES GCM\
-   Por que **ECB é inseguro**\
-   Uso correto de chaves e padding

📌 Pasta: `Criptografia/Simétrica/`

------------------------------------------------------------------------

# 🟩 2. Criptografia Assimétrica (`Assimétrica/`)

Mecanismos que usam **um par de chaves**:\
🔑 **chave privada** (mantida em segredo)\
🔓 **chave pública** (distribuída livremente)

### Conteúdos disponíveis:

-   Geração de chaves RSA\
-   Cifra e decifra com RSA\
-   Assinatura e verificação\
-   Handshake simplificado cliente/servidor\
-   **Integração completa com ICP-EDU**\
-   **Assinatura digital real de PDF (PAdES)**

### Novidades importantes:

-   Nova pasta `ICP-EDU/`\
-   Scripts Python para assinar/verificar documentos\
-   Scripts OpenSSL\
-   Integração com certificados reais da RNP\
-   Uso do PyHanko para assinar PDFs "à moda SEI"

📌 Pasta: `Criptografia/Assimétrica/`

------------------------------------------------------------------------

# 🟥 3. Funções Hash e HMAC (`Hash/`)

Funções de hash criptográficas são usadas para:

-   Integridade de dados\
-   Armazenamento seguro de senhas\
-   Autenticação (HMAC)\
-   Assinatura e verificação de documentos\
-   Detecção de alterações (efeito avalanche)

### Conteúdos disponíveis:

-   SHA‑256 (exemplo didático)\
-   HMAC\
-   Avalanche (ver como pequenas mudanças alteram o hash)\
-   Hash de arquivos

📌 Pasta: `Criptografia/Hash/`

------------------------------------------------------------------------

# 🏛️ 4. Integração com ICP-EDU / ICP-Brasil (novidade)

O aluno aprende a usar um **certificado real**, emitido pela:

🔗 https://pessoal.icpedu.rnp.br/home

Inclui:

-   Conversão de `.p12` → `.pem`\
-   Assinatura digital de arquivos\
-   Assinatura **PAdES** de PDFs\
-   Validação com Adobe Reader\
-   Scripts Python e OpenSSL

📌 Pasta: `Criptografia/Assimétrica/ICP-EDU/`

------------------------------------------------------------------------

# 📘 5. Material para Salas de Aula

Este repositório foi otimizado para atividades práticas do IFRN,
incluindo:

-   Projetos de laboratório\
-   Exercícios de segurança e redes\
-   Aulas demonstrativas\
-   Integração com conteúdos de certificação\
-   Estudos avançados de criptografia aplicada

------------------------------------------------------------------------

# 🧪 6. Requisitos recomendados

### Para executar os códigos:

    Python 3.10+
    pip install cryptography pyhanko
    sudo apt install openssl

------------------------------------------------------------------------

# 🎓 7. Objetivo Educacional

Ao final deste módulo, o aluno deve ser capaz de:

-   Compreender diferenças entre simétrica / assimétrica / hashing\
-   Usar AES da forma correta\
-   Gerar e usar chaves RSA\
-   Assinar e verificar mensagens\
-   Emitir certificados ICP-EDU\
-   Assinar PDFs no padrão PAdES\
-   Validar assinaturas com PyHanko e Adobe Reader

------------------------------------------------------------------------

# 🤝 8. Contribuição

Sinta-se livre para enviar **pull requests** com melhorias, novos
algoritmos, exemplos e correções.

------------------------------------------------------------------------

# 🏁 9. Licença

Este material pode ser utilizado livremente para fins educacionais.

------------------------------------------------------------------------

Material criado com foco em qualidade didática e alinhado com
disciplinas de **Redes**, **Segurança da Informação**, **IoT** e
**Sistemas Embarcados** do IFRN.
