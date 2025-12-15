# Jogo Pygame que usa o movimento do mouse para controlar um boneco
# e envia comandos reais de teclado (WASD) para o sistema operacional usando pynput
# Requer as bibliotecas pygame e pynput
# Instale com: pip install pygame pynput
import pygame
import sys
from pynput.keyboard import Controller as KeyController
from pynput.keyboard import Key

# Inicializa o Pygame
pygame.init()

# ---------------------------
# 1. CONFIGURAÇÃO DA JANELA
# ---------------------------

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse → WASD (Pygame + pynput)")

clock = pygame.time.Clock()

# ---------------------------
# 2. BONECO
# ---------------------------

player_pos = [WIDTH // 2, HEIGHT // 2]
PLAYER_SIZE = 40
PLAYER_SPEED = 5

# ---------------------------
# 3. MOUSE
# ---------------------------

last_mouse_pos = pygame.mouse.get_pos()
THRESHOLD = 10  # deslocamento mínimo

# ---------------------------
# 4. TEXTO
# ---------------------------

font = pygame.font.SysFont(None, 32)
last_command = ""

# ---------------------------
# 5. CONTROLADOR DO TECLADO (pynput)
# ---------------------------

kb = KeyController()

def emit_key(char):
    """
    Usa pynput para emitir teclas reais para o sistema operacional.
    """
    kb.press(char)
    kb.release(char)
    print(f"[pynput] Tecla enviada: {char}")


# ---------------------------
# 6. MOVIMENTO DO PERSONAGEM
# ---------------------------

def move_player_and_emit(command):
    """
    Move o boneco no Pygame E envia o comando WASD real pelo pynput.
    """
    global player_pos, last_command

    # Movimento no Pygame
    if command == 'w':
        player_pos[1] -= PLAYER_SPEED
    elif command == 's':
        player_pos[1] += PLAYER_SPEED
    elif command == 'a':
        player_pos[0] -= PLAYER_SPEED
    elif command == 'd':
        player_pos[0] += PLAYER_SPEED

    # Mantém dentro da tela
    player_pos[0] = max(0, min(WIDTH - PLAYER_SIZE, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - PLAYER_SIZE, player_pos[1]))

    # Atualiza HUD
    last_command = command.upper()

    # Emite o comando via pynput
    emit_key(command)


# ---------------------------
# 7. LOOP PRINCIPAL
# ---------------------------

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detecta movimento do mouse
        if event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
            dx = mx - last_mouse_pos[0]
            dy = my - last_mouse_pos[1]

            if abs(dx) >= THRESHOLD or abs(dy) >= THRESHOLD:

                # Movimento vertical predominante
                if abs(dy) > abs(dx):
                    if dy < 0:
                        move_player_and_emit('w')
                    else:
                        move_player_and_emit('s')

                # Movimento horizontal predominante
                else:
                    if dx < 0:
                        move_player_and_emit('a')
                    else:
                        move_player_and_emit('d')

                last_mouse_pos = (mx, my)

    # ---------------------------
    # Desenho da cena
    # ---------------------------

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (200, 200, 50),
                     (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    info_text = f"Último comando (WASD): {last_command or '-'}"
    text_surface = font.render(info_text, True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))

    help_text = "Mova o mouse dentro da janela para mover o boneco e enviar WASD real."
    help_surface = font.render(help_text, True, (200, 200, 200))
    screen.blit(help_surface, (20, HEIGHT - 40))

    pygame.display.flip()

pygame.quit()
sys.exit()
