# 03 — Camada de Aplicação

Este diretório contém exemplos de protocolos da camada de aplicação, implementados de forma didática usando **Python 3** e sockets quando necessário.

## Exemplos Disponíveis

### HTTP
- `http_client_python3.py`  
  Demonstra como enviar uma requisição HTTP manualmente via socket.

### DNS
- `dns_client_python3.py`  
  Monta um pacote DNS simples e envia para um resolvedor.

### SMTP
- `smtp_enviar_python3.py`  
  Demonstra o fluxo básico do protocolo SMTP.

## Objetivo didático
Mostrar como a camada de aplicação **não depende da estrutura física** — apenas da camada de transporte — e como protocolos de alto nível são construídos.

## Como executar
```bash
python3 nome_do_arquivo.py
```
