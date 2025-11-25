
# 02 — Modelos de Comunicação (OSI e TCP/IP)

Este módulo apresenta os dois principais modelos conceituais usados para entender redes de computadores:

- **Modelo OSI (7 camadas)**
- **Modelo TCP/IP (4 camadas)**

Eles foram criados para padronizar e organizar como dispositivos comunicam-se em redes.  
Todo estudo e projeto de redes, protocolos, aplicações e segurança tem como base esses modelos.

---

# 🎯 Objetivos de Aprendizagem

Ao final deste módulo o estudante deve ser capaz de:

- Explicar o propósito de modelos de referência.
- Identificar as camadas do modelo OSI e suas funções.
- Identificar as camadas do modelo TCP/IP e suas funções.
- Relacionar protocolos reais (HTTP, TCP, IP, Ethernet…) às camadas.
- Entender a diferença entre **modelo** e **implementação**.
- Utilizar os modelos para analisar e depurar redes e aplicações.

---

# 📂 Arquivos do Módulo

| Arquivo | Conteúdo |
|---------|----------|
| `osi_tcpip_resumo.md` | Comparação direta entre OSI e TCP/IP. |
| `camadas_osi.md` | Descrição detalhada das 7 camadas OSI. |
| `camadas_tcpip.md` | Descrição detalhada das camadas TCP/IP. |
| `mapas_conceituais.md` | Diagramas e resumos gráficos para estudo. |

---

# 🧭 Mapa Conceitual Geral (ASCII)

```
             +------------------------------+
             |      Modelos de Comunicação   |
             +------------------------------+
                  /                    \
      Modelo OSI (7 camadas)     Modelo TCP/IP (4 camadas)
              |                             |
    Pilha completamente          Pilha prática usada na Internet
         teórica                           (implementação real)
```

---

# 🧪 Exercícios Recomendados

### 🔹 Exercício 1 — Mapear Protocolos
Liste 10 protocolos reais (ex.: HTTP, DNS, TCP, IP, ARP, Ethernet) e coloque-os nas camadas corretas dos modelos OSI e TCP/IP.

### 🔹 Exercício 2 — Explicar Diferenças
Explique por que o modelo OSI tem 7 camadas, mas o TCP/IP funciona com apenas 4.

### 🔹 Exercício 3 — Aplicação Prática
Dado o fluxo:  
“Usuário acessa www.ifrn.edu.br pelo navegador”,  
explique **quais camadas são usadas** e **qual protocolo atua em cada uma**.

### 🔹 Exercício 4 — Queda de Pacote
Explique em qual camada ocorre:  
- colisão de quadro  
- perda de pacote  
- queda de conexão  
- porta bloqueada  
- erro de aplicação

### 🔹 Exercício 5 — Encapsulamento
Desenhe o caminho do dado da aplicação até o meio físico usando os dois modelos.

---

# 👨‍🏫 Nota para Professores

Este módulo é ideal para:
- 2ª e 3ª semanas do curso.
- Revisão contínua durante os outros módulos.
- Atividades com Wireshark para visualização de camadas.

---

# DIATINF – IFRN
Material didático para disciplina de Redes de Computadores.
