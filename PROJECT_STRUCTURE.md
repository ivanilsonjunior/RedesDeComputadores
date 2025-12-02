# 🏗️ PROJECT_STRUCTURE --- Organização do Repositório RedesDeComputadores

Este documento descreve a estrutura lógica, regras de organização,
convenções e objetivos do projeto.

------------------------------------------------------------------------

# 🎯 Objetivo Geral

Este repositório reúne **materiais teóricos**, **exemplos práticos**,
**scripts**, **exercícios** e **conteúdos complementares** utilizados em
disciplinas de:

-   Redes de Computadores\
-   Segurança em Redes\
-   Criptografia\
-   IoT\
-   Sistemas Embarcados\
-   Programação de Computadores

------------------------------------------------------------------------

# 🗂️ 1. Estrutura Geral do Repositório

    /
    ├── 01_conceitos_basicos/
    ├── 02_modelos_de_comunicacao/
    ├── 03_camadas_aplicacao/
    ├── 04_camadas_transporte/
    ├── 05_camadas_de_rede/
    ├── 06_componentes_fisicos/
    │
    ├── exercicios/
    │
    ├── material_de_apoio/
    │   ├── Camadas/
    │   │   ├── SideQuests/
    │   │   │   └── Segurança/
    │   │   │       └── Criptografia/
    │
    ├── README.md
    ├── SUMMARY.md
    ├── INDEX.md
    └── LICENSE

------------------------------------------------------------------------

# 📁 2. Descrição dos Diretórios

## 2.1 Diretórios por Conteúdo Curricular

Cada pasta numerada representa um **módulo de ensino do curso**.

Exemplo: - `01_conceitos_basicos/` → fundamentos\
- `02_modelos_de_comunicacao/` → OSI, TCP/IP\
- `03_camadas_aplicacao/` → protocolos de aplicação\
- `04_camadas_transporte/` → TCP/UDP\
- `05_camadas_de_rede/` → IPv4, IPv6, roteamento\
- `06_componentes_fisicos/` → hardware de redes

------------------------------------------------------------------------

## 2.2 Material de Apoio

📁 `material_de_apoio/`\
Armazena conteúdos complementares usados em aula:

-   códigos extras\
-   side quests\
-   aprofundamentos\
-   conteúdos de segurança (criptografia)\
-   exemplos para outras disciplinas

------------------------------------------------------------------------

## 2.3 SideQuests → Segurança → Criptografia

Estrutura modular:

    Criptografia/
    ├── Simétrica/
    ├── Assimétrica/
    └── Hash/

Cada módulo possui: - scripts de exemplo\
- READMEs específicos\
- material prático executável

------------------------------------------------------------------------

# 📑 3. Padrões e Convenções

### 3.1 Nomeação de arquivos

-   usar snake_case\
-   nomes descritivos\
-   evitar abreviações ambíguas\
-   README.md sempre nas pastas principais

### 3.2 Linguagens

Atualmente o repositório usa: - Python\
- C

### 3.3 Documentação

Cada diretório deve possuir: - README.md\
- instruções de execução\
- dependências\
- explicação teórica

------------------------------------------------------------------------

# 🚀 4. Como Expandir o Repositório

Os novos conteúdos devem seguir: - criação de pastas oficiais com
README\
- nomes consistentes\
- exemplos claros e comentados\
- adição ao SUMMARY.md e INDEX.md\
- atualização do PROJECT_STRUCTURE.md

------------------------------------------------------------------------

# 🤝 5. Contribuições

Para contribuições futuras: 1. Criar branch específica\
2. Documentar bem o código\
3. Adicionar README da nova pasta\
4. Manter padrão da estrutura\
5. Abrir Pull Request

------------------------------------------------------------------------

# 📜 Licença

Este projeto utiliza **GPL-3.0**.

------------------------------------------------------------------------

# 🧭 Última Atualização

*(preencher com data do último commit ou revisão)*
