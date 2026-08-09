# Transporte / Sockets — Exemplos Avançados
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Exemplos de sockets TCP/UDP mais elaborados que os do módulo [`04_camadas_transporte/`](../../../../04_camadas_transporte/) (que cobre apenas um par cliente/servidor ECHO). Aqui cada subpasta combina o socket com outro problema prático: descoberta de serviço, um mini servidor web, um jogo, um classificador de imagens.

---

## 📂 Organização

| Pasta | Conteúdo |
|---|---|
| [`OO/`](OO/) | Sistema cliente-servidor orientado a objetos, com descoberta automática de servidores via broadcast UDP e execução de comandos remotos por TCP — inclui um script que demonstra a falta de autenticação desse desenho. |
| [`TCP/Basico/`](TCP/Basico/) | Versão não orientada a objetos do mesmo servidor de comandos remotos (info de sistema, abrir navegador). |
| [`TCP/Simples/`](TCP/Simples/) | O exemplo TCP mais mínimo possível: uma mensagem, uma resposta. |
| [`TCP/ServidorWeb/`](TCP/ServidorWeb/) | Servidor HTTP artesanal (sem framework), devolvendo uma página HTML fixa. |
| [`TCP/CuscuzTapioca/`](TCP/CuscuzTapioca/) | Classificador de imagens (tapioca x cuscuz) servido via socket TCP, usando um modelo de rede neural já treinado. |
| [`UDP/Basico/`](UDP/Basico/) | Jogo de adivinhação de número via UDP — ilustra troca de mensagens com resposta, mesmo sem conexão. |

---

## Ordem sugerida de leitura

1. `TCP/Simples/` — o mínimo indispensável de um socket TCP.
2. `UDP/Basico/` — o equivalente em UDP, com resposta a cada mensagem.
3. `TCP/Basico/` — um "servidor de comandos" com múltiplos comandos de texto.
4. `TCP/ServidorWeb/` — a mesma ideia de servidor TCP, mas falando HTTP de verdade.
5. `OO/` — o mesmo servidor de comandos, agora com threads, descoberta automática e (de propósito) sem autenticação.
6. `TCP/CuscuzTapioca/` — um caso de uso "fora da curva", com dependências pesadas (TensorFlow); ver ressalva no README daquela pasta.

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
