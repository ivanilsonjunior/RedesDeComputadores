# Camada de Rede — Conceitos Fundamentais
Material didático — Redes de Computadores / ADS  
DIATINF — IFRN

A Camada de Rede (Network Layer) é responsável por entregar pacotes entre redes distintas.  
Seu principal protocolo é o **IP (Internet Protocol)**, que organiza endereços, fragmenta pacotes, decide rotas e controla o tempo de vida (TTL).

---

## 1. Funções Principais da Camada de Rede

### **1. Encaminhamento (Forwarding)**
- Decide para qual interface enviar um pacote.
- Baseado no endereço de destino + tabela de roteamento.

### **2. Roteamento (Routing)**
- Construção automática da tabela de rotas.
- Protocolos (conceitual para ADS): RIP, OSPF, BGP.

### **3. Endereçamento Lógico**
- Endereços IPv4 atribuídos a interfaces.
- Identificação de redes e hosts.

### **4. Fragmentação e Remontagem**
- Pacotes maiores que o MTU podem ser fragmentados.
- Apenas o destino remonta os fragmentos.

### **5. Controle de Loops (TTL)**
- Impede loops infinitos de roteamento.
- Cada roteador decrementa o TTL.

### **6. Erros e Diagnósticos**
- Uso do ICMP.
- Exemplos: host unreachable, TTL expired, echo reply.

---

## 2. Endereçamento IPv4

Um endereço IPv4 possui 32 bits, no formato **a.b.c.d**  
Exemplo: `192.168.1.10`

### Classes (histórico):
- **A:** 0.0.0.0 – 127.255.255.255  
- **B:** 128.0.0.0 – 191.255.255.255  
- **C:** 192.0.0.0 – 223.255.255.255  

### Máscara:
- Ex.: `192.168.1.10/24`  
  - Rede: `192.168.1.0`  
  - Broadcast: `192.168.1.255`

### Endereços especiais:
- `0.0.0.0` → rota padrão  
- `127.0.0.1` → loopback  
- `169.254.x.x` → APIPA  
- `255.255.255.255` → broadcast limitado  

---

## 3. Protocolo IP (IPv4)

O IP é:
- Não confiável  
- Sem conexão  
- Melhor esforço  
- Sem retransmissão  
- Sem garantia de ordem  

### Campos do cabeçalho IPv4:
- Version  
- Header Length  
- TOS/DS  
- Total Length  
- Identification  
- Flags  
- Fragment Offset  
- **TTL**  
- **Protocol** (TCP=6, UDP=17, ICMP=1)  
- Header Checksum  
- Source Address  
- Destination Address  

---

## 4. ICMP — Internet Control Message Protocol

Protocolo de controle e diagnóstico da camada de rede.

### Mensagens comuns:
- **Echo Request / Reply** (PING)  
- Destination Unreachable  
- TTL Expired  
- Redirect  
- Time Exceeded  

ICMP aparece encapsulado em IP (**Protocol = 1**).

---

## 5. Tabela de Roteamento

Uma tabela de rotas contém:
- Rede de destino  
- Gateway  
- Interface  
- Métrica  

### Exemplo (Linux):
```
$ ip route
```

---

## 6. Roteamento Estático x Dinâmico

### **Roteamento Estático**
- Configurado manualmente.
- Simples e previsível.

### **Roteamento Dinâmico**
- Roteadores trocam rotas automaticamente.
- Protocolos: RIP, OSPF, BGP (conceitual).

---

## 7. Relação com Outras Camadas

| Camada | Responsabilidade |
|--------|------------------|
| Aplicação | Serviços (HTTP, DNS, etc.) |
| Transporte | Portas, confiabilidade (TCP/UDP) |
| **Rede** | IP, roteamento, TTL |
| Enlace | MAC, ARP, Ethernet |
| Física | Meio físico |

---

## 8. Resumo Geral

A Camada de Rede responde:
- **Para onde enviar?** (rota)  
- **Quem é o destino?** (IP)  
- **O pacote cabe no enlace?** (fragmentação)  
- **O pacote já ficou velho?** (TTL)  
- **Houve erro?** (ICMP)  

---

DIATINF — IFRN  
Material educacional de Redes de Computadores e ADS.
