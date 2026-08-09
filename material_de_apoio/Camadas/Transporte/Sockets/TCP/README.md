# Sockets/TCP — Exemplos com Socket Stream
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Quatro variações de servidor/cliente TCP, da mais simples à mais elaborada.

---

## 📂 `Simples/`

O par cliente/servidor TCP mais mínimo possível: o cliente conecta, envia **uma** mensagem, recebe **uma** resposta fixa, e ambos encerram. Sem laços, sem múltiplos comandos — ideal como primeiro contato com `connect()`/`accept()`/`send()`/`recv()`.

```bash
# Terminal 1
python3 Simples/Servidor.py

# Terminal 2
python3 Simples/Cliente.py
```

> `Cliente.py` conecta em `127.0.0.1` por padrão — troque a variável `servidor` pelo IP correto se for testar entre duas máquinas.

---

## 📂 `Basico/`

Um servidor de "comandos remotos" mais completo (mas sem orientação a objetos e sem threads — atende um cliente por vez): `/help`, `/mem` (memória), `/hd` (disco), `/google` (abre navegador na máquina do servidor). Comparar com a versão orientada a objetos em [`../OO/`](../OO/), que faz a mesma coisa de forma mais estruturada e com descoberta automática via broadcast.

```bash
# Terminal 1
python3 Basico/Servidor.py

# Terminal 2
python3 Basico/Cliente.py
```

---

## 📂 `ServidorWeb/`

Um servidor HTTP **artesanal**: aceita a conexão TCP, lê a requisição bruta (sem parsear método/cabeçalhos) e sempre devolve a mesma página HTML fixa com um cabeçalho `HTTP/1.1 200 OK` escrito manualmente. É o par perfeito do lado servidor para o [`03_camadas_aplicacao/http_client_python3.py`](../../../../../03_camadas_aplicacao/http_client_python3.py) (que faz a mesma coisa do lado cliente) — ou pode ser testado direto de um navegador.

```bash
python3 ServidorWeb/Servidor.py
# depois abra http://127.0.0.1:8080 no navegador,
# ou rode o cliente HTTP manual do módulo 03
```

---

## 📂 `CuscuzTapioca/`

Um servidor TCP que recebe uma URL ou caminho de imagem, classifica com um modelo de rede neural já treinado (`Nordestino.keras`, via TensorFlow/Keras) se a imagem é "tapioca" ou "cuscuz", e devolve o resultado com as probabilidades.

> ⚠️ **Fora do padrão dos demais exemplos**: depende de bibliotecas pesadas (`tensorflow`, `numpy`, `Pillow`, `requests`) e de um modelo binário já treinado incluído na pasta. Instale as dependências antes de rodar:
> ```bash
> pip install -r CuscuzTapioca/requirements.txt
> ```

```bash
# Terminal 1
python3 CuscuzTapioca/Servidor.py

# Terminal 2
python3 CuscuzTapioca/Cliente.py
```

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
