# 🖥️ SideQuest — Localizador de Computadores na Rede

Este SideQuest implementa um **mecanismo de descoberta, identificação e monitoramento de computadores em uma rede local**, utilizando **Broadcast UDP para descoberta** e **conexões TCP para controle e coleta de informações**.

O objetivo é simular, de forma didática, o funcionamento de sistemas reais de **descoberta de serviços**, **inventário de hosts** e **monitoramento básico de rede**.

---

## 🎯 Objetivo do SideQuest

Permitir que o aluno:

- Utilize **Broadcast UDP** para localizar computadores na rede;
- Desenvolva aplicações **cliente/servidor**;
- Trabalhe com **múltiplos clientes simultaneamente**;
- Utilize **threads** para comunicação concorrente;
- Implemente um **protocolo simples de aplicação**;
- Realize **controle remoto via TCP**;
- Colete informações do cliente (ex.: MAC address).

---

## 🧠 Conceitos de Redes Abordados

- Sockets UDP e TCP
- Broadcast em redes locais
- Descoberta de serviços (Service Discovery)
- Comunicação cliente/servidor
- Threads e concorrência
- Identificação de hosts (IP + Porta)
- Monitoramento por keepalive
- Protocolo de aplicação simples

---

## 🧩 Arquitetura do Sistema

O sistema é composto por dois programas:

### 🔵 Cliente
- Envia **broadcast UDP periódico** anunciando sua presença;
- Informa ao servidor a **porta TCP** onde aceita conexões;
- Mantém um **servidor TCP interno**;
- Responde comandos enviados pelo servidor (ex.: solicitação de MAC).

### 🔴 Servidor (Controlador)
- Escuta broadcasts UDP;
- Mantém uma **lista de clientes descobertos**;
- Identifica clientes pelo par **IP / Porta TCP**;
- Possui um **menu interativo** para controle;
- Conecta-se aos clientes via **TCP** para coletar informações.

---

## 🔁 Fluxo de Funcionamento

### 1️⃣ Descoberta (UDP Broadcast)
O cliente envia periodicamente:

```
DISCOVER_REQUEST;PORT=36222
```

O servidor registra:
```
IP do cliente + Porta TCP
```

---

### 2️⃣ Controle e Consulta (TCP)

Quando solicitado no menu, o servidor:
1. Abre uma conexão TCP com o cliente;
2. Envia o comando:
   ```
   GET_MAC
   ```
3. O cliente responde:
   ```
   MAC_ADDRESS;aa:bb:cc:dd:ee:ff
   ```

---

## 📋 Menu do Servidor

O servidor possui um menu interativo utilizando `match-case`:

```
=== MENU SERVIDOR ===
1 - Listar clientes
2 - Solicitar MAC de um cliente (TCP)
3 - Solicitar MAC de todos clientes (TCP)
0 - Sair
```

---

## 📁 Estrutura da Pasta

```
LocalizadorComputadores/
├── cliente.py
├── servidor.py
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- Sistema operacional com suporte a sockets (Linux, Windows, macOS)

Nenhuma biblioteca externa é necessária.

---

### Execução

#### 1️⃣ Inicie o servidor
```bash
python3 servidor.py
```

#### 2️⃣ Em uma ou mais máquinas (ou terminais), inicie os clientes
```bash
python3 cliente.py
```

É possível executar **vários clientes na mesma máquina**, pois cada um utiliza uma porta TCP diferente.

---

## 🧪 Exemplo de Saída

### Servidor
```
[Novo cliente] 192.168.0.10:34567
[MAC recebido via TCP] 192.168.0.10:34567 => d4:a2:cd:75:ed:dd
```

### Cliente
```
[Broadcast enviado] DISCOVER_REQUEST;PORT=34567
[TCP] Conexão recebida do servidor
[MAC enviado via TCP] d4:a2:cd:75:ed:dd
```

---

## ⚠️ Observações Importantes

- O MAC address **não pode ser obtido remotamente** sem cooperação do cliente;
- Por isso, o próprio cliente coleta e envia seu MAC via TCP;
- O Broadcast funciona apenas em **redes locais**;
- Firewalls podem bloquear UDP ou TCP, dependendo da configuração.

---

## 💡 Sugestões de Extensão (Desafios)

- Enviar hostname e sistema operacional do cliente;
- Implementar timeout e remoção automática de clientes inativos;
- Utilizar mensagens em formato JSON;
- Adicionar autenticação simples;
- Criar uma interface gráfica para o servidor;
- Integrar criptografia nas conexões TCP.

---

## 📚 Aplicação Didática

Este SideQuest pode ser utilizado para:

- Demonstrações em sala de aula;
- Atividades práticas orientadas;
- Projetos avaliativos;
- Base para sistemas de monitoramento;
- Discussão sobre protocolos de aplicação e descoberta de serviços.

---

**SideQuest desenvolvido para fins educacionais no contexto da disciplina de Redes de Computadores. 🚀**
