# 05 — Camada de Rede
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Este diretório contém material teórico e scripts didáticos sobre a Camada de Rede: endereçamento IPv4, roteamento, encaminhamento, TTL e diagnóstico via ICMP.

---

# 🎯 Objetivos de Aprendizagem

Ao final deste módulo, o estudante será capaz de:

- Explicar o papel da Camada de Rede no modelo TCP/IP (endereçamento lógico, roteamento e encaminhamento).
- Interpretar um endereço IPv4 com máscara/CIDR (rede, broadcast, faixa de hosts).
- Explicar o funcionamento do ICMP (Echo Request/Reply) e o papel do TTL.
- Ler e interpretar uma tabela de roteamento real do sistema operacional.
- Simular o encaminhamento de pacotes (longest prefix match, decremento de TTL, fragmentação).

---

# 📂 Arquivos do Módulo

| Arquivo | Descrição |
|---------|-----------|
| `conceitos_camadas_de_rede.md` | Teoria: endereçamento IPv4, cabeçalho IP, ICMP, tabela de roteamento, estático x dinâmico. |
| `exercicios_camadas_de_rede.md` | Lista de exercícios práticos e conceituais do módulo. |
| `icmp_ping_python3.py` | Implementa um "ping" real com socket raw ICMP (requer privilégios administrativos). |
| `ping_simplificado_python3.py` | Simula a lógica de um ping usando UDP comum, sem exigir privilégios de root — mede RTT para ilustrar latência. |
| `roteador_simples_python3.py` | Simulador lógico de roteador: tabela de rotas, longest prefix match, TTL e fragmentação por MTU. |
| `tabela_de_roteamento_python3.py` | Lê e imprime a tabela de roteamento real do SO (`ip route` no Linux, `route print` no Windows). |

---

# 🧭 Diagrama Geral da Camada de Rede

```
Aplicação
   ↓
Transporte    (TCP ou UDP)
   ↓
Rede          ← este módulo (IP, ICMP, roteamento, TTL)
   ↓
Enlace
   ↓
Física
```

---

# ▶️ Como executar

```bash
# Ping simplificado (não exige privilégios)
python3 ping_simplificado_python3.py

# Ping ICMP real (requer sudo/administrador)
sudo python3 icmp_ping_python3.py

# Simulador de roteador (não envia pacotes reais)
python3 roteador_simples_python3.py

# Tabela de roteamento do sistema operacional
python3 tabela_de_roteamento_python3.py
```

---

# 🧪 Exercícios

Ver `exercicios_camadas_de_rede.md` para a lista completa (endereçamento IPv4, ICMP, tabela de roteamento, encaminhamento e desafios avançados como um mini-traceroute).

---

# 👨‍🏫 Notas para Professores

- `ping_simplificado_python3.py` é útil em laboratórios sem acesso root/administrador; `icmp_ping_python3.py` mostra o protocolo real, incluindo cálculo de checksum.
- `roteador_simples_python3.py` não depende de rede real — pode ser usado em qualquer sala de aula, inclusive offline.
- Combine com Wireshark para comparar o ICMP real (`icmp_ping_python3.py`) com o tráfego UDP gerado por `ping_simplificado_python3.py`.

---

DIATINF — IFRN
Material educacional para Redes de Computadores e ADS.
