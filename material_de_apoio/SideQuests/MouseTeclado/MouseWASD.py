# -*- coding: utf-8 -*-
"""
Simula a digitação das teclas W, A, S, D com base no movimento do mouse.
Pressione ESC para encerrar.
"""

from pynput import mouse, keyboard
import time

# Controladores
kb = keyboard.Controller()
mouse_ctrl = mouse.Controller()

# Configuração
THRESHOLD = 20       # deslocamento mínimo para gerar tecla
COOLDOWN = 0.15      # tempo mínimo entre emissões da mesma tecla
last_emit = time.time()

# Posição anterior do mouse
last_pos = mouse_ctrl.position

# Listeners globais
mouse_listener = None
keyboard_listener = None


def emit_key(key_char):
    kb.press(key_char)
    kb.release(key_char)
    print(f"Tecla emitida: {key_char}")


def check_movement():
    global last_pos, last_emit

    current_pos = mouse_ctrl.position
    dx = current_pos[0] - last_pos[0]
    dy = current_pos[1] - last_pos[1]

    now = time.time()

    # Evita spam exagerado
    if now - last_emit < COOLDOWN:
        last_pos = current_pos
        return

    # Eixo vertical (W / S)
    if abs(dy) > abs(dx):
        if dy < -THRESHOLD:
            emit_key('w')
            last_emit = now
        elif dy > THRESHOLD:
            emit_key('s')
            last_emit = now

    # Eixo horizontal (A / D)
    else:
        if dx < -THRESHOLD:
            emit_key('a')
            last_emit = now
        elif dx > THRESHOLD:
            emit_key('d')
            last_emit = now

    last_pos = current_pos


def on_move(x, y):
    check_movement()


def on_press(key):
    global mouse_listener, keyboard_listener

    if key == keyboard.Key.esc:
        print("\nEncerrando programa...")
        mouse_listener.stop()
        keyboard_listener.stop()
        return False


mouse_listener = mouse.Listener(on_move=on_move)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

print("Movimente o mouse para gerar WASD automaticamente.")
print("Pressione ESC para sair.")

mouse_listener.join()
keyboard_listener.join()
