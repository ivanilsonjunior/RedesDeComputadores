# Só funciona em sistemas que suportam a biblioteca pynput
# Instale a biblioteca com: pip install pynput
# Este script permite controlar o mouse usando as teclas W, A, S, D.
# Nos linux mais modernos que utilizam Wayland, o controle do mouse pode não funcionar devido a restrições de segurança.
# No linux, pode ser necessário executar o script com privilégios de superusuário. Seja cauteloso ao fazer isso.
from pynput import keyboard, mouse

# Criamos um controlador do mouse
mouse_controller = mouse.Controller()

# Define o tamanho do passo de movimento (pixels)
STEP = 20

# Mapeamento de teclas -> movimento
MOVES = {
    'w': (0, -STEP),   # cima
    's': (0, STEP),    # baixo
    'a': (-STEP, 0),   # esquerda
    'd': (STEP, 0)     # direita
}

def on_press(key):
    """
    Callback chamado quando uma tecla é pressionada.
    """
    try:
        k = key.char.lower()  # transforma em letra minúscula
        if k in MOVES:
            dx, dy = MOVES[k]
            x, y = mouse_controller.position
            mouse_controller.position = (x + dx, y + dy)
            print(f"Movendo mouse para {(x + dx, y + dy)}")
    except AttributeError:
        # Tecla especial (Shift, Ctrl, etc.) — ignoramos
        pass

def on_release(key):
    """
    Finaliza o programa quando o usuário pressiona ESC.
    """
    if key == keyboard.Key.esc:
        print("Encerrando...")
        return False  # interrompe o listener

# Inicia o listener do teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
