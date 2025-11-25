# Componentes Físicos de Redes — Conceitos Fundamentais
Material didático — Redes de Computadores / ADS  
DIATINF — IFRN

A Camada Física e os componentes físicos de uma rede são responsáveis por transportar os bits pelo meio físico — sejam eles elétricos, ópticos ou ondas de rádio.  
Este arquivo apresenta os conceitos essenciais para entender o funcionamento da infraestrutura de redes no mundo real.

---

## 1. Conectividade com Fio

### 1.1 Cabos de Par Trançado (Ethernet)
- UTP (Unshielded Twisted Pair) — mais comum.
- STP (Shielded Twisted Pair) — blindagem contra interferências.
- Tamanhos e categorias:
  - Cat5e (1 Gbps)
  - Cat6  (1 Gbps / 10 Gbps até 55m)
  - Cat6A (10 Gbps até 100m)

### 1.2 Fibra Óptica
- Monomodo (SM) — longas distâncias, lasers.
- Multimodo (MM) — curtas/médias distâncias, LEDs.
- Vantagens:
  - Imune a interferências
  - Alta banda
  - Maior alcance

---

## 2. Conectividade Sem Fio (Wi‑Fi)

### 2.1 Padrões Wi‑Fi
- 802.11n (2.4 GHz)
- 802.11ac (5 GHz)
- 802.11ax / Wi‑Fi 6 (2.4 e 5 GHz)

### 2.2 Conceitos Importantes
- RSSI (força do sinal)
- Largura de canal (20/40/80 MHz)
- Interferência e ruído
- Densidade de usuários

---

## 3. Placas de Rede (NICs)

### 3.1 Endereço MAC
Identificador único de 48 bits:
`AA:BB:CC:DD:EE:FF`

### 3.2 Duplex
- Half‑duplex → pode enviar OU receber (hubs).
- Full‑duplex → envia e recebe ao mesmo tempo (switches modernos).

### 3.3 Autonegociação
A NIC e o switch decidem automaticamente:
- velocidade (10/100/1000 Mbps)
- duplex
- MDI/MDI-X

---

## 4. Equipamentos de Rede

### 4.1 Hub
- Camada Física.
- Repassa tudo para todas as portas.
- Domínio de colisão compartilhado.
- Obsoleto, mas útil didaticamente.

### 4.2 Bridge
- Camada de Enlace.
- Conecta duas LANs.
- Filtra quadros por MAC.

### 4.3 Switch
- Comutação Ethernet.
- Uma porta = um domínio de colisão.
- Aprende MAC → tabela CAM.
- Full‑duplex, baixa latência.

### 4.4 Roteador
- Camada de Rede.
- Encaminha pacotes entre redes diferentes.
- Trabalha com IP e tabela de rotas.

### 4.5 Access Point (AP)
- Responsável pelo Wi‑Fi.
- Faz ponte (bridge) entre rádio e Ethernet.

### 4.6 Repetidores / Extensores
- Reforçam sinal elétrico ou Wi‑Fi.
- Necessários quando o alcance é limitado.

---

## 5. Padrões Ethernet

### 5.1 Fast Ethernet
- 100BASE‑TX → 100 Mbps em Cat5

### 5.2 Gigabit Ethernet
- 1000BASE‑T → 1 Gbps em Cat5e/Cat6

### 5.3 10 Gigabit Ethernet
- 10GBASE‑SR (fibra multimodo)
- 10GBASE‑LR (fibra monomodo)
- 10GBASE‑T (Cat6A)

---

## 6. Diagnóstico e Testes

### 6.1 LEDs das Interfaces
- Link (verde) → conexão detectada.
- Activity (amarelo) → tráfego.

### 6.2 Comandos úteis (Linux)
- `ip link`
- `ethtool eth0`
- `iwconfig`
- `ping`
- `iperf3`

### 6.3 Testes recomendados
- testar cabo com certificador  
- verificar velocidade negociada  
- medir throughput com iperf  
- capturar quadros com Wireshark  

---

## 7. Relação com Camadas Superiores

| Camada | Exemplo | Relação |
|--------|---------|---------|
| Aplicação | HTTP | depende da rede funcionar |
| Transporte | TCP/UDP | entrega segmentada |
| Rede | IP | entrega lógica entre redes |
| **Enlace** | Ethernet/Wi‑Fi | entrega entre interfaces |
| **Física** | Cabos/Rádio | transporte dos bits |

---

DIATINF — IFRN  
Material educacional de Redes de Computadores e ADS.
