# Unidade 2 — API de Sockets
Material adaptado do curso **Programação para Redes (NCT)** — DIATINF/IFRN

> Pré-requisito: [`01_introducao_sockets.md`](01_introducao_sockets.md). Aqui colocamos a teoria em prática: criação de sockets, ciclo de vida completo de servidor e cliente TCP, envio/recebimento de dados e comunicação UDP. Os scripts prontos [`tcp_echo_server_python3.py`](tcp_echo_server_python3.py) / [`tcp_echo_client_python3.py`](tcp_echo_client_python3.py) / [`udp_echo_server_python3.py`](udp_echo_client_python3.py) implementam exatamente o que é descrito aqui.

---

## 1. O socket como abstração do sistema operacional

Uma aplicação não acessa a placa de rede nem implementa o TCP/UDP diretamente — ela pede ao sistema operacional a criação de um **socket**, um ponto de comunicação intermediário entre a aplicação e a pilha de protocolos.

```
Aplicação Python
      |
API BSD Sockets
      |
Sistema Operacional (Kernel)
      |
TCP / UDP / IP / Interface de Rede
```

### 1.1 Socket como recurso do SO

Ao criar um socket, o kernel reserva estruturas internas: protocolo utilizado, endereços IP envolvidos, portas de origem/destino, buffers de transmissão e recepção, estado da conexão (TCP), temporizadores. A aplicação não manipula essas estruturas diretamente — só interage com um **descritor** (um número inteiro que identifica o recurso).

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# internamente pode ser o descritor 3, 4, 5...
sock.fileno()  # retorna esse número
```

### 1.2 Analogia com arquivos

Nos sistemas Unix, sockets são tratados de forma semelhante a arquivos:

| Operação em arquivos | Operação em sockets |
|---|---|
| Abrir um arquivo | Criar um socket |
| Ler dados | Receber dados (`recv`) |
| Escrever dados | Enviar dados (`send`) |
| Fechar o arquivo | Fechar o socket (`close`) |

Mas um socket **não é** um arquivo: transporta dados transitórios entre aplicações, não armazena conteúdo permanente em disco.

### 1.3 Por que usar uma API?

Sem ela, cada aplicação teria que reimplementar TCP, UDP, IPv4/IPv6, ARP, controle de congestionamento, checksums, etc. A API BSD Sockets resume tudo isso a poucas funções: `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, `recv()`.

---

## 2. Criação de sockets — `socket()`

```python
socket.socket(family, type, proto=0)
```

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Essa chamada **não** estabelece conexão nenhuma — só solicita ao SO a criação do recurso (reserva memória, cria o descritor, inicializa buffers).

### 2.1 Família de endereçamento (`family`)

| Constante | Significado |
|---|---|
| `socket.AF_INET` | Endereços IPv4 |
| `socket.AF_INET6` | Endereços IPv6 |

### 2.2 Tipo do socket (`type`)

| Constante | Comunicação |
|---|---|
| `socket.SOCK_STREAM` | Fluxo contínuo (tipicamente TCP) |
| `socket.SOCK_DGRAM` | Datagramas (tipicamente UDP) |

### 2.3 Protocolo (`proto`)

Quase sempre `0` — o SO escolhe automaticamente o protocolo mais adequado ao tipo pedido (TCP para `SOCK_STREAM`, UDP para `SOCK_DGRAM`).

### 2.4 Combinações mais comuns

| Família | Tipo | Protocolo típico |
|---|---|---|
| `AF_INET` | `SOCK_STREAM` | TCP sobre IPv4 |
| `AF_INET` | `SOCK_DGRAM` | UDP sobre IPv4 |
| `AF_INET6` | `SOCK_STREAM` | TCP sobre IPv6 |
| `AF_INET6` | `SOCK_DGRAM` | UDP sobre IPv6 |

---

## 3. Ciclo de vida do servidor TCP

```
socket() → bind() → listen() → accept() → recv() → send() → close()
```

| Função | Finalidade |
|---|---|
| `socket()` | Cria o socket |
| `bind()` | Associa o socket a um endereço IP e uma porta |
| `listen()` | Coloca o socket em modo de escuta |
| `accept()` | Aceita uma nova conexão |
| `recv()` | Recebe dados do cliente |
| `send()` | Envia dados ao cliente |
| `close()` | Encerra a comunicação |

### 3.1 `bind()` — associando o socket a um endereço

```python
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 5000))
```

- **Endereço IP**: `"127.0.0.1"` restringe a conexões locais; um IP específico (`"192.168.1.100"`) restringe a essa interface; `"0.0.0.0"` aceita conexões vindas de **qualquer** interface de rede da máquina (Ethernet, Wi-Fi, loopback) — configuração comum em servidores reais.
- **Porta**: número que os clientes deverão usar para se conectar.
- **Conflito**: só um socket pode estar associado a um mesmo par (IP, porta) por vez. Tentar repetir gera `Address already in use`.

### 3.2 `listen()` — modo de escuta

```python
servidor.listen(5)
```

Coloca o socket em estado `LISTEN`, pronto para aceitar conexões. O parâmetro (**backlog**) define o tamanho máximo da fila de conexões pendentes — se vários clientes tentam conectar ao mesmo tempo, os que não estão sendo atendidos aguardam nessa fila (o valor real pode ser limitado pelo SO).

### 3.3 `accept()` — aceitando conexões

```python
socket_cliente, endereco = servidor.accept()
```

Duas características fundamentais:

1. **É bloqueante**: a execução para até que um cliente se conecte.
2. **Cria um novo socket**: `accept()` não transforma o socket de escuta em socket de comunicação — ele **cria outro socket**, dedicado exclusivamente àquele cliente. O socket de escuta original continua livre para aceitar novas conexões. Essa separação é a base dos servidores concorrentes (Unidade 3).

```
Socket de Escuta --- accept() ---> Novo Socket (Cliente A)
       |
  continua aceitando novos clientes
```

`endereco` é uma tupla `(ip_cliente, porta_cliente)`, por exemplo `('192.168.1.15', 53482)` — útil para logging, autenticação ou identificação do cliente.

### 3.4 `recv()` / `send()` / `close()`

```python
dados = socket_cliente.recv(1024)          # recebe até 1024 bytes
socket_cliente.send(b"Mensagem recebida")  # envia bytes
socket_cliente.close()                     # libera buffers, memória, descritores
```

### 3.5 Ciclo completo

```
Criar o socket → Escolher IP e porta → Modo de escuta → Aceitar conexão
→ Receber dados → Processar → Enviar resposta → Fechar conexão
```

Esse ciclo se repete continuamente enquanto o servidor está de pé.

---

## 4. Ciclo de vida do cliente TCP

```
socket() → connect() → send() → recv() → close()
```

Note que o cliente **não** usa `bind()`, `listen()` nem `accept()` — essas são exclusivas do servidor.

### 4.1 `connect()` — estabelecendo a conexão

```python
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("192.168.1.100", 5000))
```

Internamente, o SO: escolhe uma **porta efêmera** para o cliente, cria a entrada da conexão TCP, envia a solicitação (SYN), aguarda a resposta do servidor e conclui o handshake. Só depois disso a aplicação pode enviar/receber dados.

```
Cliente                          Servidor
socket()
connect() ---- SYN --------------->
         <---- SYN/ACK -------------
---- ACK ------------------------->
Conexão estabelecida
```

### 4.2 Endereço e porta do servidor

O primeiro parâmetro de `connect()` é o computador de destino (IP, hostname ou `127.0.0.1` para testes locais); o segundo é a porta do **serviço**, não do cliente. A porta que o cliente usa é escolhida automaticamente pelo SO (porta efêmera) e normalmente não precisa ser informada pelo programador.

### 4.3 Erros de conexão e timeout

Situações comuns: servidor desligado, porta errada, IP inválido, firewall bloqueando. O erro típico é `ConnectionRefusedError`/`OSError`. Boas práticas:

```python
try:
    cliente.connect(("192.168.1.100", 5000))
except OSError as erro:
    print(erro)
```

Também é possível limitar o tempo de espera:

```python
cliente.settimeout(5)  # connect()/recv() aguardam no máximo 5s
```

### 4.4 Ciclo completo

```
Criar o socket → Informar endereço do servidor → Conectar
→ Enviar solicitação → Receber resposta → Encerrar a conexão
```

### 4.5 Comparando servidor e cliente TCP

| Servidor TCP | Cliente TCP |
|---|---|
| `socket()` | `socket()` |
| `bind()` | `connect()` |
| `listen()` | `send()` |
| `accept()` | `recv()` |
| `recv()` | `close()` |
| `send()` | — |
| `close()` | — |

---

## 5. Envio e recebimento no TCP

### 5.1 TCP transporta bytes, não "mensagens"

O TCP não sabe o que é uma string, um objeto ou uma mensagem — ele transmite apenas uma **sequência contínua de bytes**. `"BitDogLab"` vira `42 69 74 44 6F 67 4C 61 62` para a pilha de protocolos; cabe à aplicação dar significado a esses bytes.

### 5.2 `send()` x `sendall()`

```python
enviados = cliente.send(dados)   # pode enviar SÓ PARTE dos dados; retorna quantos bytes foram aceitos
cliente.sendall(dados)           # insiste até enviar tudo, ou lança erro
```

Na prática, **use `sendall()`** sempre que quiser garantir que a mensagem inteira seja entregue ao buffer do sistema.

### 5.3 Strings precisam virar bytes

Sockets trabalham só com `bytes`. Uma `str` precisa ser convertida com `.encode()` (tipicamente `"utf-8"`) antes de enviar, e os bytes recebidos precisam de `.decode()` para voltar a ser texto:

```python
cliente.sendall("Olá servidor".encode("utf-8"))
...
dados = servidor_socket.recv(1024)
print(dados.decode("utf-8"))
```

### 5.4 `recv()` é bloqueante e não garante o tamanho pedido

```python
dados = cliente.recv(1024)
```

`1024` é o **máximo**, não o exato — o SO pode devolver de 1 a 1024 bytes, dependendo do que já chegou ao buffer de recepção. Enquanto não há dados, `recv()` bloqueia a execução.

### 5.5 Detectando o fim da conexão

Quando o outro lado fecha a conexão corretamente, `recv()` retorna `b""` (bytes vazio). Esse é o padrão clássico de loop de um servidor TCP:

```python
while True:
    dados = sock.recv(1024)
    if not dados:
        break  # cliente encerrou a conexão
    ...
```

### 5.6 TCP é fluxo — a aplicação define os limites das mensagens

Como o TCP não preserva os limites de cada `send()`, dois envios separados:

```python
cliente.sendall(b"ABC")
cliente.sendall(b"DEF")
```

podem chegar ao outro lado como `ABCDEF`, como `AB` + `CDEF`, ou de qualquer outra forma fragmentada — tudo é válido. Estratégias comuns para delimitar mensagens:

- **Delimitador**: ex. `TEMP:27.5\n`, lendo até encontrar `\n`.
- **Tamanho prefixado**: ex. `0012Temperatura`, onde os 4 primeiros caracteres informam o tamanho do restante.
- **Tamanho fixo**: sempre ler exatamente N bytes por mensagem.

Protocolos reais como HTTP resolvem isso com cabeçalhos (`Content-Length`) ou *chunked transfer encoding* — justamente porque o TCP só entrega um fluxo de bytes.

### 5.7 Exemplo completo (par cliente/servidor)

```python
# Cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 5000))
cliente.sendall("Olá servidor".encode("utf-8"))
cliente.close()
```

```python
# Servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 5000))
servidor.listen()
cliente, endereco = servidor.accept()
dados = cliente.recv(1024)
print(dados.decode("utf-8"))
cliente.close()
servidor.close()
```

Ver a versão completa e comentada em [`tcp_echo_server_python3.py`](tcp_echo_server_python3.py) e [`tcp_echo_client_python3.py`](tcp_echo_client_python3.py).

---

## 6. Comunicação com UDP

Sem conexão prévia: cada datagrama já carrega tudo que é preciso para o SO encaminhá-lo.

```
TCP: connect() → conexão estabelecida → dados
UDP: datagrama → (pronto, já foi)
```

### 6.1 Ciclo de vida — servidor UDP

```
socket() → bind() → recvfrom() → sendto() → close()
```

Sem `listen()`/`accept()` — não há conexões para aceitar, cada datagrama é tratado independentemente.

```python
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("0.0.0.0", 5000))

dados, endereco = servidor.recvfrom(1024)  # (bytes recebidos, (ip, porta) de quem enviou)
servidor.sendto(b"OK", endereco)           # responde exatamente para quem enviou
```

### 6.2 Ciclo de vida — cliente UDP

```
socket() → sendto() → recvfrom() → close()
```

Sem `connect()` — o destino é informado a cada envio:

```python
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.sendto(b"Temperatura:27", ("192.168.1.100", 5000))
dados, endereco = cliente.recvfrom(1024)
```

### 6.3 `sendto()` e `recvfrom()`

`sendto(dados, (ip_destino, porta_destino))` empacota e envia; `recvfrom(tamanho)` retorna `(dados, endereco_remetente)`. Um mesmo socket pode receber (e responder) mensagens de **múltiplos clientes diferentes**, já que cada datagrama informa sua origem — não é preciso um socket por cliente como acontece com `accept()` no TCP.

### 6.4 Comparando TCP e UDP na API

| | TCP | UDP |
|---|---|---|
| Existe conexão | Sim | Não |
| Conectar | `connect()` | `sendto()` |
| Aceitar conexão | `accept()` | não existe |
| Receber | `recv()` | `recvfrom()` |
| Enviar | `send()`/`sendall()` | `sendto()` |
| Socket por cliente | Sim (um novo por `accept()`) | Não (um socket atende todos) |

Ver a implementação completa em [`udp_echo_server_python3.py`](udp_echo_server_python3.py) e [`udp_echo_client_python3.py`](udp_echo_client_python3.py).

---

## Resumo da Unidade 2

- Servidor TCP: `socket() → bind() → listen() → accept() → recv()/send() → close()`.
- Cliente TCP: `socket() → connect() → send()/recv() → close()`.
- `accept()` sempre cria um **novo socket** por cliente — o de escuta nunca "vira" o de conversa.
- TCP transmite **bytes**, não mensagens — cabe à aplicação delimitar onde cada mensagem começa/termina.
- UDP dispensa conexão: `sendto()`/`recvfrom()` carregam o endereço a cada chamada.

**Próximo passo**: [`03_servidores_concorrentes.md`](03_servidores_concorrentes.md) — como atender vários clientes ao mesmo tempo, com threads e `asyncio`.
