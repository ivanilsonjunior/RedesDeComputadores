# Exercícios — Componentes Físicos de Redes
Material Didático — Redes de Computadores / ADS  
DIATINF — IFRN

Este conjunto de exercícios visa desenvolver compreensão prática e teórica da camada física,
dos meios de transmissão e dos equipamentos de rede usados no dia a dia.

---

## 1. Cabos e Conectividade

### 1.1 — Classifique os cabos abaixo:
Para cada item, identifique:
- Tipo (UTP/STP)
- Categoria (Cat5e, Cat6, Cat6A)
- Velocidade suportada
- Distância máxima

a) Cabo azul Cat5e  
b) Cabo laranja Cat6  
c) Cabo verde Cat6A  

---

### 1.2 — Explique:
- Qual a diferença entre UTP e STP?  
- Por que a blindagem é importante em ambientes industriais?  

---

### 1.3 — Verdadeiro ou Falso:
a) “Cat5e suporta 10 Gbps a 100 metros.”  
b) “Fibra óptica não sofre interferência eletromagnética.”  
c) “Cabo coaxial ainda é amplamente usado em redes locais modernas.”  

---

## 2. Fibra Óptica

### 2.1 — Complete:
- Fibra **monomodo** é indicada para ____________.  
- Fibra **multimodo** utiliza ____________ para transmitir luz.  
- A perda por distância em fibras é medida em ____________.  

---

### 2.2 — Diferencie:
- SM x MM  
- Conectores LC x SC  
- 10GBASE‑SR x 10GBASE‑LR  

---

## 3. Equipamentos de Rede

### 3.1 — Associe cada dispositivo à sua camada:
- Hub  
- Bridge  
- Switch  
- Roteador  
- Access Point  

Camadas:
1. Física  
2. Enlace  
3. Rede  

---

### 3.2 — O que acontece em cada equipamento?

a) HUB:  
b) SWITCH:  
c) ROTEADOR:  
d) ACCESS POINT:  

Explique o comportamento de broadcast, colisões e filtragem.

---

## 4. Interfaces de Rede (NIC)

### 4.1 — Execute o script ethernet_info_python3.py e responda:
- Qual a velocidade da interface principal?  
- Está em half ou full duplex?  
- A autonegociação está ativa?  

---

### 4.2 — Explique:
- O que é endereço MAC?  
- Ele pode ser alterado?  

---

## 5. Redes Sem Fio (Wi‑Fi)

### 5.1 — Com o script wifi_scan_python3.py:
Liste:
- 3 redes mais fortes  
- Seus níveis de sinal  
- Tipo de segurança utilizada  

---

### 5.2 — Responda:
- Por que redes de 5 GHz têm alcance menor que as de 2.4 GHz?  
- O que é largura de canal (20/40/80 MHz)?  

---

## 6. Diagnóstico e Testes

### 6.1 — Escolha dois dos testes abaixo e execute:
- Verificar status com `ip link`  
- Capturar quadros com Wireshark  
- Medir velocidade com `iperf3`  
- Usar `ethtool` para ver capacidades da NIC  

Descreva os resultados.

---

## 7. Desafio Final (Para Nota Extra)

### 7.1 — Crie um mapa físico da sala de laboratório:
- posições dos switches  
- cabeamento  
- portas utilizadas  
- interfaces de cada máquina  

### 7.2 — Explique o fluxo dos quadros Ethernet em dois cenários:
a) Comunicação entre máquinas no mesmo switch  
b) Comunicação entre máquinas em switches diferentes  

---

DIATINF — IFRN  
Material educacional para prática de Redes de Computadores e ADS.
