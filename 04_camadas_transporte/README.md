
# 04 — Camada de Transporte

Este diretório contém exemplos de código didático relacionados à **Camada de Transporte** do modelo TCP/IP, com implementações em **Python 3** e **C**, demonstrando os dois principais protocolos desta camada:

- **TCP** – Orientado à conexão, confiável, garante entrega e ordem.
- **UDP** – Não orientado à conexão, sem garantia de entrega ou ordem.

Os exemplos foram desenvolvidos para fins educacionais nas disciplinas da **DIATINF/IFRN**, atendendo aos cursos:

- CST em Redes de Computadores  
- CST em Análise e Desenvolvimento de Sistemas  

---

## 📘 Objetivos Didáticos

- Demonstrar o estabelecimento e encerramento de conexões TCP.
- Explicar como funcionam portas, multiplexação e fluxo de dados.
- Evidenciar diferenças práticas entre TCP e UDP.
- Permitir que estudantes explorem falhas, latência, pacote perdido, etc.

---

## 📂 Arquivos Disponíveis

### 🟦 **TCP – Transmission Control Protocol**

| Arquivo | Descrição |
|--------|-----------|
| `tcp_echo_server_python3.py` | Servidor TCP que recebe mensagens e devolve (ECO). |
| `tcp_echo_client_python3.py` | Cliente TCP que envia mensagens ao servidor. |
| `tcp_echo_server.c` | Servidor TCP em C (POSIX). |
| `tcp_echo_client.c` | Cliente TCP em C (POSIX). |

---

### 🟧 **UDP – User Datagram Protocol**

| Arquivo | Descrição |
|--------|-----------|
| `udp_echo_server_python3.py` | Servidor UDP que recebe datagramas e devolve. |
| `udp_echo_client_python3.py` | Cliente UDP para testar envio/recebimento. |

---

## ▶ Como Executar os Exemplos

### 🐍 **Python 3**

Execute qualquer script assim:

```bash
python3 nome_do_arquivo.py
```

---

### 🧰 **C (Linux)**

Compile:

```bash
gcc arquivo.c -o programa
```

Execute:

```bash
./programa
```

---

## 🧪 Exercícios Recomendados

### 🔹 Experimentos com TCP
1. Adicione suporte a múltiplos clientes usando threads.
2. Meça o RTT (round-trip time) de cada mensagem.
3. Implemente um mini-chat com broadcast.
4. Adicione logs com timestamp em cada mensagem.
5. Modifique o cliente para enviar mensagens automáticas a cada 2 segundos.

### 🔹 Experimentos com UDP
1. Envie 100 pacotes e calcule taxa de perda.
2. Varie o tamanho dos pacotes para observar fragmentação.
3. Adicione simulação de perda artificial (dropar 30% dos pacotes).
4. Meça latência aproximada (UDP “ping”).
5. Crie um modo “flood” para testar sobrecarga.

---

## 📚 Relacionamento com o Modelo TCP/IP

A camada de transporte é responsável por:

- **Multiplexação/demultiplexação** (uso de portas)
- **Segmentação e reagrupamento**
- **Garantia de confiabilidade (TCP)**
- **Comunicação sem conexão (UDP)**

Este diretório fornece exemplos práticos desses conceitos.

---

## 👨‍🏫 Autor / DIATINF–IFRN

Material desenvolvido para fins educacionais nos cursos da DIATINF/IFRN.  
Sinta-se livre para reutilizar e adaptar em sala de aula.

