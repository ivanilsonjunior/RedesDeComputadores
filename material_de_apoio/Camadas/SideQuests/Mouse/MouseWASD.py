# -*- coding: utf-8 -*-
"""
Simula a digitação das teclas W, A, S, D com base no movimento do mouse.
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

def emit_key(key_char):
    """
    Emite uma tecla como se fosse digitada.
    """
    kb.press(key_char)
    kb.release(key_char)
    print(f"Tecla emitida: {key_char}")

def check_movement():
    """
    Compara a posição atual com a anterior e decide se emite W, A, S ou D.
    """
    global last_pos, last_emit

    current_pos = mouse_ctrl.position
    dx = current_pos[0] - last_pos[0]
    dy = current_pos[1] - last_pos[1]

    now = time.time()

    # Evita spam exagerado
    if now - last_emit < COOLDOWN:
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
    """
    Callback acionado ao mover o mouse.
    """
    check_movement()


with mouse.Listener(on_move=on_move) as listener:
    print("Movimente o mouse para gerar WASD automaticamente.")
    print("Pressione Ctrl+C no terminal para sair.")
    listener.join()