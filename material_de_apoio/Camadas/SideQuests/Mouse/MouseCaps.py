from pynput import mouse, keyboard
import time

# Controlador do teclado
kb = keyboard.Controller()

# Controle de tempo para detectar double-click
last_right_click_time = 0
DOUBLE_CLICK_INTERVAL = 0.3  # segundos

# Estado lógico do CapsLock (não temos uma API para ler o estado real)
caps_on = False

def toggle_capslock():
    """
    Emite um evento de pressionar a tecla CapsLock.
    """
    kb.press(keyboard.Key.caps_lock)
    kb.release(keyboard.Key.caps_lock)

def on_click(x, y, button, pressed):
    global last_right_click_time, caps_on

    if button == mouse.Button.right and pressed:
        current_time = time.time()

        # Verifica se é double click
        if (current_time - last_right_click_time) <= DOUBLE_CLICK_INTERVAL:
            caps_on = not caps_on
            toggle_capslock()
            print(">>> CapsLock ativado" if caps_on else ">>> CapsLock desativado")

        last_right_click_time = current_time


# Listener do mouse
with mouse.Listener(on_click=on_click) as listener:
    print("Programa iniciado. Dê duplo clique com o botão direito para alternar CapsLock.")
    print("Pressione Ctrl+C no terminal para encerrar.")
    listener.join()
