
# 04 — Camada de Transporte

Este diretório contém exemplos de código didático relacionados à **Camada de Transporte** do modelo TCP/IP, implementados em **Python 3** e **C (POSIX)**.

Ele demonstra o funcionamento prático dos dois principais protocolos dessa camada:

- **TCP** – orientado à conexão, confiável, com controle de fluxo.  
- **UDP** – não orientado à conexão, sem garantias de entrega ou ordem.  

Todos os scripts foram preparados com foco no ensino para os cursos:

- CST em Redes de Computadores (RC)  
- CST em Análise e Desenvolvimento de Sistemas (ADS)  

---

## 📘 Objetivos Didáticos

- Entender o funcionamento da camada de transporte.
- Visualizar como portas identificam serviços.
- Diferenciar TCP e UDP através de código real.
- Compreender conexões, fluxo, pacotes e mensagens.
- Proporcionar um laboratório simples para experimentação.

---

## 📂 Arquivos Disponíveis

### 🟦 TCP (Transmission Control Protocol)

| Arquivo | Linguagem | Descrição |
|--------|-----------|-----------|
| `tcp_echo_server_python3.py` | Python 3 | Servidor TCP de echo, altamente comentado. |
| `tcp_echo_client_python3.py` | Python 3 | Cliente TCP para testes. |
| `tcp_echo_server.c` | C (POSIX) | Servidor TCP em baixo nível. |
| `tcp_echo_client.c` | C (POSIX) | Cliente TCP compatível com o servidor acima. |

---

### 🟧 UDP (User Datagram Protocol)

| Arquivo | Linguagem | Descrição |
|--------|-----------|-----------|
| `udp_echo_server_python3.py` | Python 3 | Servidor UDP que devolve datagramas. |
| `udp_echo_client_python3.py` | Python 3 | Cliente UDP simples. |

---

## ▶ Como Executar

### 🐍 Python 3

```bash
python3 nome_do_arquivo.py
```

### 🧰 C (Linux)

Compilar:

```bash
gcc arquivo.c -o programa
```

Executar:

```bash
./programa
```

---

## 🧪 Exercícios Recomendados

### 🔹 TCP
1. Adicione suporte a múltiplos clientes usando threads.  
2. Faça o cliente medir o RTT de cada mensagem enviada.  
3. Crie um mini-chat com broadcast.  
4. Modifique o servidor para registrar todas as mensagens em um arquivo.  
5. Faça o servidor limitar o tamanho das mensagens (controle de aplicação).

---

### 🔹 UDP
1. Envie 100 pacotes e calcule quantos retornam (taxa de perda).  
2. Varie o tamanho dos pacotes para observar fragmentação.  
3. Adicione uma “perda artificial” de 20%.  
4. Faça o cliente medir RTT simulando um UDP ping.  
5. Crie um modo “stress test”: enviar o máximo possível por 5 segundos.

---

## 👨‍🏫 Observações Didáticas

- TCP é ótimo para comparar com UDP — sempre que possível, use os dois scripts juntos.
- Execute vários clientes TCP ao mesmo tempo para mostrar multiplexação.
- Alterar portas, TTL, e delays é ótimo para experimentação.
- O aluno aprende MUITO ao modificar esse código.

---

## DIATINF – IFRN

Material de apoio educacional para as disciplinas de Redes.
Sinta-se à vontade para adaptar, melhorar e ampliar.
