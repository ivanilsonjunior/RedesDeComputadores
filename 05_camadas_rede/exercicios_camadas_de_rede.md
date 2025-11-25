# 🚀 Exercícios — Camada de Rede (IP, ICMP, Roteamento)
### Material Didático — Redes de Computadores / ADS  
DIATINF — IFRN

A Camada de Rede é uma das mais importantes do modelo TCP/IP — aqui vivem conceitos como endereçamento IP, roteamento, TTL, fragmentação e diagnósticos via ICMP.

Estes exercícios foram elaborados para consolidar o entendimento por meio de **experimentos práticos**, **análises de pacotes**, **interpretação de rotas** e **simulações realistas**.

---

# 🧩 1. Endereçamento IPv4

## 📘 1.1 — Para cada endereço abaixo, determine:
- Endereço de rede  
- Endereço de broadcast  
- Quantidade de hosts  
- Faixa de endereços utilizáveis  

**a)** 192.168.10.25/24  
**b)** 10.0.5.130/20  
**c)** 172.16.200.77/28  

---

## 💡 1.2 — Responda:
- Qual a diferença entre **IP privado** e **IP público**?  
- Explique **rede x broadcast**.  
- O que é **CIDR**? Por que substituiu o modelo de **classes**?

---

## 🔁 1.3 — Interpretando endereços especiais
Explique o propósito de:

- 127.0.0.1  
- 0.0.0.0  
- 169.254.x.x  
- 255.255.255.255  

---

# 🛰️ 2. ICMP — Diagnósticos e Controle de Erro

## 🏓 2.1 — Usando o script icmp_ping_python3.py

Execute 5 pings para:
- 8.8.8.8  
- Seu roteador local  
- Uma máquina da rede do laboratório  

Depois responda:
- Quais foram os RTTs médios?  
- Houve timeouts? Por quê?  
- O que representa o **TTL** nas respostas?

---

## 🔍 2.2 — Análise com Wireshark  
Capture um **Echo Request** e um **Echo Reply** e identifique:

- Tipo e Código ICMP  
- TTL  
- Checksum  
- Tamanho do pacote  
- IP de origem e destino  

---

## 🎯 2.3 — Pesquise e liste 5 tipos de mensagens ICMP além do Echo.

---

# 📡 3. Tabela de Roteamento (Routing Table)

## 🗺️ 3.1 — Execute tabela_de_roteamento_python3.py

Em seguida, explique:

- O significado da rota **default / 0.0.0.0**  
- O que indica “via X.X.X.X”  
- O papel da interface (ex.: eth0, wlan0)  
- O que representa a **métrica**  

---

## 🔀 3.2 — Analise a tabela de rotas em 3 cenários:
- Conectado ao **Wi-Fi**  
- Conectado via **cabo**  
- **Sem rede**  

Explique o motivo das diferenças observadas.

---

# 📦 4. Encaminhamento (Forwarding)

## ⚙️ 4.1 — Executando roteador_simples_python3.py

Ao enviar o pacote de teste:

- Qual rota foi selecionada?  
- O TTL foi decrementado?  
- Houve fragmentação? Por quê?  
- Qual interface fez o encaminhamento?  

---

## 🛠️ 4.2 — Modifique o simulador

Altere:
- MTU → valores maiores e menores  
- Adicione novas rotas  
- Provoque TTL = 0  

Descreva o comportamento observado.

---

## 📬 4.3 — Teste com 3 pacotes diferentes
Crie pacotes variando:
- destino  
- TTL  
- tamanho do payload  

Compare o resultado do encaminhamento.

---

# 🧠 5. Questões Conceituais

## 📘 5.1 — Explique com suas palavras
- Encaminhamento x Roteamento  
- TTL e loops de roteamento  
- Por que o IP é “melhor esforço”?  
- O que é o **Longest Prefix Match**?  

---

## ❓ 5.2 — O que acontece quando:
a) Não existe rota para o destino?  
b) O TTL chega a zero?  
c) O pacote é maior que o MTU do enlace?  

---

# 🏆 6. Desafios Avançados (para nota extra)

## 🧮 6.1 — Construir um simulador próprio de rotas  
Implementar:
- Rotas estáticas  
- Rota padrão  
- Decisão automática por prefixo  
- Impressão formatada da tabela de rotas  

---

## 🔎 6.2 — Criar um mini-traceroute
Implementar:
- Envio de ICMP Echo Request  
- TTL 1, 2, 3, …  
- Coleta dos next-hops  
- Impressão dos saltos até o destino  

---

DIATINF — IFRN  
Material educacional para Redes de Computadores e ADS.
