# Exercícios Avançados — API de Sockets, Concorrência e Protocolos Binários
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Estes exercícios cobrem as Unidades 1–4 (ver [`01_introducao_sockets.md`](01_introducao_sockets.md) a [`04_representacao_dados_struct.md`](04_representacao_dados_struct.md)) e os scripts [`servidor_concorrente_threads.py`](servidor_concorrente_threads.py), [`servidor_concorrente_asyncio.py`](servidor_concorrente_asyncio.py) e [`protocolo_binario_struct.py`](protocolo_binario_struct.py). Para os exercícios de TCP/UDP básico (echo), veja [`04_camadas_transporte_exercicios.md`](04_camadas_transporte_exercicios.md).

---

## 1. Problema do encontro e endereçamento

**1.1** — Explique, com suas palavras, por que é o **servidor** que precisa iniciar sua execução primeiro no modelo cliente/servidor, e não o cliente. O que aconteceria se um cliente tentasse `connect()` antes do servidor executar `bind()` + `listen()`?

**1.2** — Rode `tcp_echo_server_python3.py` e, em outro terminal, tente iniciar uma segunda instância do mesmo servidor (mesma porta). Explique o erro obtido e relacione-o com o conceito de tupla de conexão.

**1.3** — Usando `netstat` (Windows) ou `ss -tan` (Linux), identifique as portas efêmeras usadas por dois clientes distintos conectados ao mesmo `tcp_echo_server_python3.py` ao mesmo tempo.

---

## 2. `accept()` e sockets por cliente

**2.1** — Modifique `tcp_echo_server_python3.py` para imprimir o valor de `cliente.fileno()` (o descritor do socket) toda vez que `accept()` retornar. Abra três clientes ao mesmo tempo e observe que cada um recebe um descritor diferente — mesmo que todos usem a mesma porta do servidor.

**2.2** — No servidor original (iterativo), explique por que o segundo cliente só é atendido depois que o primeiro se desconecta. Aponte exatamente a linha de código responsável por esse comportamento.

**2.3 — TCP não preserva mensagens.** Escreva um cliente que faça:
```python
cliente.sendall(b"ABC")
cliente.sendall(b"DEF")
```
em sequência rápida (sem esperar resposta entre os dois `sendall`). No servidor, imprima cada `recv(1024)` recebido. Documente o que aconteceu: os dois `sendall()` do cliente viraram exatamente dois `recv()` no servidor? Explique por que isso não é garantido (ver `02_api_sockets.md`, seção 5.6).

---

## 3. Servidor concorrente com threads

**3.1** — Rode [`servidor_concorrente_threads.py`](servidor_concorrente_threads.py) e conecte 3 clientes simultâneos usando [`tcp_echo_client_python3.py`](tcp_echo_client_python3.py) (adaptando-o, se necessário, para não travar aguardando `input()` — ou use `nc localhost 5000` em cada terminal). Envie mensagens de terminais diferentes intercaladas e confirme que nenhum cliente precisa esperar o outro terminar.

**3.2** — Remova o `Lock` do `contador_clientes` em `servidor_concorrente_threads.py` (ou simule a condição de corrida somando 1000 vezes em vez de uma). Explique por que, sem `Lock`, o contador pode acabar com um valor diferente do número real de clientes atendidos.

**3.3** — Adicione uma nova funcionalidade compartilhada entre threads: uma lista `clientes_conectados` que armazena o endereço de cada cliente ativo, removendo-o quando ele desconecta. Proteja essa lista com um `Lock` próprio. Implemente um comando especial (`"/quem"`) que, quando recebido de um cliente, faz o servidor responder com a lista de todos os clientes atualmente conectados.

---

## 4. Servidor concorrente com `asyncio`

**4.1** — Rode [`servidor_concorrente_asyncio.py`](servidor_concorrente_asyncio.py) e repita o teste do exercício 3.1. Compare o uso de CPU/memória (via `Gerenciador de Tarefas` ou `htop`) entre a versão com threads e a versão com `asyncio`, conectando 20+ clientes simultâneos em cada uma (pode usar um pequeno script para abrir várias conexões de uma vez).

**4.2** — No `servidor_concorrente_asyncio.py`, insira deliberadamente uma chamada bloqueante e pesada dentro de `atender_cliente()` (ex.: `import time; time.sleep(5)` sem `await`, simulando um cálculo lento). Conecte dois clientes e observe: o segundo cliente consegue ser atendido enquanto o primeiro "calcula"? Explique o resultado relacionando com a seção 6.4 de `03_servidores_concorrentes.md` (event loop bloqueado).

**4.3** — Reescreva o exercício 4.2 usando `await asyncio.sleep(5)` em vez de `time.sleep(5)`. O comportamento muda? Por quê?

---

## 5. Bits, bytes e codificação

**5.1** — Sem executar, calcule à mão o valor de `f"{0b10110101:02x}"` e `f"{0xA7:08b}"`. Depois confirme no interpretador Python.

**5.2** — Escreva uma função `mostrar_flags(valor, nomes)` que recebe um inteiro e uma lista de nomes de flags (na ordem dos bits 0, 1, 2...) e imprime quais estão ativas. Por exemplo, `mostrar_flags(0b0101, ["ACK", "ERRO", "URGENTE", "RESPOSTA"])` deve indicar que `ACK` e `URGENTE` estão ativas.

**5.3** — Explique por que `len("café")` pode ser diferente de `len("café".encode("utf-8"))`. Calcule os dois valores e identifique qual caractere é responsável pela diferença.

**5.4** — Um campo de protocolo hipotético usa 6 bits para "tipo" e 10 bits para "código", totalizando 16 bits (2 bytes). Escreva as funções `construir_campo(tipo, codigo)` e `extrair_campo(valor)` usando deslocamento (`<<`, `>>`) e máscaras (`&`), análogas ao exemplo de `TIPO`/`CÓDIGO` de 4+4 bits em `04_representacao_dados_struct.md` (seção 2.14–2.15).

---

## 6. `struct` e o protocolo binário próprio

**6.1** — Rode [`protocolo_binario_struct.py`](protocolo_binario_struct.py) como servidor em um terminal e como cliente em outro. Envie a mesma mensagem três vezes: sem flags, só com `MAIUSCULO`, e com `MAIUSCULO + INVERTER` combinadas. Confirme que o resultado corresponde ao esperado pela combinação de flags.

**6.2** — Use `struct.calcsize(FORMATO_CABECALHO)` para confirmar que o cabeçalho tem exatamente 6 bytes. Depois, capture o tráfego com Wireshark (filtro `tcp.port == 5050`) enquanto o cliente envia uma mensagem, e identifique manualmente, nos bytes brutos do payload TCP, onde termina o cabeçalho e onde começa o texto.

**6.3** — Adicione uma terceira flag `REPETIR = 1 << 2` ao protocolo: quando ativada, o servidor deve responder com o texto processado repetido duas vezes (ex.: `"IFRN"` vira `"IFRNIFRN"`). Atualize `processar()`, e no cliente, adicione a pergunta correspondente.

**6.4** — Adicione ao cabeçalho um novo campo `timestamp` de 4 bytes (inteiro sem sinal, segundos desde 1970 — use `int(time.time())`), alterando `FORMATO_CABECALHO` para `"!BBHHI"`. Ajuste `empacotar()` e `receber_mensagem()`. No servidor, imprima a diferença entre o `timestamp` recebido e o horário atual (uma estimativa simples de latência).

**6.5 — Desafio.** Combine os três scripts: implemente uma versão de `protocolo_binario_struct.py` cujo **servidor** seja concorrente (baseado em threads **ou** `asyncio`, à sua escolha), capaz de atender múltiplos clientes simultaneamente enviando mensagens no protocolo binário. Use como base tanto `servidor_concorrente_threads.py`/`servidor_concorrente_asyncio.py` (para a concorrência) quanto `protocolo_binario_struct.py` (para o framing com `struct`).

---

## 7. Comparando com um protocolo real

**7.1** — Releia [`../03_camadas_aplicacao/dns_client_python3.py`](../03_camadas_aplicacao/dns_client_python3.py). Identifique, no código, a linha equivalente a `struct.calcsize()` desta unidade (mesmo que o script não use o módulo `struct` diretamente, ele calcula tamanhos e desloca posições manualmente). Reescreva a função `parsear_resposta()` daquele script utilizando `struct.unpack()` em vez de slicing manual sempre que possível, e compare a legibilidade das duas versões.

**7.2** — O cabeçalho DNS tem 12 bytes, formados por 6 campos de 16 bits (`"!HHHHHH"`). Verifique isso com `struct.calcsize("!HHHHHH")` e explique a relação com a seção 6.26–6.27 de `04_representacao_dados_struct.md`.

---

DIATINF — IFRN
Material educacional para Redes de Computadores e ADS.
