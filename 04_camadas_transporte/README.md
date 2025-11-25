# 04 — Camada de Transporte
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

A Camada de Transporte é responsável por oferecer comunicação fim a fim entre processos, acima da camada de rede.  
Nesta camada encontramos dois protocolos fundamentais:

- **TCP (Transmission Control Protocol)** — orientado à conexão, confiável.
- **UDP (User Datagram Protocol)** — sem conexão, sem garantia de entrega.

Este módulo contém exemplos práticos em Python para demonstrar, passo a passo, como esses protocolos funcionam na prática.

--------------------------------------------------------------------

OBJETIVOS DE APRENDIZAGEM

Ao final deste módulo, o estudante será capaz de:
- Explicar as funções da Camada de Transporte no modelo TCP/IP.
- Diferenciar TCP e UDP (confiabilidade, conexão, fluxo).
- Criar sockets TCP e UDP em Python.
- Implementar comunicação cliente/servidor usando TCP.
- Implementar comunicação sem conexão usando UDP.
- Testar scripts usando ferramentas como nc e telnet.
- Analisar o tráfego gerado com Wireshark.

--------------------------------------------------------------------

ARQUIVOS DO MÓDULO

1. tcp_echo_server_python3.py  
   — Servidor TCP ECHO (conexão, confiabilidade, fluxo).

2. tcp_echo_client_python3.py  
   — Cliente TCP compatível com o servidor.

3. udp_echo_server_python3.py  
   — Servidor UDP ECHO (sem conexão, sem garantia de entrega).

4. udp_echo_client_python3.py  
   — Cliente UDP com tratamento de timeout.

--------------------------------------------------------------------

BREVE TEORIA

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

--------------------------------------------------------------------

DIAGRAMA RESUMIDO

TCP (conexão):

Cliente              Servidor
   | ---- SYN -----> |
   | <--- SYN/ACK -- |
   | ---- ACK -----> |  (conexão estabelecida)

UDP (sem conexão):

Cliente ---- DATAGRAMA ----> Servidor
(não há handshake)

--------------------------------------------------------------------

EXERCÍCIOS RECOMENDADOS

1. Modifique o cliente TCP para:
   - enviar arquivos
   - medir tempo de resposta
   - usar múltiplas conexões simultâneas

2. Modifique o servidor TCP para:
   - tratar vários clientes com threads
   - registrar mensagens em arquivo

3. Modifique o cliente UDP para:
   - enviar 100 pacotes e calcular taxa de perda
   - enviar pacotes numerados

4. Use o Wireshark para capturar:
   - handshake TCP
   - retransmissões TCP
   - pacotes UDP sem resposta

5. Compare:
   - tempo de entrega TCP vs UDP
   - comportamento com wi-fi fraco

--------------------------------------------------------------------

NOTAS PARA PROFESSORES

- Demonstrações com nc enriquecem as aulas:
    $ nc -lvp 5000
    $ nc 127.0.0.1 5000

- Ideal para práticas em laboratório com alunos em duplas:
    um fica como servidor, outro como cliente.

- Integra-se perfeitamente com o módulo de aplicação
  (HTTP, DNS, SMTP), pois esses protocolos usam TCP ou UDP por baixo.

--------------------------------------------------------------------

DIATINF — IFRN
Material educacional para cursos de Redes de Computadores e ADS.
