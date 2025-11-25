# Exercícios — Unicast, Broadcast e Multicast  
Material Didático — Redes de Computadores / ADS  
DIATINF — IFRN

Este arquivo reúne exercícios práticos e teóricos para ajudar o estudante a compreender, analisar e demonstrar na prática os três modos fundamentais de entrega de quadros e pacotes em redes: **Unicast**, **Broadcast** e **Multicast**.

---

# 🧩 1. Conceitos Fundamentais

## 1.1 — Classifique cada situação como UNICAST, BROADCAST ou MULTICAST:
a) Um PC envia ARP Request para descobrir o MAC do gateway.  
b) Um cliente acessa um servidor HTTP.  
c) IPTV envia vídeo apenas para clientes inscritos.  
d) DHCP Discover enviado pelo cliente ao entrar na rede.  
e) OSPF envia mensagens Hello para roteadores vizinhos.  

---

## 1.2 — Explique com suas palavras:
- A diferença entre **unicast**, **broadcast** e **multicast**.  
- Por que o broadcast não atravessa roteadores.  
- O que são endereços MAC multicast (01:00:5E:xx:xx:xx).  
- Por que multicast é mais eficiente que broadcast.

---

# 🧪 2. Exercícios Práticos com Scripts

Os scripts fornecidos no módulo permitem observar o funcionamento real desses modos de entrega.

Scripts usados:  
- **unicast_demo.py**  
- **broadcast_demo.py**  
- **multicast_demo.py**  

---

# 🔵 3. UNICAST — Demonstração 1→1

## 3.1 — Execução
Terminal 1:
```
python3 unicast_demo.py
```

Terminal 2:
```
python3 unicast_demo.py cliente
```

## 3.2 — Responda:
- O servidor recebe pacotes apenas de um cliente por vez?  
- É possível enviar de múltiplos clientes simultaneamente? Explique.  
- Qual porta é usada na comunicação?  
- O unicast é entregue para quantas portas do switch?  

---

# 🟡 4. BROADCAST — Demonstração 1→TODOS

## 4.1 — Execução
Terminal 1:
```
python3 broadcast_demo.py
```

Terminal 2:
```
python3 broadcast_demo.py cliente
```

## 4.2 — Responda:
- O servidor recebe pacotes enviados de broadcast?  
- Todos os hosts da LAN receberiam esse pacote? Por quê?  
- Como o Wireshark mostra quadros de broadcast?  
- Em qual endereço MAC o broadcast é enviado?  

---

# 🟢 5. MULTICAST — Demonstração 1→GRUPO

## 5.1 — Execução
Terminal 1:
```
python3 multicast_demo.py
```

Terminal 2:
```
python3 multicast_demo.py cliente
```

## 5.2 — Responda:
- Quais hosts recebem o pacote multicast?  
- O pacote é enviado para todas as portas? Explique IGMP Snooping.  
- Quais protocolos reais usam multicast?  
- Qual faixa IPv4 é usada para multicast?  

---

# 📡 6. Análise com Wireshark

Realize uma captura enquanto executa cada script.

## 6.1 — Identifique:
- Endereço MAC de destino: unicast, broadcast ou multicast  
- Tipo do frame  
- Conteúdo da mensagem UDP  
- TTL (no caso de multicast)  
- Porta de origem e destino  

## 6.2 — Explique:
- Por que quadros broadcast aparecem para todas as máquinas no mesmo switch?  
- Como o Wireshark diferencia tráfego multicast?  

---

# 🛠️ 7. Modificações no Código

Altere cada script para:

### UNICAST:
- mudar porta  
- enviar resposta do servidor ao cliente (eco)

### BROADCAST:
- enviar mensagens periódicas a cada 1 segundo  
- registrar timestamp completo

### MULTICAST:
- mudar o grupo multicast para outro endereço  
- criar dois clientes e observar comportamento

Documente o resultado.

---

# 🧠 8. Desafios

## 8.1 — Crie um script que:
- envie **unicast**, **broadcast** e **multicast** em sequência  
- identifique o tipo de entrega recebida  

## 8.2 — Explique o comportamento do switch em:
a) Rede com IGMP Snooping ativado  
b) Rede sem IGMP Snooping  

## 8.3 — Desenhe (mesmo em ASCII) o fluxo de entrega dos três modos.

---

DIATINF — IFRN  
Material educacional para Redes de Computadores e ADS.
