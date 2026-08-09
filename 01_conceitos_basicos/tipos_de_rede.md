# Tipos de Redes
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Redes são classificadas principalmente pela sua **abrangência geográfica**, mas também importam sua **propriedade** (quem administra) e a **tecnologia** usada para conectar os dispositivos.

---

## ✔️ PAN — Personal Area Network
Rede de curtíssimo alcance, ao redor de uma única pessoa ou dispositivo.
- Alcance: poucos metros.
- Exemplos: Bluetooth (fones de ouvido, teclado), NFC, USB, Zigbee.
- Uso típico: conectar acessórios pessoais, sem necessidade de infraestrutura fixa.

## ✔️ LAN — Local Area Network
Rede local, restrita a um único prédio, andar, laboratório ou casa, geralmente sob administração de um único responsável.
- Alcance: até algumas centenas de metros (limitado pelo cabeamento e pelos equipamentos ativos, não por uma regra fixa).
- Meios comuns: Ethernet cabeada (par trançado) e Wi-Fi.
- Exemplos: rede de um laboratório do IFRN, rede doméstica.

> Algumas literaturas também citam a **CAN (Campus Area Network)**: várias LANs interligadas dentro de um mesmo campus/conjunto de prédios próximos, ainda sob uma administração única — um estágio intermediário entre LAN e MAN.

## ✔️ MAN — Metropolitan Area Network
Rede que cobre uma cidade ou região metropolitana, interligando múltiplas LANs.
- Alcance: dezenas de quilômetros.
- Exemplos: rede de um provedor de internet local, backbone que interliga campi de uma universidade em cidades diferentes.

## ✔️ WAN — Wide Area Network
Rede de longa distância, cobrindo países ou continentes, formada pela interligação de várias redes menores.
- Alcance: global.
- Exemplo máximo: a própria **Internet** — uma "rede de redes".

---

## Comparação rápida

| Tipo | Alcance típico | Administração | Exemplos |
|------|-----------------|----------------|----------|
| PAN | até ~10 m | pessoal | Bluetooth, NFC, fones sem fio |
| LAN | até algumas centenas de metros | única organização | rede de laboratório, rede doméstica |
| MAN | dezenas de km | provedor/instituição | rede metropolitana, backbone de campus |
| WAN | ilimitado (global) | múltiplas organizações interligadas | Internet |

---

## Outras classificações importantes

Além da abrangência, redes também costumam ser descritas por:

- **Propriedade**: rede **privada** (ex.: LAN de uma empresa, com acesso controlado) x rede **pública** (ex.: Internet).
- **Topologia**: como os dispositivos estão organizados fisicamente/logicamente — ver [`topologias.md`](topologias.md).
- **Meio de transmissão**: rede **cabeada** x rede **sem fio (wireless)**.

Essas classificações não são excludentes: uma rede doméstica, por exemplo, é ao mesmo tempo uma **LAN**, **privada**, em topologia **estrela** e majoritariamente **sem fio**.

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
