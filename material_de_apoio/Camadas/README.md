# Camadas — Material Complementar de Sockets
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Esta pasta reúne exemplos de sockets **mais avançados e exploratórios** que os das disciplinas numeradas (`03_camadas_aplicacao/`, `04_camadas_transporte/`, `06_componentes_fisicos/`), organizados pela camada do modelo OSI/TCP-IP a que mais se relacionam.

> 💡 Recomendado depois de já ter estudado os módulos [`03_camadas_aplicacao/`](../../03_camadas_aplicacao/), [`04_camadas_transporte/`](../../04_camadas_transporte/) e [`06_componentes_fisicos/`](../../06_componentes_fisicos/) — aqui os exemplos combinam vários conceitos ao mesmo tempo (threads, descoberta de serviço, protocolos próprios) em vez de isolar um conceito por vez.

---

## 📂 Organização

| Pasta | Camada | Conteúdo |
|---|---|---|
| [`Aplicação/`](Aplicação/) | Aplicação | Servidor de comandos remoto via broadcast UDP (`Remoto.py`). |
| [`Enlace/`](Enlace/) | Enlace | Descoberta de dispositivos Bluetooth e broadcast UDP básico. |
| [`Transporte/Sockets/`](Transporte/Sockets/) | Transporte | Sockets TCP/UDP mais elaborados: sistema cliente-servidor orientado a objetos com autodescoberta, servidor HTTP mínimo, jogo de adivinhação em UDP e um classificador de imagens via TCP. |

---

## ⚠️ Sobre a qualidade didática deste material

Diferente dos módulos numerados, estes scripts foram escritos ao longo do tempo com objetivos variados (aula, demonstração rápida, side quest) e nem sempre têm o mesmo cuidado de comentários e tratamento de erros. Onde havia bugs que impediam a execução, eles foram corrigidos — mas o estilo de código continua mais "cru" que o dos módulos 01-06. Use isso a seu favor: é um bom material para **exercícios de leitura e depuração de código de terceiros**, uma habilidade tão importante quanto escrever código do zero.

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
