# 04 — Camada de Transporte
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

A Camada de Transporte é responsável por oferecer comunicação fim a fim entre processos, acima da camada de rede.
Nesta camada encontramos dois protocolos fundamentais:

- **TCP (Transmission Control Protocol)** — orientado à conexão, confiável.
- **UDP (User Datagram Protocol)** — sem conexão, sem garantia de entrega.

Este módulo reúne dois níveis de material:

1. Uma **trilha de programação de sockets** em 4 unidades (seções 01–04 abaixo), adaptada do curso *Programação para Redes (NCT)*, cobrindo desde "o que é um socket" até a construção de protocolos binários próprios com `struct`.
2. **Exemplos prontos** de servidor/cliente ECHO em C e Python, para quem quer só rodar e observar o comportamento de TCP/UDP na prática.

--------------------------------------------------------------------

## OBJETIVOS DE APRENDIZAGEM

Ao final deste módulo, o estudante será capaz de:
- Explicar as funções da Camada de Transporte no modelo TCP/IP e por que existe o "problema do encontro".
- Diferenciar TCP e UDP (confiabilidade, conexão, fluxo x datagrama).
- Criar sockets TCP e UDP em Python usando a API completa (`socket`, `bind`, `listen`, `accept`, `connect`, `send`/`recv`, `sendto`/`recvfrom`).
- Implementar servidores **concorrentes** (atendendo vários clientes ao mesmo tempo) com **threads** e com **`asyncio`**.
- Construir e interpretar campos binários de um protocolo próprio usando operadores bit a bit e o módulo `struct`.
- Testar scripts usando ferramentas como `nc` e `telnet`, e analisar o tráfego gerado com Wireshark.

--------------------------------------------------------------------

## TRILHA DE PROGRAMAÇÃO DE SOCKETS (comece por aqui se nunca programou com sockets)

| # | Arquivo | Conteúdo |
|---|---|---|
| 1 | [`01_introducao_sockets.md`](01_introducao_sockets.md) | Comunicação entre processos, modelo cliente/servidor, o "problema do encontro", endereços/portas, comparação TCP x UDP, tipos de socket. |
| 2 | [`02_api_sockets.md`](02_api_sockets.md) | `socket()`, ciclo de vida completo de servidor e cliente TCP (`bind`/`listen`/`accept` e `connect`), envio/recebimento (`send`/`sendall`/`recv`), comunicação UDP (`sendto`/`recvfrom`). |
| 3 | [`03_servidores_concorrentes.md`](03_servidores_concorrentes.md) | Servidor iterativo x concorrente, como o SO diferencia conexões (tupla IP+porta), concorrência com **threads** (e `Lock`) e com **`asyncio`**. |
| 4 | [`04_representacao_dados_struct.md`](04_representacao_dados_struct.md) | Bits, operadores bit a bit e flags, `bytes`/`bytearray`, codificação de texto (`encode`/`decode`), `int.to_bytes`/`from_bytes` e ordem de bytes, `struct.pack`/`unpack` para montar protocolos binários próprios. |

Cada unidade termina com um "próximo passo" apontando para a seguinte — leia em ordem na primeira vez.

--------------------------------------------------------------------

## ARQUIVOS DO MÓDULO

### Exemplos básicos (echo) — Python e C

1. `tcp_echo_server_python3.py` / `tcp_echo_client_python3.py` — par TCP ECHO (conexão, confiabilidade, fluxo).
2. `udp_echo_server_python3.py` / `udp_echo_client_python3.py` — par UDP ECHO (sem conexão, sem garantia de entrega).
3. `tcp_echo_server.c` / `tcp_echo_client.c` e `udp_echo_server.c` / `udp_echo_client.c` — os mesmos exemplos em C, mostrando a mesma API BSD Sockets por trás do módulo `socket` do Python.

### Scripts avançados (Unidades 3 e 4)

4. [`servidor_concorrente_threads.py`](servidor_concorrente_threads.py) — servidor TCP que atende vários clientes ao mesmo tempo, uma thread por cliente, com um contador compartilhado protegido por `Lock`.
5. [`servidor_concorrente_asyncio.py`](servidor_concorrente_asyncio.py) — a mesma ideia, mas com `asyncio` (uma única thread, uma `Task` por cliente).
6. [`protocolo_binario_struct.py`](protocolo_binario_struct.py) — cliente/servidor com um **protocolo de aplicação próprio**: cabeçalho binário fixo (`struct`), flags bit a bit e payload de tamanho variável.

--------------------------------------------------------------------

## BREVE TEORIA

TCP:
- Protocolo orientado à conexão.
- Realiza handshake (3-way).
- Garante entrega, ordem e fluxo.
- Usado em HTTP, HTTPS, SSH, SMTP, FTP.

UDP:
- Protocolo sem conexão (connectionless).
- Não garante entrega.
- Menos sobrecarga, mais rápido.
- Usado em DNS, VoIP, streaming, jogos.

Para a teoria completa (com exemplos de código para cada conceito), ver a trilha [`01_introducao_sockets.md`](01_introducao_sockets.md) → [`04_representacao_dados_struct.md`](04_representacao_dados_struct.md) acima.

--------------------------------------------------------------------

## DIAGRAMA RESUMIDO

TCP (conexão):

```
Cliente              Servidor
   | ---- SYN -----> |
   | <--- SYN/ACK -- |
   | ---- ACK -----> |  (conexão estabelecida)
```

UDP (sem conexão):

```
Cliente ---- DATAGRAMA ----> Servidor
(não há handshake)
```

--------------------------------------------------------------------

## EXERCÍCIOS RECOMENDADOS

Exercícios básicos de TCP/UDP (echo, Wireshark, comparação de desempenho): ver [`04_camadas_transporte_exercicios.md`](04_camadas_transporte_exercicios.md).

Exercícios de API completa, concorrência (threads/`asyncio`) e protocolos binários com `struct`: ver [`exercicios_avancados.md`](exercicios_avancados.md).

Resumo do que cada lista cobre:

1. Modificar o cliente TCP para enviar arquivos, medir tempo de resposta, usar múltiplas conexões simultâneas.
2. Modificar o servidor TCP para tratar vários clientes com threads, registrar mensagens em arquivo.
3. Modificar o cliente UDP para enviar pacotes numerados e calcular taxa de perda.
4. Usar o Wireshark para capturar handshake TCP, retransmissões TCP, pacotes UDP sem resposta.
5. Implementar um protocolo binário próprio com `struct`, incluindo flags e cabeçalho de tamanho fixo.
6. Comparar um servidor concorrente com threads e com `asyncio` sob carga.

--------------------------------------------------------------------

## NOTAS PARA PROFESSORES

- Demonstrações com nc enriquecem as aulas:
    ```
    $ nc -lvp 5000
    $ nc 127.0.0.1 5000
    ```

- Ideal para práticas em laboratório com alunos em duplas: um fica como servidor, outro como cliente.

- Integra-se perfeitamente com o módulo de aplicação (HTTP, DNS, SMTP), pois esses protocolos usam TCP ou UDP por baixo — o parsing manual de DNS em [`../03_camadas_aplicacao/dns_client_python3.py`](../03_camadas_aplicacao/dns_client_python3.py) é um ótimo contraponto prático para a Unidade 4 (representação de dados/`struct`) deste módulo.

- A trilha de 4 unidades é densa (equivale a várias aulas). Sugestão de distribuição: Unidade 1 e 2 numa semana (teoria + `tcp_echo_*`/`udp_echo_*`), Unidade 3 na semana seguinte (`servidor_concorrente_*`), Unidade 4 por último (`protocolo_binario_struct.py`), fechando com os exercícios avançados como avaliação prática.

--------------------------------------------------------------------

## MATERIAL COMPLEMENTAR

Para exemplos de sockets TCP/UDP mais elaborados (sistema cliente-servidor com autodescoberta, servidor HTTP artesanal, jogo em UDP, classificador de imagens via TCP), ver:
```
../material_de_apoio/Camadas/Transporte/Sockets/
```

--------------------------------------------------------------------

DIATINF — IFRN
Material educacional para cursos de Redes de Computadores e ADS.
