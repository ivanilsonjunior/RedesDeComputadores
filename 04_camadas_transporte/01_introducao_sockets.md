# Unidade 1 — Introdução aos Sockets
Material adaptado do curso **Programação para Redes (NCT)** — DIATINF/IFRN

> Esta unidade e as três seguintes (`02_api_sockets.md`, `03_servidores_concorrentes.md`, `04_representacao_dados_struct.md`) formam uma trilha de **programação** de sockets que complementa a teoria de camada de transporte já apresentada no [`README.md`](README.md) deste módulo. Comece por aqui se você ainda não programou nada com sockets.

---

## 1. Comunicação entre processos

Quando utilizamos um navegador para acessar um site, enviamos uma mensagem pelo WhatsApp ou consultamos o DNS, estamos usando aplicações que trocam informações através da rede. Por trás dessa comunicação existem mecanismos implementados pelo sistema operacional e pelos protocolos da arquitetura TCP/IP que permitem que programas em computadores diferentes se encontrem e troquem dados de forma organizada.

### 1.1 Processos e aplicações distribuídas

Um **processo** é um programa em execução. O sistema operacional cria, executa, interrompe e finaliza processos, controlando o acesso à memória, ao processador e aos recursos de entrada e saída.

Em uma **aplicação distribuída**, cada processo executa uma parte da solução e coopera com os demais através da troca de mensagens — normalmente processos em computadores diferentes, conectados por uma rede. Essa arquitetura distribui a carga de processamento, aumenta a disponibilidade do serviço e facilita a escalabilidade.

Exemplos: navegação na Web, correio eletrônico, armazenamento em nuvem, sistemas bancários, mensagens instantâneas, streaming.

### 1.2 Comunicação local x comunicação em rede

- **Comunicação local**: dois processos no mesmo computador. Não precisa de rede — o sistema operacional oferece memória compartilhada, pipes, filas de mensagens, sinais e sockets locais (Unix Domain Sockets). Baixa latência.
- **Comunicação em rede**: processos em computadores diferentes. Os dados atravessam switches e roteadores até o destino, dependendo da pilha TCP/IP. Introduz desafios: atrasos, perdas, falhas de conexão, diferenças entre sistemas operacionais.

### 1.3 Comunicação entre processos (IPC)

**IPC (Interprocess Communication)** é o conjunto de mecanismos do sistema operacional que permite a dois ou mais processos compartilhar dados e sincronizar atividades. Quando os processos estão em computadores diferentes, o principal mecanismo de IPC é o **socket**, que funciona como interface entre a aplicação e a pilha TCP/IP.

### 1.4 O papel dos protocolos

Uma conexão física entre dois computadores não basta para haver comunicação entre aplicações — é preciso que ambas sigam regras comuns (**protocolos**) sobre: como estabelecer conexão, identificar os participantes, organizar os dados, detectar erros, confirmar recebimento e encerrar a comunicação.

Na arquitetura TCP/IP: o **IP** identifica computadores; o **TCP** fornece comunicação confiável orientada à conexão; o **UDP** oferece comunicação simples baseada em datagramas; o **HTTP** permite comunicação entre navegadores e servidores; o **DNS** traduz nomes em endereços IP.

---

## 2. Modelo Cliente/Servidor

O **Cliente/Servidor** é a arquitetura de comunicação predominante em sistemas distribuídos. Existem dois papéis:

- **Cliente**: inicia a comunicação, solicitando um serviço.
- **Servidor**: permanece aguardando solicitações e responde quando um cliente conecta.

```
            Solicitação
+-----------+ -----------> +-----------+
|  Cliente  |              |  Servidor |
+-----------+              +-----------+
     ^                            |
     |                            |
     +-------- Resposta ---------+
```

### 2.1 Cliente — comportamento ativo

O cliente decide **quando** iniciar a comunicação: localiza o servidor, estabelece a conexão, envia solicitações, recebe respostas e apresenta o resultado ao usuário. Exemplos: navegadores, clientes SSH/FTP, apps de e-mail e mensagens.

### 2.2 Servidor — comportamento passivo

O servidor permanece continuamente em execução, aguardando conexões: cria um socket, associa-se a uma porta conhecida, entra em espera, aceita conexões e as atende. Não procura clientes na rede — sua função é **estar disponível para ser encontrado**. Exemplos: servidores Web, DNS, banco de dados, arquivos, e-mail.

### 2.3 Requisição e resposta

```
Cliente                 Servidor
Requisição  ----------------->
                Processamento
Resposta    <-----------------
```

Uma única conexão pode envolver várias requisições/respostas — ao carregar uma página, o navegador pode solicitar o HTML, o CSS, imagens, scripts, etc., cada um em uma nova requisição.

### 2.4 Exemplos de aplicações Cliente/Servidor

| Aplicação | Cliente | Servidor |
|---|---|---|
| Navegação Web | Navegador | Servidor HTTP |
| Correio eletrônico | Cliente de e-mail | Servidor SMTP/IMAP |
| Transferência de arquivos | Cliente FTP | Servidor FTP |
| Acesso remoto | Cliente SSH | Servidor SSH |
| Banco de dados | Aplicação | Servidor de Banco de Dados |
| Resolução de nomes | Resolver DNS | Servidor DNS |

---

## 3. O problema do encontro (Rendezvous Problem)

**Pergunta central**: como duas aplicações em computadores diferentes conseguem se encontrar para iniciar uma comunicação?

Sem estratégia definida, nenhum dos lados sabe quem deve iniciar, para onde enviar, ou se o outro está pronto. A solução adotada pelas redes de computadores:

> Uma das aplicações inicia sua execução primeiro, associa-se a um endereço conhecido e permanece aguardando conexões; a outra inicia posteriormente e estabelece contato utilizando esse endereço.

Essa decisão é a base do modelo Cliente/Servidor: o **servidor** inicia primeiro, associa-se a uma porta conhecida e aguarda; o **cliente** inicia depois, localiza esse endereço e conecta.

**Analogia**: uma agência bancária (servidor) permanece aberta aguardando os clientes chegarem. O endereço da agência = endereço IP; o número do guichê = porta do serviço.

```
Servidor                          Cliente
Inicia
  |
Associa-se à porta
  |
Fica aguardando ------------------|
                                Inicia
                                  |
                          Localiza o servidor
                                  |
                          Solicita conexão
  |<--------------------------------
Aceita
  |
Comunicação inicia
```

---

## 4. Endereços e identificação de aplicações

Para localizar um serviço, o cliente precisa de: **endereço IP**, **porta** e **protocolo de transporte**.

### 4.1 Endereço IP

Identificador lógico da interface de rede.

- **IPv4**: 32 bits, 4 grupos decimais (`192.168.1.10`).
- **IPv6**: 128 bits (`2001:db8:1::15`), usado com `socket.AF_INET6`.
- **Loopback / localhost**: `127.0.0.1` (IPv4) ou `::1` (IPv6) — usado quando cliente e servidor rodam na mesma máquina; os dados não saem para a rede física, o que facilita testes.

### 4.2 Nome de host e resolução de nomes (DNS)

Nomes como `www.ifrn.edu.br` são mais fáceis de lembrar que endereços IP, mas a comunicação continua ocorrendo via IP. A conversão de nome → IP é a **resolução de nomes**, feita pelo **DNS**. Em Python: `socket.gethostbyname()`.

### 4.3 Portas

O endereço IP identifica o computador; a **porta** identifica *qual aplicação* naquele computador deve receber a conexão (um mesmo IP pode hospedar HTTP na porta 80, SSH na 22, um banco de dados na 3306, etc.).

Faixas de porta (0 a 65535):

| Faixa | Nome | Uso |
|---|---|---|
| 0–1023 | Portas conhecidas (*Well-Known*) | Serviços padronizados: HTTP 80, HTTPS 443, SSH 22, DNS 53, SMTP 25 |
| 1024–49151 | Portas registradas | Aplicações registradas na IANA e serviços corporativos; portas típicas de laboratório: 5000, 8000, 8080, 9000 |
| 49152–65535 | Portas efêmeras (*Dynamic/Ephemeral*) | Escolhidas automaticamente pelo SO para o **cliente**, usadas só durante aquela conexão |

Um mesmo computador pode manter várias conexões simultâneas com o(s) mesmo(s) servidor(es) porque cada conexão do cliente usa uma porta efêmera diferente.

### 4.4 Identificando uma aplicação na rede

A tripla **(endereço IP, porta, protocolo de transporte)** identifica univocamente uma aplicação de rede. Diferentes serviços podem compartilhar a mesma porta desde que usem protocolos de transporte distintos — ex.: DNS oferece serviço tanto em UDP quanto em TCP, ambos na porta 53.

Em Python, isso já aparece na criação do socket:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

`AF_INET` define a família de endereços (IPv4); `SOCK_STREAM` define o tipo de comunicação (ver seção 6). O endereço e a porta serão informados depois, em `bind()` ou `connect()` (Unidade 2).

---

## 5. Protocolos TCP e UDP

A camada de transporte oferece dois protocolos principais, escolhidos no momento da criação do socket.

### 5.1 TCP (Transmission Control Protocol)

**Orientado à conexão** e **confiável**: antes de transmitir, cliente e servidor executam o *three-way handshake* (SYN → SYN+ACK → ACK). O TCP garante, dentro do possível: entrega, ordenação, ausência de duplicatas, controle de fluxo (protege o receptor) e controle de congestionamento (protege a rede). Usado por HTTP/HTTPS, SSH, FTP, SMTP/IMAP/POP3, bancos de dados.

Corresponde a `socket.SOCK_STREAM`.

### 5.2 UDP (User Datagram Protocol)

**Não orientado à conexão**: cada mensagem (datagrama) é enviada independentemente, sem handshake, sem confirmação, sem retransmissão automática — protocolo de "melhor esforço". Em compensação, tem baixa sobrecarga e baixa latência. Usado por DNS, streaming, jogos on-line, VoIP, telemetria IoT.

Corresponde a `socket.SOCK_DGRAM`.

### 5.3 Comparação

| Característica | TCP | UDP |
|---|---|---|
| Orientado à conexão | Sim | Não |
| Comunicação | Fluxo contínuo de bytes | Datagramas independentes |
| Garantia de entrega | Sim | Não |
| Ordem dos dados | Garantida | Não garantida |
| Retransmissão | Sim | Não |
| Controle de fluxo/congestionamento | Sim | Não |
| Latência / desempenho | Maior / menor | Menor / maior |
| API de sockets | `SOCK_STREAM` | `SOCK_DGRAM` |

A escolha depende do requisito da aplicação: se a perda de dados é inaceitável, use TCP; se baixa latência importa mais do que entrega perfeita, UDP costuma ser melhor.

---

## 6. Tipos de sockets

`SOCK_STREAM` e `SOCK_DGRAM` **não são os protocolos em si** — são o *tipo de serviço* que a aplicação pede ao sistema operacional. Na prática, o SO quase sempre implementa `SOCK_STREAM` com TCP e `SOCK_DGRAM` com UDP, mas a API foi desenhada para ser independente da implementação exata.

```python
# Socket orientado a fluxo (tipicamente TCP)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket orientado a datagramas (tipicamente UDP)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

| | `SOCK_STREAM` | `SOCK_DGRAM` |
|---|---|---|
| Modelo | Fluxo contínuo | Datagramas |
| Conexão | Necessária | Não necessária |
| Preserva limites da mensagem | Não | Sim |
| Confiabilidade | Sim | Não garantida |
| Funções principais | `connect()`, `accept()`, `send()`, `recv()` | `sendto()`, `recvfrom()` |

---

## Resumo da Unidade 1

- Sockets existem para resolver o **problema do encontro**: o servidor se anuncia primeiro em um endereço conhecido; o cliente o localiza e inicia a conexão.
- Uma aplicação de rede é identificada pela tripla **IP + porta + protocolo**.
- **TCP** (`SOCK_STREAM`) é confiável e orientado à conexão; **UDP** (`SOCK_DGRAM`) é rápido e não orientado à conexão.

**Próximo passo**: [`02_api_sockets.md`](02_api_sockets.md) — como criar sockets e implementar o ciclo de vida completo de clientes e servidores TCP/UDP em Python.
