# 🔐 Funções Hash Criptográficas

## Disciplina: Redes de Computadores / Internet das Coisas (IoT)

Funções hash criptográficas são usadas para **garantir a integridade dos dados**,
verificando se uma informação foi alterada durante armazenamento ou transmissão.

Diferente da criptografia:
- Hash não usa chave
- Hash não é reversível
- Hash não esconde informações

---

## Principais características
- Mesma entrada gera sempre o mesmo hash
- Saída de tamanho fixo
- Pequena alteração gera grande mudança (efeito avalanche)
- Impossível reverter o hash para a mensagem original
- Resistência a colisões

---

## Algoritmos
### ❌ Obsoletos (não usar)
- MD5
- SHA-1

### ✅ Recomendados
- SHA-256
- SHA-512
- SHA-3

Neste material utilizamos **SHA-256**.

---

## Hash × Criptografia

| Hash | Criptografia Simétrica |
|------|------------------------|
| Não usa chave | Usa chave |
| Não reversível | Reversível |
| Integridade | Confidencialidade |

---

## Estrutura dos exemplos
- `basico/` – exemplos introdutórios
- `arquivos/` – verificação de integridade
- `senhas/` – armazenamento seguro
- `hmac/` – integridade + autenticação

---

## Aplicações em Redes e IoT
- Verificação de integridade de mensagens
- Autenticação de dispositivos
- Atualização segura de firmware
- HTTPS, MQTT seguro, TLS
