# Unidade 3 — Servidores Concorrentes
Material adaptado do curso **Programação para Redes (NCT)** — DIATINF/IFRN

> Pré-requisito: [`02_api_sockets.md`](02_api_sockets.md). Os exemplos práticos desta unidade estão em [`servidor_concorrente_threads.py`](servidor_concorrente_threads.py) e [`servidor_concorrente_asyncio.py`](servidor_concorrente_asyncio.py).

---

## 1. Servidor iterativo

Os servidores TCP/UDP construídos na Unidade 2 são **iterativos**: atendem **um cliente por vez**. Enquanto está processando um cliente, o servidor não retorna a `accept()` — novos clientes ficam esperando na fila do `listen()`.

```python
while True:
    cliente, endereco = servidor.accept()
    dados = cliente.recv(1024)
    cliente.sendall(b"OK")
    cliente.close()
```

```
Aceita Cliente 1 → Atende Cliente 1 → Encerra Cliente 1 → Aceita Cliente 2 → ...
```

**Vantagens**: implementação simples, fácil de depurar, baixo consumo de memória — ótimo para fins didáticos.

**Limitações**: tempo de espera cresce conforme chegam clientes; baixa utilização dos recursos do computador (múltiplos núcleos ociosos); baixa escalabilidade. Exemplo: se cada atendimento leva 20s e chegam 10 clientes ao mesmo tempo, o décimo só começa a ser atendido após ~180s — mesmo que a máquina tenha vários núcleos livres.

O problema não está na API BSD Sockets, e sim na lógica do programa: enquanto ele está em `recv()`/processando, ele não volta para `accept()`.

---

## 2. Servidor concorrente

Um **servidor concorrente** consegue atender vários clientes ao mesmo tempo: enquanto um cliente está sendo processado, o servidor continua aceitando novas conexões.

```
Servidor
   |
Socket de Escuta
   |
accept() recebe conexão
   |
 ┌─┼─┐
 A  B  C   ← atendimento simultâneo
```

### 2.1 Separando "aceitar" de "atender"

No modelo iterativo, `accept()` e o atendimento ocorrem sequencialmente na mesma thread. No modelo concorrente, depois de `accept()` o atendimento é **delegado** para outro fluxo de execução, e o laço principal volta imediatamente para `accept()`.

### 2.2 Cada cliente tem seu próprio socket

Como vimos na Unidade 2, `accept()` sempre cria um **novo socket** — o de escuta segue livre. Cada socket conectado mantém seus próprios buffers, endereço remoto e porta remota; dados de um cliente nunca se misturam com os de outro (isso é garantido pelo SO, não pela aplicação).

### 2.3 Recursos compartilhados e controle de concorrência

Mesmo com sockets isolados por cliente, a aplicação pode ter recursos **compartilhados** entre os atendimentos: um arquivo de log, uma lista de usuários conectados, um contador, uma conexão de banco de dados. Se dois atendimentos tentam atualizar o mesmo contador ao mesmo tempo sem coordenação, o resultado pode ficar incorreto — uma **condição de corrida** (*race condition*). Esse problema, e como evitá-lo, é tratado na seção 5 (Threads).

---

## 3. Como o sistema operacional diferencia as conexões

Se vários clientes usam a **mesma** porta do servidor, como o SO sabe qual pacote pertence a qual conexão?

### 3.1 A tupla da conexão

Uma conexão TCP é identificada de forma única pela combinação de quatro valores:

```
(IP_origem, Porta_origem, IP_destino, Porta_destino)
```

Exemplo — dois clientes conectados ao mesmo servidor `192.168.1.100:5000`:

```
Cliente A: (192.168.1.10, 51000, 192.168.1.100, 5000)
Cliente B: (192.168.1.11, 52000, 192.168.1.100, 5000)
```

O IP e a porta do servidor são iguais, mas o IP e a porta efêmera de cada cliente diferem — logo, as tuplas são diferentes. Até um mesmo computador cliente pode manter várias conexões simultâneas com o mesmo servidor, pois cada uma usa uma porta efêmera distinta.

### 3.2 Como isso é usado

A cada segmento TCP recebido, o SO extrai (IP origem, porta origem, IP destino, porta destino) e compara com sua tabela de conexões ativas, entregando os dados ao **socket conectado correto** — seja ele tratado por um processo, uma thread ou uma corrotina assíncrona.

Esse mecanismo é o que permite que um servidor atenda milhares de clientes simultaneamente usando uma única porta.

---

## 4. Modelo pai/filho (delegação de atendimento)

Depois que `accept()` aceita uma conexão, **quem** atende esse cliente depende da arquitetura escolhida:

| Arquitetura | Como o socket chega ao atendimento |
|---|---|
| Processos (`fork()`) | O processo filho **herda** o descritor do socket conectado |
| Threads | O objeto `socket` é **compartilhado** com a nova thread |
| `asyncio` | O socket é associado à **coroutine** responsável pela conexão |

Em todos os casos, o princípio é o mesmo: **aceitar rapidamente uma conexão e delegar seu atendimento**, para que o laço principal volte a chamar `accept()` o quanto antes. Historicamente, servidores Unix usavam `fork()` (um processo por cliente, isolamento total, mas caro de criar); hoje, `threading` e `asyncio` são as abordagens mais usadas em Python — e são o foco das próximas seções.

---

## 5. Concorrência com Threads

Uma **thread** é um fluxo de execução independente dentro do mesmo processo. Threads de um mesmo processo compartilham memória (variáveis globais, listas, dicionários, conexões abertas), mas cada uma tem sua própria pilha de execução.

### 5.1 Uma thread por cliente

```python
import socket
import threading

def atender_cliente(cliente, endereco):
    while True:
        dados = cliente.recv(1024)
        if not dados:
            break
        cliente.sendall(dados)
    cliente.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 5000))
servidor.listen()

while True:
    cliente, endereco = servidor.accept()
    thread = threading.Thread(target=atender_cliente, args=(cliente, endereco))
    thread.start()
```

`target` é a função que a thread vai executar; `args` são os argumentos dela; `start()` inicia a execução **sem bloquear** o laço principal, que volta imediatamente a `accept()`.

> Ver a implementação completa em [`servidor_concorrente_threads.py`](servidor_concorrente_threads.py).

### 5.2 Operações bloqueantes por thread

`recv()` continua bloqueante — mas agora o bloqueio afeta só a thread daquele cliente. As demais threads continuam executando normalmente (essa independência é a principal vantagem do modelo).

### 5.3 Condições de corrida e sincronização

Threads compartilham memória — se duas threads incrementam a mesma variável ao mesmo tempo sem coordenação:

```python
contador = 0
# Thread A e Thread B executam, "ao mesmo tempo":
contador += 1
```

o resultado esperado seria `2`, mas dependendo do escalonamento pode dar `1` (uma escrita "pisou" na outra). Isso é uma **condição de corrida**.

A solução é um **Lock**:

```python
lock = threading.Lock()

with lock:
    contador += 1
```

Enquanto uma thread está dentro do `with lock:`, as demais aguardam — só uma por vez modifica o recurso compartilhado.

### 5.4 Custo e escalabilidade

Cada thread tem custo: pilha própria, estruturas do SO, tempo de criação e de troca de contexto (*context switching*). Para poucos/médios clientes simultâneos, "uma thread por cliente" é simples e eficiente. Para milhares de conexões, o custo acumulado de tantas threads pode pesar — nesses casos usam-se *pools* de threads ou `asyncio`.

### 5.5 Boas práticas

- Thread principal só aceita conexões; a lógica de atendimento fica em função separada.
- Feche o socket ao final do atendimento.
- Proteja recursos compartilhados com `Lock` quando necessário.
- Evite tarefas demoradas desnecessárias dentro de uma thread de atendimento.

> **Nota sobre o GIL**: o CPython usa um *Global Interpreter Lock*, que permite só uma thread executando bytecode Python por vez. Isso não invalida o modelo — chamadas de rede como `recv()`, `send()` e `accept()` liberam o GIL enquanto aguardam o SO, permitindo que outras threads rodem nesse intervalo. Por isso threads continuam sendo uma boa solução para aplicações de rede (dominadas por espera de I/O, não por cálculo).

---

## 6. Concorrência com `asyncio`

Uma alternativa mais moderna: em vez de uma thread por cliente, um único fluxo de execução (**event loop**) alterna entre várias conexões, cedendo o controle sempre que uma operação de rede precisa esperar.

### 6.1 O problema das operações bloqueantes

`recv()` tradicional bloqueia a thread inteira. Com uma única thread, isso pararia o atendimento de todos os demais clientes. `asyncio` resolve isso permitindo que, ao aguardar E/S, o controle volte ao *event loop*, que executa outra tarefa pronta.

### 6.2 Corrotinas e `await`

```python
async def atender_cliente(reader, writer):
    dados = await reader.read(1024)
    writer.write(dados)
    await writer.drain()
    writer.close()
    await writer.wait_closed()
```

- `async def` declara uma **corrotina** — pode suspender e retomar sua execução.
- `await` marca um ponto em que a corrotina pode ser suspensa enquanto aguarda algo (leitura de rede, por exemplo), devolvendo o controle ao *event loop* para que outras corrotinas continuem.

### 6.3 Cada cliente é uma *Task*

```
Event Loop
   |
Task Cliente A
Task Cliente B
Task Cliente C
```

Embora exista apenas uma thread, várias conexões avançam "ao mesmo tempo": enquanto o Cliente A está em `await reader.read(...)` (aguardando dados), o *event loop* já está executando o Cliente B.

> Ver a implementação completa em [`servidor_concorrente_asyncio.py`](servidor_concorrente_asyncio.py).

### 6.4 Vantagens e limitações

**Vantagens**: menor consumo de memória, poucas trocas de contexto, ótima escalabilidade para milhares de conexões simultâneas dominadas por espera de rede (I/O-bound). Base de frameworks como FastAPI, aiohttp, `websockets`.

**Limitações**: código que consome CPU intensivamente (cálculo pesado) **bloqueia o event loop inteiro**, travando todas as outras conexões — nesse caso, usa-se threads/processos separados para essa parte específica.

---

## 7. Threads x `asyncio`

| Critério | Threads | `asyncio` |
|---|---|---|
| Unidade de execução | Thread | Corrotina |
| Escalonamento | Sistema operacional (preemptivo) | Event loop (cooperativo) |
| Operações de rede | Bloqueantes por thread | Não bloqueantes com `await` |
| Compartilhamento de memória | Direto (mesmo processo) | Direto (mesmo processo) |
| Custo de criação | Maior | Menor |
| Escalabilidade | Boa para poucos/médios clientes | Muito alta para I/O-bound |
| Curva de aprendizado | Menor | Maior (`async`/`await`, event loop) |
| Reuso de bibliotecas tradicionais | Fácil | Precisa de bibliotecas compatíveis com `asyncio` |

**Quando usar threads**: poucos clientes simultâneos, quer reaproveitar código/bibliotecas síncronas já existentes, prioriza simplicidade.

**Quando usar `asyncio`**: muitos clientes simultâneos, workload dominado por espera de rede, precisa de alta escalabilidade.

Na prática, é comum **combinar** as duas abordagens: `asyncio` atendendo a rede e delegando tarefas pesadas de CPU para threads/processos separados.

---

## Resumo da Unidade 3

- Servidor **iterativo** atende um cliente por vez; servidor **concorrente** separa "aceitar conexão" de "atender cliente".
- O SO diferencia conexões pela tupla `(IP origem, porta origem, IP destino, porta destino)` — por isso um servidor consegue atender vários clientes na mesma porta.
- **Threads**: uma por cliente, memória compartilhada, cuidado com condições de corrida (`Lock`).
- **`asyncio`**: uma única thread, várias corrotinas alternando via `await`, ótimo para muitas conexões dominadas por I/O.

**Próximo passo**: [`04_representacao_dados_struct.md`](04_representacao_dados_struct.md) — como montar e interpretar campos binários (bits, bytes, `struct`) para construir protocolos de aplicação próprios.
