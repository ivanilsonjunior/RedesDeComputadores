# 📘 Redes de Computadores --- Material Didático Completo

Repositório oficial contendo **exemplos práticos**, **scripts**,
**exercícios**, **materiais teóricos** e **side quests** para
disciplinas de:

-   **Redes de Computadores**\
-   **Segurança da Informação**\
-   **Criptografia**\
-   **IoT / Sistemas Embarcados**\
-   **Programação (apoio complementar)**

Este repositório foi estruturado para ser usado em **aulas,
laboratórios, cursos e estudos autônomos**.

------------------------------------------------------------------------

# 🧭 Navegação Rápida

-   📚 **[SUMMARY.md --- Sumário Geral](SUMMARY.md)**\
-   📖 **[INDEX.md --- Índice Detalhado](INDEX.md)**\
-   🏗️ **[PROJECT_STRUCTURE.md --- Estrutura Oficial do
    Projeto](PROJECT_STRUCTURE.md)**\
-   📝 **Exercícios:** `material_de_apoio/`\
-   🧩 **Sockets avançados (TCP/UDP, Bluetooth, broadcast):**
    `material_de_apoio/Camadas/`\
-   🔐 **Criptografia & Segurança:**
    `material_de_apoio/SideQuests/Segurança/Criptografia/`

------------------------------------------------------------------------

# 🗂️ Estrutura Geral do Repositório

A organização segue a lógica didática clássica das disciplinas de Redes:

    /
    ├── 01_conceitos_basicos/
    ├── 02_modelos_de_comunicacao/
    ├── 03_camadas_aplicacao/
    ├── 04_camadas_transporte/
    ├── 05_camadas_rede/
    ├── 06_componentes_fisicos/
    │
    ├── exercicios/
    │
    ├── material_de_apoio/
    │   ├── Camadas/                  ← sockets avançados por camada OSI
    │   │   ├── Aplicação/
    │   │   ├── Enlace/
    │   │   └── Transporte/Sockets/
    │   └── SideQuests/
    │       ├── Segurança/
    │       │   └── Criptografia/
    │       └── (BitDogLab, WebScraping, MouseTeclado, ...)
    │
    ├── README.md
    ├── SUMMARY.md
    ├── INDEX.md
    └── LICENSE

Cada uma das pastas numeradas corresponde a uma **unidade de conteúdo**
no curso.

------------------------------------------------------------------------

# 🎯 Objetivos do Repositório

✔ Consolidar num único local todo o conteúdo prático e teórico usado nas
disciplinas\
✔ Fornecer códigos simples e executáveis para laboratório\
✔ Criar uma base modular que pode ser usada em **várias disciplinas**\
✔ Servir como referência para estudos posteriores ou projetos dos
alunos\
✔ Facilitar manutenção e expansão por meio de documentação formal

------------------------------------------------------------------------

# 🧠 Conteúdos Incluídos

## 🟦 1. Conceitos Básicos --- `01_conceitos_basicos/`

-   Redes PAN/LAN/MAN/WAN\
-   Topologias\
-   Noções de comunicação\
-   Legislação\
-   Primeira visão da Internet

## 🟩 2. Modelos de Comunicação --- `02_modelos_de_comunicacao/`

-   RM-OSI\
-   TCP/IP\
-   Encapsulamento\
-   Comparações

## 🟧 3. Camada de Aplicação --- `03_camadas_aplicacao/`

-   HTTP / HTTPS\
-   FTP / SFTP\
-   SMTP / POP3 / IMAP\
-   DNS\
-   SSH\
-   Cliente/Servidor

## 🟨 4. Camada de Transporte --- `04_camadas_transporte/`

-   UDP\
-   TCP\
-   Controle de congestionamento\
-   Multiplexação

## 🟥 5. Camada de Rede --- `05_camadas_rede/`

-   IPv4\
-   IPv6\
-   ARP/RARP\
-   CIDR, VLSM\
-   Roteamento básico

## 🟫 6. Componentes Físicos --- `06_componentes_fisicos/`

-   NICs\
-   Hubs, switches, bridges\
-   Roteadores\
-   APs, repetidores\
-   Meios físicos

------------------------------------------------------------------------

# 🔐 SideQuest: Segurança e Criptografia

A pasta `material_de_apoio/.../Criptografia/` contém um módulo inteiro
dedicado a:

### **Simétrica**

-   AES (ECB, CBC, GCM)\
-   Cifra de César\
-   Criptografia de arquivos

### **Assimétrica**

-   RSA básico\
-   Geração de chaves\
-   Assinaturas\
-   Mini-handshake cliente-servidor

### **Hash, HMAC e Integridade**

-   SHA-256\
-   HMAC\
-   Salt de senhas\
-   Efeito avalanche\
-   Hash de arquivos

Cada módulo possui **README próprio**, exemplos e scripts prontos.

------------------------------------------------------------------------

# 🧪 Exercícios e Laboratórios

Pasta: `exercicios/`

Inclui: - listas de exercícios\
- roteiros de laboratório\
- atividades guiadas\
- desafios práticos

------------------------------------------------------------------------

# 🛠️ Como Utilizar

## 1. Pré-requisitos

-   Python 3 (para scripts de criptografia e protocolos)\
-   Compilador C (para alguns exemplos didáticos)\
-   Navegador web para consultar documentação\
-   Git (opcional para clonar)

## 2. Clonar o repositório

``` bash
git clone https://github.com/ivanilsonjunior/RedesDeComputadores
```

## 3. Executar scripts Python

``` bash
python3 nome_do_script.py
```

## 4. Navegar pela documentação

Use os arquivos: - `SUMMARY.md` para navegação geral\
- `INDEX.md` para conteúdo detalhado\
- `PROJECT_STRUCTURE.md` para entender a organização

------------------------------------------------------------------------

# 🤝 Contribuições

Contribuições são bem-vindas!\
Sugestões, correções ou novos conteúdos podem seguir estes passos:

1.  Criar um branch\
2.  Documentar alterações\
3.  Garantir README na nova pasta\
4.  Seguir convenções do projeto\
5.  Abrir um Pull Request

------------------------------------------------------------------------

# 📜 Licença

Este material é distribuído sob a licença **GPL-3.0**.\
Consulte o arquivo `LICENSE` para detalhes.

------------------------------------------------------------------------