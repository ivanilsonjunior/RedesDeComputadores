
# Exercícios — Camada de Aplicação (HTTP, DNS, SMTP)

Este arquivo contém exercícios práticos e teóricos para consolidar o aprendizado dos protocolos da Camada de Aplicação.

---

# 📘 1. Exercícios sobre HTTP

## 1.1 — Requisição HTTP Manual
Use o script `http_client_python3.py` para enviar requisições HTTP para três sites diferentes:
- www.ifrn.edu.br
- www.google.com
- www.wikipedia.org

**Tarefas:**
- Identifique os códigos de resposta (200, 301, 404, etc.).
- Compare o tamanho dos cabeçalhos.
- Verifique se há redirecionamento.

---

## 1.2 — Modificar o Cliente HTTP
Altere o script para:
- Permitir que o usuário digite o caminho (ex.: `/index.html`)
- Exibir apenas os cabeçalhos HTTP
- Salvar o corpo da resposta em um arquivo `.html`

---

## 1.3 — Identificar Componentes do HTTP
Dado o cabeçalho:

```
HTTP/1.1 200 OK
Server: Apache
Content-Type: text/html
Content-Length: 1024
```

Explique:
- A função de cada linha.
- O significado do código **200 OK**.

---

# 📘 2. Exercícios sobre DNS

## 2.1 — Consultar Diferentes Domínios
Use o script `dns_client_python3.py` para consultar:

- ifrn.edu.br  
- google.com  
- github.com  

**Tarefas:**
- Compare o tamanho das respostas.
- Analise a resposta bruta em hexadecimal.
- Verifique quantos bytes são usados no cabeçalho.

---

## 2.2 — Consulta AAAA (IPv6)
Modifique o script para consultar registros **AAAA**.

Dicas:
- Mude o tipo (QTYPE) de `0x0001` (A) para `0x001c` (AAAA).

---

## 2.3 — Testando Perda ou Latência
Execute 20 consultas para o mesmo domínio e:
- Conte quantas falham
- Meça o tempo médio de resposta (use `time.time()`)

---

# 📘 3. Exercícios sobre SMTP

## 3.1 — Aumentar o Corpo do E-mail
Modifique `smtp_enviar_python3.py` para permitir:
- Corpo do e-mail em múltiplas linhas
- Entrada do usuário para assunto

---

## 3.2 — Mostrar o Fluxo SMTP
Ative o modo debug:

```python
servidor.set_debuglevel(1)
```

Analise:
- HELO
- MAIL FROM
- RCPT TO
- DATA
- QUIT

---

## 3.3 — Comparar com Captura no Wireshark
Capture o tráfego SMTP e explique:
- Quais comandos aparecem
- Como o servidor responde
- Diferença entre texto simples e TLS

---

# 📘 4. Exercícios integrados (HTTP + DNS)

## 4.1 — Resolver DNS e Fazer HTTP
Escreva um programa que:
1. Consulta o DNS para obter o IP de um site
2. Usa o IP para fazer a requisição HTTP

---

# 📘 5. Exercícios de Análise

## 5.1 — Com base nos logs:
Explique por que DNS usa UDP ao invés de TCP.

## 5.2 — Segurança:
Liste 3 ataques comuns que acontecem na camada de aplicação:
- Spoofing
- DNS poisoning
- SQL Injection (conceitual, camada superior)

---

Material de apoio — DIATINF/IFRN
