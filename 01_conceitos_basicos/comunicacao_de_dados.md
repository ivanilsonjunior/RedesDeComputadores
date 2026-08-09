# Comunicação de Dados
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Antes de estudar protocolos específicos, é preciso entender os conceitos básicos que descrevem *a qualidade* de uma comunicação em rede: quanto ela transporta, quão rápido chega, e o que pode dar errado no caminho.

---

## 📌 Sinal: analógico x digital

Toda informação transmitida em uma rede precisa virar um **sinal físico**:
- **Sinal analógico**: varia de forma contínua (ex.: onda de rádio, tensão elétrica variável).
- **Sinal digital**: varia em níveis discretos, tipicamente representando bits 0 e 1 (ex.: pulsos elétricos em um cabo Ethernet).

Mesmo redes "digitais" (como Wi-Fi e Ethernet) transmitem, no nível físico, sinais analógicos (ondas de rádio, tensão) que são **modulados** para representar bits digitais. Esse processo é estudado na Camada Física — ver [`06_componentes_fisicos/`](../06_componentes_fisicos/).

---

## 📌 Banda (largura de banda)

Capacidade **máxima teórica** de um canal de comunicação — quanto ele consegue transportar por unidade de tempo, em condições ideais.

- Medida em **bits por segundo** (bps), e seus múltiplos: kbps, Mbps, Gbps.
- É uma característica do **meio e dos equipamentos**, não do tráfego real.
- Exemplo: um link "100 Mbps" tem banda de 100 milhões de bits por segundo.

> ⚠️ **Cuidado com a unidade**: banda/velocidade de rede é medida em **bits** por segundo (Mbps), enquanto tamanho de arquivo é medido em **bytes** (MB). 1 byte = 8 bits, então um link de 100 Mbps transfere, no melhor caso, cerca de 12,5 MB/s — não 100 MB/s.

---

## 📌 Throughput (vazão)

Taxa **real** de dados que efetivamente chega ao destino, medida na prática.

- Sempre é **menor ou igual** à banda disponível.
- É reduzida por: congestionamento, interferência, distância, número de usuários simultâneos, overhead de protocolo (cabeçalhos).
- Também existe o termo **goodput**: a taxa de dados *úteis* (sem contar retransmissões e cabeçalhos) — ainda menor que o throughput.

```
Banda (capacidade máxima teórica)
   ≥ Throughput (o que realmente passa)
      ≥ Goodput (dados úteis de fato)
```

---

## 📌 Latência

Tempo que um pacote leva para ir da origem ao destino. Costuma ser composta por quatro parcelas:

| Componente | O que representa |
|---|---|
| **Processamento** | Tempo para o dispositivo examinar o cabeçalho e decidir o que fazer com o pacote |
| **Fila (enfileiramento)** | Tempo esperando em um buffer até poder ser transmitido |
| **Transmissão** | Tempo para "empurrar" todos os bits do pacote no meio físico (depende do tamanho do pacote e da banda) |
| **Propagação** | Tempo para o sinal viajar fisicamente pelo meio até o próximo salto (depende da distância e da velocidade do sinal no meio) |

Quando se mede o tempo de ida **e volta** de um pacote (como no `ping`), o valor obtido é o **RTT (Round-Trip Time)** — ver os scripts de ping em [`05_camadas_rede/`](../05_camadas_rede/).

---

## 📌 Jitter

Variação da latência entre pacotes consecutivos de um mesmo fluxo.

- Mesmo que o RTT médio seja bom, um jitter alto prejudica aplicações sensíveis a tempo real (VoIP, videoconferência, jogos online), pois os pacotes chegam em intervalos irregulares.
- Aplicações em tempo real costumam usar um **buffer de jitter** para reordenar/suavizar a chegada dos pacotes antes de reproduzi-los.

---

## 📌 Perda de pacotes

Pacotes que não chegam ao destino. Principais causas:

- **Congestionamento**: buffers de roteadores/switches lotados descartam pacotes excedentes.
- **Erros de transmissão**: ruído ou interferência corrompem o sinal (comum em Wi-Fi).
- **Falhas de enlace**: cabo rompido, sinal fraco, colisões.
- **TTL expirado**: o pacote "envelheceu" e foi descartado por um roteador (ver TTL em [`05_camadas_rede/conceitos_camadas_de_rede.md`](../05_camadas_rede/conceitos_camadas_de_rede.md)).

O impacto da perda depende do protocolo de transporte usado:
- **TCP** detecta a perda e retransmite automaticamente (ao custo de mais latência).
- **UDP** não retransmite — a aplicação é quem decide o que fazer (ver [`04_camadas_transporte/`](../04_camadas_transporte/)).

---

## Resumo visual

```
Banda        → o quanto o link SUPORTA
Throughput   → o quanto realmente PASSA
Latência     → quanto tempo DEMORA para chegar
Jitter       → o quanto a latência VARIA
Perda        → o quanto NÃO chega
```

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
