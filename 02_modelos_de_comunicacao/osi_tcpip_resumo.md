
# Comparação: Modelo OSI vs Modelo TCP/IP

## 📌 Modelo OSI (7 camadas)

1. Aplicação  
2. Apresentação  
3. Sessão  
4. Transporte  
5. Rede  
6. Enlace  
7. Física  

Criado pela ISO.  
É um **modelo teórico**, amplamente utilizado para fins de estudo.

---

## 📌 Modelo TCP/IP (4 camadas)

1. Aplicação  
2. Transporte  
3. Rede  
4. Acesso à Rede (Enlace + Física combinadas)  

Criado pelo Departamento de Defesa dos EUA (DoD).  
É o **modelo prático e real** usado na Internet.

---

# 📌 Principais Diferenças

| Modelo OSI | Modelo TCP/IP |
|------------|----------------|
| 7 camadas | 4 camadas |
| Modelo teórico | Modelo prático |
| Camadas separadas para apresentação/sessão | Funções incorporadas na camada de aplicação |
| Estrutura detalhada | Estrutura simplificada |
| Didático | Operacional |

---

# 📌 Correspondência entre as camadas

```
OSI:    Aplicação – Apresentação – Sessão – Transporte – Rede – Enlace – Física
TCP/IP:                Aplicação            – Transporte – Rede – Acesso
```

---

# 📌 Encapsulamento (Visão Geral)

```
Aplicação → Transporte → Rede → Enlace → Física
```

Exemplo real:
```
HTTP → TCP → IP → Ethernet → Sinal elétrico/radiofrequência
```

---

# 🧭 Resumo Visual (ASCII)

```
+-------------------------------+
|   Modelos de Comunicação      |
+-------------------------------+
        /                   OSI (7 camadas)     TCP/IP (4 camadas)
```

---

Material de apoio — DIATINF/IFRN
