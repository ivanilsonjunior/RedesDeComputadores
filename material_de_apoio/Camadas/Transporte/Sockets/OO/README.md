# Sockets/OO — Sistema Cliente-Servidor com Autodescoberta
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Um sistema mais completo, escrito em estilo orientado a objetos, que combina três ideias:

1. Um servidor TCP que executa comandos remotos.
2. Um mecanismo de **descoberta de serviço**: o servidor se anuncia periodicamente via broadcast UDP, para que clientes o encontrem sem saber seu IP de antemão.
3. Um cliente "rogue" (`Hacker.py`) que demonstra por que esse desenho, sem autenticação, é perigoso.

---

## 📂 Arquivos

| Arquivo | Papel |
|---|---|
| `Sistema.py` | Interpreta os comandos de texto (`/help`, `/mem`, `/hd`, `/google`, `/ip`) e executa a ação correspondente. Não é executado diretamente. |
| `Servidor.py` | Servidor TCP: aceita conexões, repassa o texto recebido para `Sistema.comando()` e devolve a resposta. Em paralelo (thread daemon), anuncia seu `(IP, porta)` via broadcast UDP a cada 60s. |
| `Cliente.py` | Cliente TCP interativo simples — pede o comando ao usuário e já sabe o IP/porta do servidor (`127.0.0.1:8888`, ajuste se necessário). |
| `ClienteTurbo.py` | Cliente "inteligente": fica escutando os anúncios de broadcast do servidor e monta uma lista dos servidores encontrados na rede, sem precisar saber o IP de antemão. |
| `Hacker.py` | **Demonstração de exploração**: escuta os mesmos anúncios de broadcast e, assim que descobre um servidor, conecta-se por TCP e envia `/google` — sem fornecer qualquer credencial. |

### Comandos aceitos pelo servidor (via `Sistema.comando`)

| Comando | Efeito |
|---|---|
| `/help` | Lista os comandos disponíveis. |
| `/mem` | Retorna uso de memória (`psutil.virtual_memory()`). |
| `/hd` | Retorna uso de disco (`psutil.disk_usage`). |
| `/google` | Abre uma URL fixa no navegador **da máquina que roda o servidor**. |
| `/ip <ip1> <ip2> <mascara>` | Verifica se dois IPs estão na mesma rede, dada uma máscara em bits (ex.: `/ip 192.168.1.10 192.168.1.20 24`). |

---

## ▶️ Como executar

Terminal 1 — inicia o servidor (aceita comandos e anuncia-se por broadcast):
```bash
python3 Servidor.py
```

Terminal 2 — cliente manual, já sabendo o endereço:
```bash
python3 Cliente.py
```

Terminal 3 — cliente que descobre o servidor sozinho:
```bash
python3 ClienteTurbo.py
```

Terminal 4 — demonstração de exploração (não precisa saber IP nem senha):
```bash
python3 Hacker.py
```

---

## ⚠️ Por que `Hacker.py` funciona sem senha

`Servidor.py` aceita **qualquer** conexão TCP e executa **qualquer** comando reconhecido por `Sistema.comando()` — inclusive `/google`, que abre um navegador na máquina do servidor — sem checar quem está do outro lado. Combinado com o anúncio automático por broadcast (qualquer um na mesma LAN descobre o servidor), isso é, na prática, um caso de **execução remota de comando (RCE) sem autenticação**.

Use isso como material de discussão:
- O que impediria `Hacker.py` de funcionar? (autenticação, lista de IPs permitidos, TLS + certificado, etc.)
- Como isso se relaciona com os mecanismos estudados em [`material_de_apoio/SideQuests/Segurança/Criptografia/`](../../../../SideQuests/Segurança/Criptografia/) (assinatura, HMAC, handshake autenticado)?

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
