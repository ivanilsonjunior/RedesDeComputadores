
# Topologias de Rede

As topologias definem como os dispositivos estão organizados fisicamente ou logicamente.

---

## 🔸 Topologia em Estrela

```
      [PC]   [PC]
        \     /
         \   /
         [ SWITCH ]
         /   \\
      [PC]  [PC]
```

**Vantagens:**
- Fácil expansão.
- Fácil identificação de falhas.
- Isolamento de problemas.

**Desvantagens:**
- Dependência do switch (ponto único de falha).

---

## 🔸 Topologia em Barramento

```
PC ─── PC ─── PC ─── PC
```

**Vantagens:**
- Baixo custo.
- Fácil instalação (histórico).

**Desvantagens:**
- Colisões frequentes.
- Pouco utilizada atualmente.
- Dificuldade de expansão.

---

## 🔸 Topologia em Anel

```
[PC] → [PC] → [PC] → [PC] → (volta ao início)
```

**Vantagens:**
- Sem colisões.
- Fluxo ordenado.

**Desvantagens:**
- Falha em um ponto pode parar toda a rede.
- Reparo difícil.

---

## 🔸 Topologia em Malha

```
 Representação abstrata:

      [A]────[B]
       │ \   │ \
       │  \  │  \
      [C]────[D]
```

**Vantagens:**
- Altíssima redundância.
- Alta tolerância a falhas.

**Desvantagens:**
- Alto custo.
- Complexidade de instalação.

---

## 🔸 Topologias Híbridas

Mistura de duas ou mais topologias, por exemplo:

- Estrela + Barramento  
- Malha + Estrela  
- Anel duplo  

Usadas frequentemente em redes corporativas modernas.

---

## Comparação Geral

| Topologia | Uso Atual | Vantagens | Desvantagens |
|----------|-----------|-----------|--------------|
| Estrela | Muito comum | Fácil manutenção | Ponto único de falha |
| Barramento | Pouco usada | Simples, barata | Colisões, difícil expandir |
| Anel | Usada em redes especializadas | Sem colisões | Falha derruba tudo |
| Malha | Usada em backbones | Alta redundância | Custo alto |
| Híbrida | Comum em empresas | Flexível | Complexidade |

---

Material de apoio — DIATINF/IFRN
