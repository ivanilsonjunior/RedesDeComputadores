# Sockets/UDP — Jogo de Adivinhação
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

## 📂 `Basico/`

Um jogo simples de adivinhação de número, usado para mostrar que UDP **não é** "sem resposta" por natureza — a aplicação é livre para implementar seu próprio ciclo de pergunta/resposta sobre um transporte sem conexão.

### Protocolo (definido pela própria aplicação, não pelo UDP)

1. O servidor sorteia um número inteiro entre 0 e 10000.
2. O cliente envia um palpite (texto de um número inteiro).
3. O servidor responde com uma destas mensagens:
   - `"maior"` — o número sorteado é maior que o palpite.
   - `"menor"` — o número sorteado é menor que o palpite.
   - `"acertou!"` — o cliente acertou; o servidor encerra.

### Como executar

```bash
# Terminal 1
python3 Basico/Servidor.py

# Terminal 2
python3 Basico/Cliente.py
```

### Para refletir

- O que acontece se um pacote de palpite se perder no caminho? E se a resposta do servidor se perder?
- Como isso se compara ao [`udp_echo_client_python3.py`](../../../../../04_camadas_transporte/udp_echo_client_python3.py) do módulo 04, que já trata timeout explicitamente?

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
