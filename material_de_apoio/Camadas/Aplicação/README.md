# Aplicação — Servidor de Comandos Remoto
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

## `Remoto.py`

Um servidor de comandos simples que escuta broadcast UDP na porta `5555` e reage a mensagens de texto.

### Comandos aceitos

| Comando | Efeito |
|---|---|
| `pagina` | Abre uma URL fixa no Google Chrome (caminho do executável hardcoded para Windows — ajuste `chrome_path` se necessário). |
| `whoru` | Responde `Estou aqui` para quem perguntou. |
| `quit 123` | Encerra o servidor, apenas se a senha `123` for informada. |

### Como executar

```bash
python3 Remoto.py
```

### Como testar (enviando comandos)

Não há um cliente dedicado nesta pasta — qualquer emissor de broadcast UDP na porta 5555 serve. Um teste rápido em Python:

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(b"whoru", ("255.255.255.255", 5555))
print(s.recvfrom(1024))
```

Ou reaproveite [`06_componentes_fisicos/broadcast_demo.py`](../../../06_componentes_fisicos/broadcast_demo.py) como base, trocando a porta para `5555` e a mensagem para um dos comandos acima.

### ⚠️ Nota de segurança (proposital)

Este servidor **não tem autenticação real**: a "senha" do comando `quit` é uma string fixa (`"123"`) embutida no código-fonte e enviada em texto puro pela rede — qualquer um que capture o tráfego (ex.: com Wireshark) descobre a senha. Isso é intencional como gancho de discussão: por que uma senha fixa em texto puro é insegura? O que mudaria com um hash, um desafio-resposta, ou um canal cifrado? Ver [`material_de_apoio/SideQuests/Segurança/Criptografia/`](../../SideQuests/Segurança/Criptografia/) para os mecanismos que resolveriam esse problema.

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
