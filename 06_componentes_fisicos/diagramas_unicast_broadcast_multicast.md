# Diagramas ASCII — Unicast, Broadcast e Multicast
Material Didático — Redes de Computadores / ADS  
DIATINF — IFRN

Este arquivo contém diagramas ASCII ilustrando, de forma didática,
os três modos de entrega fundamentais: **Unicast**, **Broadcast** e **Multicast**.

---

# 1. UNICAST — Comunicação 1 → 1

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
             │                                        │
       ┌─────┴─────┐                           ┌─────┴─────┐
       │   SWITCH   │  → Consulta tabela CAM →  │ Porta do B │
       └────────────┘                           └────────────┘
```

---

# 2. BROADCAST — Comunicação 1 → TODOS

```
                         REDE LOCAL (LAN)
              ┌────────────┬────────────┬────────────┬────────────┐
              │            │            │            │            │
        ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Host A   │ │ Host B   │ │ Host C   │ │ Host D   │ │ Host E   │
        └─────┬────┘ └─────┬────┘ └─────┬────┘ └─────┬────┘ └─────┬────┘
              │            │            │            │            │
              │            │            │            │            │
              └──────┬─────┴─────┬─────┴─────┬─────┴─────┬───────┘
                     │           │           │
              ┌──────┴──────────────────────────────────────────┐
              │                        SWITCH                    │
              └──────┬──────────────────────────────────────────┘
                     │
                     │  Quadro Ethernet Broadcast
                     │  Destino: FF:FF:FF:FF:FF:FF
                     ├──────────────────────────────────────────▶ TODOS
```

---

# 3. MULTICAST — Comunicação 1 → GRUPO

```
                     GRUPO MULTICAST (Ex: 224.0.0.251)
                 ┌──────────────────────────────────────┐
                 │ Hosts que desejam receber multicast  │
                 └───────┬──────────────┬──────────────┘
                         │              │
                 ┌──────────┐   ┌──────────┐
                 │ Host B   │   │ Host D   │   ← inscritos no grupo
                 └─────┬────┘   └─────┬────┘
                       │              │
                       │              │
                ┌──────┴──────────────┴──────┐
                │           SWITCH            │
                │    com IGMP Snooping       │
                └──────┬──────────────┬──────┘
                       │              │
        ┌──────────┐   │              │   ┌──────────┐
        │ Host A   │   │   (ignora)   │   │ Host C   │
        └─────┬────┘   │              │   └─────┬────┘
              │         │              │         │
              │   ┌─────┴────────────────────┐  │
              │   │ Quadro Multicast         │  │
              │   │ MAC: 01:00:5E:XX:XX:XX   │  │
              └──▶│ IP: 224.x.x.x            │  │
                  └──────────────────────────┘
```

---

# 4. Tabela Comparativa

```
+------------+---------------+-------------------------+--------------------------+
|   MODO     |   ENTREGA     |     RECEBEDORES         |      EXEMPLOS            |
+------------+---------------+-------------------------+--------------------------+
| UNICAST    | 1  →  1       | Host específico         | HTTP, SSH, DNS Query     |
| BROADCAST  | 1  →  TODOS   | Toda a LAN              | ARP, DHCP Discover       |
| MULTICAST  | 1  →  GRUPO   | Apenas inscritos        | IPTV, OSPF, mDNS         |
+------------+---------------+-------------------------+--------------------------+
```

---

DIATINF — IFRN  
Material educacional para Redes de Computadores e ADS.
