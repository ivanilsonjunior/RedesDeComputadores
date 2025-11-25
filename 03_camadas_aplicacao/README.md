
# 03 — Camada de Aplicação

A Camada de Aplicação é a camada mais próxima do usuário dentro do modelo TCP/IP.  
É nela que vivem os protocolos usados diariamente, como:

- HTTP (Web)
- DNS (Resolução de nomes)
- SMTP (E-mail)
- HTTPS (Web segura)
- SSH (Acesso remoto)
- FTP/SFTP (Transferência de arquivos)

Este módulo reúne exemplos práticos que demonstram como aplicações reais usam sockets e protocolos para comunicação.

---

# 🎯 Objetivos de Aprendizagem

Ao final deste módulo, o estudante será capaz de:

- Compreender o papel da Camada de Aplicação no modelo TCP/IP.
- Diferenciar protocolo, serviço e aplicação.
- Construir e enviar requisições HTTP (GET).
- Entender a estrutura de uma consulta DNS.
- Enviar mensagens SMTP simples.
- Interpretar capturas no Wireshark.
- Relacionar protocolos da camada de aplicação ao transporte (TCP/UDP).

---

# 📂 Arquivos do Módulo

| Arquivo | Descrição |
|--------|-----------|
| `http_client_python3.py` | Cliente HTTP construído manualmente usando sockets. |
| `dns_client_python3.py` | Cliente DNS via UDP montando o pacote manualmente. |
| `smtp_enviar_python3.py` | Envio didático de e-mail usando SMTP. |
| `conceitos_camadas_aplicacao.md` | Conteúdo teórico sobre a camada de aplicação. |
| `exercicios_camadas_aplicacao.md` | Lista de exercícios e desafios práticos. |

---

# 🧭 Diagrama Geral da Camada de Aplicação

```
Aplicação     ← (onde o usuário interage)
     ↓
Transporte    (TCP ou UDP)
     ↓
Rede          (IP)
     ↓
Enlace
     ↓
Física
```

---

# 🔍 Protocolos e seus Transportes

| Protocolo | Transporte |
|-----------|------------|
| HTTP | TCP |
| HTTPS | TCP |
| DNS | UDP/TCP |
| SMTP | TCP |
| FTP | TCP |
| SSH | TCP |
| DHCP | UDP |

---

# 🧪 Exercícios Recomendados

1. Modifique o cliente HTTP para solicitar páginas diferentes.  
2. Adapte o script DNS para consultas AAAA (IPv6).  
3. Capture com Wireshark o tráfego DNS gerado pelo script.  
4. Analise os cabeçalhos retornados por três sites diferentes.  
5. Crie uma ferramenta que salve a resposta HTTP em um arquivo `.html`.  
6. Modifique o SMTP para permitir corpo de mensagem multi-linha.  

---

# 👨‍🏫 Notas para Professores

- Use Wireshark para relacionar teoria ↔ prática.  
- DNS é excelente para exercícios de engenharia reversa.  
- SMTP ajuda a introduzir segurança posteriormente (TLS).  
- HTTP permite demonstrar conceitos modernos como REST.

---

# DIATINF — IFRN

Material educacional para Redes de Computadores e ADS.
