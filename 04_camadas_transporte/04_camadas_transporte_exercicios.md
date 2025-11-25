# Exercícios — Camada de Transporte (TCP e UDP)
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Este arquivo contém exercícios práticos e teóricos para reforçar o entendimento
da Camada de Transporte, especialmente os protocolos TCP e UDP, utilizando
os scripts deste módulo.

------------------------------------------------------------
1. Exercícios sobre TCP
------------------------------------------------------------

1.1 — Handshake TCP
Explique o processo de handshake (SYN, SYN/ACK, ACK) e capture no Wireshark
uma conexão TCP aberta entre seu cliente e servidor.

Tarefas:
- Identificar a porta de origem e destino.
- Identificar o número de sequência inicial.
- Explicar o porquê do ACK complementar.

------------------------------------------------------------

1.2 — Modificar o Servidor TCP
Modifique o arquivo tcp_echo_server_python3.py para:
a) Registrar cada mensagem recebida em um arquivo de log.
b) Incluir a data e a hora no registro.
c) Aceitar até 10 clientes simultâneos usando threads.

------------------------------------------------------------

1.3 — Modificar o Cliente TCP
Modifique o arquivo tcp_echo_client_python3.py para:
a) Aceitar um parâmetro de linha de comando contendo o IP do servidor.
b) Enviar 10 mensagens automaticamente, numeradas.
c) Medir o RTT médio (Round Trip Time).

Dica: use time.time().

------------------------------------------------------------

1.4 — Comparação prática
Explique por que TCP é considerado:
- Confiável
- Orientado à conexão
- Ordenado
- Baseado em fluxo contínuo

Use capturas do Wireshark para ilustrar exemplos.

------------------------------------------------------------
2. Exercícios sobre UDP
------------------------------------------------------------

2.1 — Perda de pacotes
Utilize udp_echo_client_python3.py e modifique para enviar 100 pacotes numerados,
capturando quantos são recebidos de volta.

Perguntas:
- Qual a taxa de perda?
- Todos chegaram na mesma ordem?

------------------------------------------------------------

2.2 — Tempo de resposta
Modifique o cliente UDP para medir o tempo entre envio e recebimento (quando houver).

Explique:
- Por que não há garantia de entrega?
- Por que o UDP costuma ser mais rápido?

------------------------------------------------------------

2.3 — Modificação no servidor UDP
Adapte o servidor UDP para:
a) Inserir um atraso artificial (ex.: time.sleep(0.5)).
b) Registrar o endereço de cada cliente.
c) Rejeitar pacotes maiores que 256 bytes.

------------------------------------------------------------
3. Comparação TCP vs UDP
------------------------------------------------------------

3.1 — Tabela de comparação
Preencha uma tabela com:
- Confiabilidade
- Ordem
- Overhead
- Velocidade
- Casos de uso

------------------------------------------------------------

3.2 — Aplicações reais
Pesquise e liste 5 aplicações reais que usam UDP e 5 que usam TCP.

Explique por que cada aplicação escolheu esse protocolo.

------------------------------------------------------------
4. Integração com outras camadas
------------------------------------------------------------

4.1 — Relacionando com Aplicação
Escolha um protocolo da camada de aplicação (HTTP, DNS ou SMTP).
Explique como ele utiliza TCP ou UDP e por quê.

------------------------------------------------------------

4.2 — Relacionando com a Camada de Rede
Capture em Wireshark:
- Segmentos TCP encapsulados em pacotes IP
- Datagramas UDP encapsulados em pacotes IP

Explique a diferença entre:
- Fragmentação
- MTU
- Overhead

------------------------------------------------------------
5. Desafio Final (para nota extra)
------------------------------------------------------------

5.1 — Chat TCP em Python
Crie um mini chat usando sockets TCP com:
- Múltiplos clientes
- Threads
- Nome de usuário
- Mensagens broadcast

5.2 — Jogo simples com UDP
Implemente:
- Cliente envia posição X,Y
- Servidor devolve confirmação
- Jogadores simulados movem-se rapidamente

Mostre na prática a diferença entre atraso e perda.

------------------------------------------------------------

DIATINF — IFRN
Material para prática de Redes de Computadores e ADS.
