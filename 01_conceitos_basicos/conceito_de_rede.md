# Conceito de Rede de Computadores
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Uma **rede de computadores** é um conjunto de dispositivos autônomos interligados que trocam informações entre si, seguindo regras combinadas previamente.

Essa troca ocorre por meio de:
- um **meio físico** (cabo metálico, fibra óptica, rádio); e
- **protocolos**, que são o conjunto de regras que define *o quê* é enviado, *como* é formatado e *quando* pode ser transmitido.

Sem um protocolo em comum, dois dispositivos podem estar fisicamente conectados e mesmo assim não conseguirem se comunicar — da mesma forma que duas pessoas ligadas por telefone não se entendem se falam idiomas diferentes.

---

## Por que redes existem?

- **Compartilhar recursos**: arquivos, impressoras, conexão com a Internet, poder de processamento.
- **Comunicação e colaboração**: e-mail, mensageiros, videoconferência.
- **Centralização e backup**: servidores de arquivos, sistemas de backup em rede.
- **Computação distribuída**: várias máquinas cooperando em uma mesma tarefa (ex.: data centers, computação em nuvem).
- **Redundância e disponibilidade**: se um caminho falha, outro pode assumir.

---

## Componentes principais de uma rede

| Componente | Papel | Exemplos |
|---|---|---|
| **Dispositivos finais (hosts)** | Origem ou destino final dos dados | computador, celular, servidor, impressora de rede |
| **Equipamentos intermediários** | Encaminham dados entre hosts | switch, roteador, access point |
| **Meios físicos** | Transportam o sinal | cabo UTP, fibra óptica, rádio (Wi-Fi) |
| **Protocolos** | Definem as regras da comunicação | TCP/IP, HTTP, Ethernet |

> Aprofundamento sobre cada equipamento intermediário e meio físico: ver módulo [`06_componentes_fisicos/`](../06_componentes_fisicos/).

---

## Cliente e servidor: o modelo básico de comunicação

A maioria das aplicações de rede segue o modelo **cliente-servidor**:

- O **servidor** oferece um serviço e fica esperando por conexões (ex.: um site esperando visitantes).
- O **cliente** inicia a comunicação, solicitando o serviço (ex.: o navegador do usuário).

```
   Cliente                       Servidor
 (solicita)  ─────── pedido ────▶ (aguardando)
             ◀────── resposta ───
```

Esse modelo aparece em praticamente todos os protocolos estudados neste repositório (HTTP, DNS, SMTP, TCP/UDP echo) — ver módulos [`03_camadas_aplicacao/`](../03_camadas_aplicacao/) e [`04_camadas_transporte/`](../04_camadas_transporte/).

Existe também o modelo **P2P (peer-to-peer)**, em que não há um servidor central fixo: cada dispositivo pode atuar como cliente e servidor ao mesmo tempo (ex.: BitTorrent).

---

## Endereçamento: como um dispositivo é identificado na rede

Para que uma mensagem chegue ao destino certo, cada dispositivo precisa de um identificador único dentro da rede:

- **Endereço MAC** — identifica a interface de rede fisicamente (camada de Enlace). Ex.: `AA:BB:CC:DD:EE:FF`.
- **Endereço IP** — identifica logicamente um dispositivo dentro de uma rede (camada de Rede). Ex.: `192.168.1.10`.
- **Porta** — identifica um processo/aplicação específico dentro do dispositivo (camada de Transporte). Ex.: porta 80 para HTTP.

Esses três níveis de endereçamento serão detalhados nos módulos [`02_modelos_de_comunicacao/`](../02_modelos_de_comunicacao/), [`05_camadas_rede/`](../05_camadas_rede/) e [`06_componentes_fisicos/`](../06_componentes_fisicos/).

---

## Resumo

Uma rede de computadores existe para permitir que dispositivos **autônomos** troquem dados de forma **combinada e identificável**: usando um meio físico para transportar o sinal, protocolos para dar significado a esse sinal, e endereços para saber quem é quem.

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
