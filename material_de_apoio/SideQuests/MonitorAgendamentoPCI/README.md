# 📅 SideQuest — Monitor de Vagas de Agendamento (PCI-RN)

Este SideQuest implementa um **monitor de vagas** para o site de agendamento da Carteira de Identidade Nacional do Rio Grande do Norte ([agendamento.pci.rn.gov.br](https://agendamento.pci.rn.gov.br/public/agendamento)). Você escolhe uma cidade, o script consulta a API do site periodicamente e dispara uma **notificação do sistema** assim que surgir um horário livre.

---

## 🎯 Objetivo do SideQuest

Permitir que o aluno:

- Consuma uma **API REST real** (via `requests`), na prática de "camada de aplicação";
- Pratique **engenharia reversa de uma API não documentada**, a partir do tráfego de uma SPA (Single Page Application);
- Implemente **polling** (consulta periódica) como alternativa simples a webhooks/notificações push;
- Trabalhe com **notificações do sistema operacional** a partir de um script Python.

---

## 🧠 Conceitos de Redes/Aplicação Abordados

- Protocolo HTTP (requisições GET, query strings, JSON)
- Cliente REST consumindo uma API de terceiros
- Diferença entre uma página renderizada no servidor e uma SPA (Next.js) que busca dados via JavaScript depois de carregar
- Polling vs. notificação em tempo real (por que este script consulta de tempos em tempos, em vez de "ficar ouvindo" o servidor)

---

## 🕵️ Como a API foi descoberta

O site é uma SPA em Next.js — o HTML inicial vem praticamente vazio, e os dados aparecem via chamadas JavaScript depois. Para descobrir os endpoints usados:

1. Abra o site no navegador, aperte F12 → aba **Network**, filtre por `Fetch/XHR`;
2. Interaja com a página (escolha uma cidade, uma data) e observe as requisições que aparecem;
3. Alternativamente, os arquivos `.js` da pasta `/_next/static/chunks/...` (visíveis também em "Sources") contêm o código-fonte da aplicação, incluindo os caminhos de API usados internamente.

Foi assim que chegamos aos 4 endpoints usados neste script (todos públicos, sem necessidade de login):

| Endpoint | O que retorna |
|---|---|
| `GET /api/get-locais/public` | Lista de todas as cidades/unidades de atendimento |
| `GET /api/ordens/public` | "Lotes" de vagas (chamados de *ordens*) por cidade, com status `LIBERADO`/`DESLIBERADO` |
| `GET /api/ordens/public/datas?ordem=<id>` | Datas com vaga para um lote específico |
| `GET /api/vagas/horas?ordem=<id>&data=<data>` | Horários ainda livres numa data específica |

Quando o passo de datas ou de horários volta vazio, é exatamente a mesma situação que o próprio site mostra como a mensagem **"Novas vagas no próximo dia útil às 8h"** — o script reproduz essa mesma lógica.

---

## 📁 Estrutura da Pasta

```
MonitorAgendamentoPCI/
├── monitor_vagas.py
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar

### 1️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Rode o monitor

```bash
python3 monitor_vagas.py
```

### 3️⃣ Escolha a(s) cidade(s)

O script lista todas as localidades disponíveis com um número. Digite um único número (`2`) para monitorar uma cidade, ou vários separados por vírgula (`1,5,10`) para monitorar várias ao mesmo tempo.

### 4️⃣ Deixe rodando

A cada 5 minutos (configurável — veja `INTERVALO_SEGUNDOS` no topo do script) ele consulta a API para cada cidade escolhida e imprime o resultado no terminal. Quando encontrar uma vaga nova em qualquer uma delas, além de imprimir, ele dispara uma notificação do sistema via `notify-send` (Linux), identificando de qual cidade é a vaga.

---

## ⚠️ Observações Importantes

- **Este script só monitora e avisa — ele nunca agenda por você.** A etapa final de agendamento no site exige resolver um captcha, que existe justamente para garantir que um humano confirme o horário. Ao ser notificado, é você quem acessa o site e agenda manualmente — e rápido, porque vagas de identidade costumam sumir em segundos.
- `notify-send` já vem instalado por padrão na maioria das distribuições Linux Desktop (pacote `libnotify-bin` no Ubuntu/Debian). Se não estiver disponível, o script cai automaticamente para um aviso sonoro (`\a`) + texto no terminal.
- O intervalo padrão entre consultas é de **5 minutos**. Evite diminuir demais esse valor — é uma API pública de um serviço do governo, não documentada para uso por terceiros; consultas muito frequentes podem sobrecarregar o serviço ou fazer seu IP ser bloqueado.
- O script guarda em memória quais vagas (`ordem` + `data`) já foram notificadas, para não repetir o aviso a cada rodada — só avisa de novo se surgir uma vaga realmente nova.
- Se o site do PCI-RN mudar sua API (nomes de endpoints, formato de resposta), o script para de funcionar até ser atualizado — é o risco de depender de uma API não documentada.

---

## 💡 Sugestões de Extensão (Desafios)

- O script já monitora várias cidades numa única lista, uma de cada vez a cada rodada — para muitas cidades, revisitar o conceito de **concorrência** (Unidade 3 de `04_camadas_transporte/`) e consultar todas em paralelo com threads;
- Guardar as vagas já vistas em um arquivo, para sobreviver a reinícios do script;
- Enviar a notificação por outro canal (e-mail, Telegram, WhatsApp) além do `notify-send`;
- Rodar como um serviço em segundo plano (ex.: `systemd`, `cron`, ou um contêiner) em vez de precisar deixar o terminal aberto;
- Adaptar o script para outro site de agendamento público, praticando a mesma técnica de engenharia reversa de API.

---

## 📚 Aplicação Didática

Este SideQuest pode ser utilizado para:

- Demonstrações em sala de aula sobre como uma SPA se comunica com o backend;
- Introdução a engenharia reversa de APIs a partir do DevTools do navegador;
- Discussão sobre uso responsável de scraping/polling em serviços de terceiros;
- Exercício de camada de aplicação usando uma API do mundo real, não simulada.

---

**SideQuest desenvolvido para fins educacionais no contexto da disciplina de Redes de Computadores. 🚀**
