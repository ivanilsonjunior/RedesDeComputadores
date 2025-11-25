# Unicast, Broadcast e Multicast — Conceitos Essenciais
Material Didático — Redes de Computadores / ADS  
DIATINF — IFRN

Este documento apresenta um dos temas mais importantes da Camada de Enlace e também utilizado na Camada de Rede: **modos de entrega de quadros e pacotes**.

A forma como uma mensagem é endereçada determina o comportamento dos dispositivos de rede (switches, roteadores, APs).  
Aqui estão os três modos fundamentais: **Unicast**, **Broadcast** e **Multicast**.

---

# 1. Unicast

## Conceito
Unicast é a comunicação *um-para-um*.  
Um único remetente envia dados para **um único destinatário específico**.

## Na camada de enlace (Ethernet)
- O quadro contém um **MAC de destino específico**.  
  Ex.: `A4:5E:60:12:34:56`

## Comportamento no switch
- O switch *procura* o MAC na tabela CAM (MAC Address Table).  
- Encaminha o quadro **somente para a porta correta**.

## Exemplo típico
- Comunicação entre dois PCs em um switch.
- Acesso a um servidor via SSH, HTTP, etc.

---

# 2. Broadcast

## Conceito
Broadcast é a comunicação *um-para-todos* dentro da mesma rede local (LAN).

## Na camada de enlace
Endereço de broadcast:
- **FF:FF:FF:FF:FF:FF**

## Na camada de rede (IPv4)
Endereço de broadcast da rede:
- Ex.: `192.168.1.255` em uma rede /24  
Broadcast limitado:
- `255.255.255.255`

## Comportamento no switch
- O quadro broadcast é enviado **para todas as portas**, exceto por onde chegou.

## Exemplos típicos
- ARP Request  
- DHCP Discover  
- Anúncios de serviços em LAN  

---

# 3. Multicast

## Conceito
Multicast é a comunicação *um-para-muitos*, direcionada a um grupo específico de receptores.

Nem todos recebem — apenas quem faz parte do grupo multicast.

## Na camada de enlace (Ethernet)
Faixa de MAC multicast:
- **01:00:5E:xx:xx:xx**

## Na camada de rede (IPv4)
Faixa de endereços multicast:
- **224.0.0.0 a 239.255.255.255** (Classe D)

Exemplos:
- 224.0.0.1 → Todos os hosts  
- 224.0.0.5 → Roteadores OSPF  
- 224.0.0.251 → mDNS (Apple Bonjour)

## Comportamento no switch
- Switch usa **IGMP Snooping** para saber quais portas desejam receber multicast.
- Sem IGMP Snooping, multicast vira broadcast.

## Exemplos típicos
- IPTV  
- Videoconferência em grupo  
- Protocolos de roteamento (OSPF, RIPng)  
- IoT e descoberta de serviços  

---

# 4. Comparação Geral

| Tipo       | Alcance                   | Destinatários         | Exemplo            |
|------------|---------------------------|------------------------|--------------------|
| Unicast    | 1 → 1                     | Host específico        | SSH, HTTP          |
| Broadcast  | 1 → Todos (LAN)           | Toda a rede local     | ARP, DHCP          |
| Multicast  | 1 → Grupo interessado     | Hosts inscritos        | IPTV, OSPF, mDNS   |

---

# 5. Exercícios

## 5.1 — Classifique as situações abaixo:
a) PC solicitando o endereço MAC via ARP → _________  
b) IPTV enviando vídeo para vários assinantes → _________  
c) Cliente acessando um servidor web → _________  

---

## 5.2 — Explique:
- Por que switches não encaminham broadcast além da LAN?  
- Por que multicast é mais eficiente que broadcast?

---

## 5.3 — Pesquise e responda:
- Qual é a função do IGMP?  
- O que acontece se um switch **não** tiver IGMP Snooping?

---

# 6. Resumo Final

- **Unicast** → entrega dirigida  
- **Broadcast** → entrega para todos  
- **Multicast** → entrega para um grupo específico  

Esses conceitos são fundamentais para entender:
- Ethernet  
- Wi-Fi  
- ICMP  
- IPv4  
- Protocolos de roteamento  
- Serviços modernos como streaming e IoT  

---

DIATINF — IFRN  
Material educacional para Redes de Computadores e ADS.
