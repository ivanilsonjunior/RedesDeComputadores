# Módulo 06 — Componentes Físicos, Unicast, Broadcast e Multicast  
Material Didático — Redes de Computadores / ADS  
DIATINF — IFRN

Este README unificado reúne **todo o conteúdo completo do módulo**, incluindo:
- Conceitos teóricos  
- Diagramas ASCII  
- Scripts práticos (unicast, broadcast, multicast)  
- Exercícios aplicados  
- Explicação detalhada dos modos de entrega na Ethernet  

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, o estudante será capaz de:

- Entender a infraestrutura física de redes (cabos, Wi-Fi, NICs).
- Compreender o funcionamento de hubs, switches, roteadores e APs.
- Explicar padrões Ethernet e capacidades de cada meio físico.
- **Diferenciar unicast, broadcast e multicast** e seus impactos na rede.
- Executar scripts reais que demonstram esses modos de entrega.
- Capturar e analisar quadros no Wireshark.
- Relacionar os modos de entrega com a Camada de Enlace e de Rede.

---

# 📚 1. Conceitos Fundamentais

## Conectividade com Fio
- Cabos UTP/STP, categorias, velocidades  
- Fibra óptica (SM/MM), conectores, aplicações  

## Conectividade Sem Fio
- Padrões Wi‑Fi  
- Banda, modulação, RSSI  

## Placas de Rede
- Endereço MAC  
- Duplex  
- Autonegociação  

## Equipamentos
- Hub  
- Bridge  
- Switch  
- Roteador  
- Access Point  

---

# 📡 2. Unicast, Broadcast e Multicast

## 2.1 Conceitos resumidos

| Modo      | Entrega      | Destinatários | Exemplos |
|-----------|--------------|---------------|----------|
| Unicast   | 1 → 1        | Host único    | HTTP, SSH |
| Broadcast | 1 → Todos    | Toda a LAN    | ARP, DHCP |
| Multicast | 1 → Grupo    | Hosts inscritos | IPTV, OSPF |

---

# 🖼️ 3. Diagramas ASCII (Visual)

## 3.1 Unicast

```
         (Host A)                                  (Host B)
     ┌──────────────┐                        ┌──────────────┐
     │  MAC: AA:AA  │                        │  MAC: BB:BB  │
     └───────┬──────┘                        └───────┬──────┘
             │                                        │
             │      Quadro Ethernet Unicast           │
             │ ─────────────────────────────────────▶ │
             │     Destino: BB:BB:BB:BB:BB:BB         │
             │     Origem : AA:AA:AA:AA:AA:AA         │
       ┌─────┴─────┐                           ┌─────┴─────┐
       │   SWITCH   │  → Consulta tabela CAM →  │ Porta do B │
       └────────────┘                           └────────────┘
```

## 3.2 Broadcast

```
                     REDE LOCAL (LAN)
       ┌──────────┬──────────┬──────────┬──────────┬──────────┐
       │ Host A   │ Host B   │ Host C   │ Host D   │ Host E   │
       └─┬────────┴──┬────────┴──┬────────┴──┬────────┴──┬──────┘
         │           │           │           │           │
          ┌──────────┴───────────────────────────────────┐
          │                     SWITCH                   │
          └───────┬──────────────────────────────────────┘
                  │  Destino FF:FF:FF:FF:FF:FF
                  ├────────────────────────────────────→ TODOS
```

## 3.3 Multicast

```
                    GRUPO MULTICAST (Ex: 224.0.0.251)
                 ┌───────────────┬───────────────┬──────────────┐
                 │ Host B        │ Host D        │ Host (grupo)  │
                 └────┬──────────┴──────┬────────┴──────────────┘
                      │                 │
              ┌───────┴─────────────────┴──────────┐
              │             SWITCH (IGMP)            │
              └─────────┬───────────────┬──────────┘
                        │               │
        Host A ────────▶│ MAC Multicast │─────────┐
                        │ 01:00:5E:xx   │         │
                        └──────────────────────────┘
```

---

# 🧪 4. Scripts de Demonstração

## 4.1 UNICAST – `unicast_demo.py`
Envio 1→1 usando UDP.

Uso:
```
python3 unicast_demo.py
python3 unicast_demo.py cliente
```

---

## 4.2 BROADCAST – `broadcast_demo.py`
Envio 1→todos usando o endereço 255.255.255.255.

Uso:
```
python3 broadcast_demo.py
python3 broadcast_demo.py cliente
```

---

## 4.3 MULTICAST – `multicast_demo.py`
Envio 1→grupo usando endereço multicast (224.x.x.x).

Uso:
```
python3 multicast_demo.py
python3 multicast_demo.py cliente
```

---

# 📝 5. Exercícios Integrados

## 5.1 Classificação
Classifique diversas situações como unicast, broadcast ou multicast.

## 5.2 Prática com Scripts
Execute cada script e explique:
- comportamento do switch  
- portas atingidas  
- formato do quadro  
- comportamento no Wireshark  

## 5.3 Modificações no Código
Altere os scripts para:
- mudar portas  
- criar múltiplos clientes  
- modularizar o envio  
- testar atraso ou perda  

## 5.4 Wireshark
- capture quadros  
- identifique MAC de destino  
- identifique mensagens multicast (mDNS, OSPF, SSDP)

---

# 📎 Material Complementar

- [`material_de_apoio/Camadas/Enlace/`](../material_de_apoio/Camadas/Enlace/) — descoberta de dispositivos Bluetooth e um par broadcast UDP mais simples que os scripts deste módulo.

---

# 📦 Arquivos Incluídos no Módulo

- conceitos_componentes_fisicos.md  
- unicast_broadcast_multicast.md  
- diagramas_unicast_broadcast_multicast.md  
- unicast_demo.py  
- broadcast_demo.py  
- multicast_demo.py  
- exercicios_componentes_fisicos.md  
- exercicios_broad_multi_uni.md  

---

# 📘 Conclusão

Este módulo combina teoria, prática e visualização — permitindo que o aluno entenda **como a comunicação realmente acontece na rede física e no Ethernet**.

Ele é extremamente útil para:
- ensino de Redes  
- ADS  
- disciplinas de TCP/IP  
- prática com switches reais  
- formação profissional em TI  

---

DIATINF — IFRN  
Material educacional para Redes de Computadores e ADS.
