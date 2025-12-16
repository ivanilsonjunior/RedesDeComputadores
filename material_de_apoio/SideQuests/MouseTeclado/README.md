# 🖱️⌨️ SideQuest — MouseTeclado (Automação de Input + Eventos)

Esta pasta reúne exemplos de **automação e captura de eventos de teclado/mouse** em Python, com foco didático para a disciplina de **Redes de Computadores** (SideQuest).  
A ideia é mostrar como aplicações podem **capturar eventos**, **interpretar ações** e **controlar interfaces**, preparando terreno para sidequests de **controle remoto** (via TCP/UDP) e **sistemas distribuídos**.

> ✅ **Importante (Linux):** em ambientes **Wayland**, a automação “global” (mover mouse e injetar teclas no sistema) costuma ser **bloqueada** por segurança. Muitos exemplos aqui funcionam **plenamente em Xorg/X11**.  
> Você pode checar sua sessão com:
>
> ```bash
> echo $XDG_SESSION_TYPE
> ```
>
> - `x11` → tende a funcionar
> - `wayland` → pode bloquear injeção de eventos (mouse/teclado)

---

## 🎯 Objetivos de Aprendizagem

Ao concluir estes exemplos, o aluno deve ser capaz de:

- Capturar eventos de teclado e mouse (press/release/motion/click).
- Interpretar eventos como comandos (ex.: **WASD**).
- Controlar o mouse e/ou teclado por software (automação).
- Implementar **limiares (threshold)** e **cooldown** para evitar “spam” de eventos.
- Entender as **restrições do SO** (Wayland vs Xorg), permissões e limitações de segurança.
- Preparar o caminho para automação **remota** (via sockets) em sidequests posteriores.

---

## 🧠 Conceitos Abordados

- *Event listeners* (callbacks)
- Threads/loops de evento (dependendo do exemplo)
- Controle de fluxo por eventos (event-driven)
- Debounce e detecção de double click
- Threshold (zona morta) e rate limiting (cooldown)
- Integração com GUI (Pygame) vs automação global (pynput)

---

## 📦 Dependências

A maior parte dos exemplos utiliza a biblioteca **pynput**:

```bash
pip install pynput
```

Para exemplos com janela gráfica, usa-se **Pygame**:

```bash
pip install pygame
```

> Em algumas distribuições Linux, o suporte do `pynput` em X11 pode depender de pacotes do sistema (ex.: `python3-xlib` em Debian/Ubuntu).

---

## 📁 Estrutura Esperada da Pasta

> (Os nomes exatos dos scripts podem variar conforme sua organização.)

Normalmente você verá algo como:

- Exemplos `pynput` (teclado ↔ mouse)
- Exemplos com janela `pygame`
- Scripts auxiliares / testes mínimos

---

## 🧪 Exemplos (visão geral)

A seguir, os exemplos típicos desta pasta e o que cada um demonstra.  
Use-os como base para **desafios incrementalmente mais difíceis**.

### 1) Teclado (WASD) → Move o Mouse (pynput)
**Ideia:** o aluno pressiona `W/A/S/D` e o mouse se move na tela.

**Conceitos:**
- Listener de teclado
- Atualização de posição do mouse
- Passo fixo (STEP)

**Pontos de atenção:**
- Em **Wayland**, mover mouse global pode não funcionar.
- Em X11 funciona melhor (às vezes requer permissões / sessão Xorg).

**Extensões sugeridas:**
- Aceleração (segurar tecla aumenta velocidade)
- Movimento diagonal (W+D etc.)
- Limites de tela / “teleporte” nas bordas

---

### 2) Mouse (double right click) → Toggle CapsLock (pynput)
**Ideia:** detectar **duplo clique** do botão direito e alternar CapsLock.

**Conceitos:**
- Listener do mouse (click press)
- Detecção de double-click (tempo entre cliques)
- Emissão de tecla `caps_lock`

**Limitação importante:**
- Injetar CapsLock no **Wayland** pode falhar (bloqueio de automação global).
- Em X11 tende a funcionar.

**Extensões sugeridas:**
- Triple click → Enter
- Scroll → seta ↑/↓
- Gesto (mouse rápido pra esquerda) → Ctrl+Z

---

### 3) Movimento do Mouse → “Gera” WASD automaticamente (duas versões)
Há **duas formas didáticas** de fazer isso:

#### 3.1) Versão “global” (pynput emite teclas reais)
**Ideia:** ao mover mouse para cima/baixo/esquerda/direita, o programa injeta `w/s/a/d` no sistema (para controlar outra aplicação).

- **Vantagem:** controla qualquer software (jogo, editor, etc.)
- **Desvantagem:** em **Wayland** normalmente não injeta teclas.

#### 3.2) Versão “interna” (Pygame interpreta WASD dentro da janela)
**Ideia:** o mouse se move e o programa “interpreta” WASD apenas para mover um personagem na janela do Pygame — sem digitar nada no sistema.

- **Vantagem:** funciona bem em Wayland, pois tudo acontece dentro da janela.
- **Desvantagem:** não controla aplicativos externos.

---

## 🎮 Exemplo com Pygame: Mouse → WASD (personagem na tela)

### Como funciona (modelo mental)
1. O Pygame dispara eventos `MOUSEMOTION` quando o mouse se move.
2. O programa calcula deslocamento:
   - `dx = mx - last_mx`
   - `dy = my - last_my`
3. Se `dx`/`dy` passar de um **threshold**, decide a direção:
   - Se |dy| > |dx| → vertical (W/S)
   - Senão → horizontal (A/D)
4. Move o personagem e atualiza HUD.

### Parâmetros importantes
- `THRESHOLD`: evita ruído (tremidinha do mouse).
- `PLAYER_SPEED`: controla a velocidade do personagem.
- FPS (clock tick): deixa o movimento estável.

### Extensões sugeridas (bem ricas para aula)
- Diagonais (W+D, W+A…)
- “Zona morta” circular (deadzone)
- Velocidade proporcional a |dx|/|dy|
- Obstáculos e colisões
- Objetivo: “capture o alvo” (minigame)

---

## 🛠️ Troubleshooting (Linux)

### 1) Wayland bloqueando automação global
Se você quer **mover mouse global** ou **injetar teclas globais** e não funciona:

```bash
echo $XDG_SESSION_TYPE
```

Se retornar `wayland`, a solução mais simples para aula é **usar Xorg** (sessão “GNOME on Xorg”, “Ubuntu on Xorg”, etc.).

### 2) Script não responde a eventos
- Rode pelo terminal para ver logs/prints.
- Garanta que a janela/terminal tenha foco (dependendo do listener).
- Confira se a distro bloqueia captura global.

### 3) Firewall / permissões
Alguns ambientes restringem injeção de eventos por segurança.  
Quando necessário para testes locais, rode como administrador **somente em ambiente controlado/lab**.

---

## ✅ Propostas de Atividade (para você usar direto)

### Atividade A — “Mouse como joystick”
1. Ajustar THRESHOLD e PLAYER_SPEED até ficar controlável.
2. Implementar diagonais.
3. Criar “alvo” que aparece aleatoriamente e pontuação por colisão.

### Atividade B — “Teclas como controle de mouse”
1. WASD move mouse; SHIFT aumenta STEP.
2. Espaço = clique esquerdo; Enter = clique direito.
3. Escrever um relatório curto explicando limitações Wayland/Xorg.

### Atividade C — “Automação remota”
1. Cliente capta eventos locais.
2. Envia comandos (W/A/S/D, click, etc.) via TCP para um servidor.
3. Servidor reexecuta comandos (em ambiente permitido) ou simula em Pygame.

---

## 📚 Referências e Leitura Complementar

- Documentação do Pygame (event loop, input)
- Documentação do pynput (keyboard/mouse listeners)
- Conceitos de segurança do Wayland vs X11 (por que automação global é restrita)

---

## ⚠️ Aviso de Uso Responsável

Automação de mouse/teclado pode ser usada para fins indevidos.  
Este material é **educacional**, para laboratórios e estudos controlados, e deve respeitar políticas institucionais e regras do ambiente.

---

**Bons estudos e boas SideQuests! 🚀**
