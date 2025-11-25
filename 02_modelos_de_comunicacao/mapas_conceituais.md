
# Mapas Conceituais — OSI e TCP/IP

Este arquivo apresenta mapas conceituais em formato ASCII para facilitar o estudo dos modelos OSI e TCP/IP.

---

# 📌 Modelo OSI (7 camadas)

```
+-------------------+
|   7. Aplicação    |
+-------------------+
| 6. Apresentação   |
+-------------------+
|    5. Sessão      |
+-------------------+
|   4. Transporte   |
+-------------------+
|     3. Rede       |
+-------------------+
|    2. Enlace      |
+-------------------+
|    1. Física      |
+-------------------+
```

Funções principais:
- Aplicação: Serviços ao usuário (HTTP, DNS, SMTP)
- Apresentação: Formatação, criptografia
- Sessão: Gerenciamento de sessões
- Transporte: TCP/UDP
- Rede: IP, ICMP, roteamento
- Enlace: Ethernet, Wi-Fi
- Física: Sinais, cabos, rádio

---

# 📌 Modelo TCP/IP (4 camadas)

```
+------------------------+
|     Aplicação          |
+------------------------+
|      Transporte        |
+------------------------+
|         Rede           |
+------------------------+
|    Acesso à Rede       |
+------------------------+
```

Funções principais:
- Aplicação: Protocolos de alto nível (HTTP, FTP, DNS)
- Transporte: TCP/UDP
- Rede: IP, ICMP
- Acesso à Rede: Ethernet, Wi-Fi, drivers

---

# 📌 Comparação lado a lado

```
    OSI (7)                    TCP/IP (4)
----------------------------------------------
 Aplicação                Apresentação             +--> Aplicação
 Sessão                   /
----------------------------------------------
 Transporte              ---> Transporte
----------------------------------------------
 Rede                    ---> Rede
----------------------------------------------
 Enlace                   Física                  +--> Acesso à Rede
```

---

# 📌 Encapsulamento (Fluxo Geral)

```
Aplicação
   ↓
Transporte
   ↓
Rede
   ↓
Enlace
   ↓
Física
```

Exemplo real:
```
HTTP → TCP → IP → Ethernet → Sinal (cabo ou rádio)
```

---

# 📌 Desencapsulamento (Máquina de Destino)

```
Sinal
  ↓
Enlace
  ↓
Rede
  ↓
Transporte
  ↓
Aplicação
```

---

# Material de apoio — DIATINF/IFRN

Este arquivo serve como referência visual rápida para revisões e estudos acelerados.
