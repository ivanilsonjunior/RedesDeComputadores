from pynput import mouse, keyboard
import time

# Controlador do teclado
kb = keyboard.Controller()

# Controle de tempo para detectar double-click
last_right_click_time = 0
DOUBLE_CLICK_INTERVAL = 0.3  # segundos

# Estado lógico do CapsLock
caps_on = False

# Referências globais dos listeners
mouse_listener = None
keyboard_listener = None


def toggle_capslock():
    kb.press(keyboard.Key.caps_lock)
    kb.release(keyboard.Key.caps_lock)


def on_click(x, y, button, pressed):
    global last_right_click_time, caps_on

    if button == mouse.Button.right and pressed:
        current_time = time.time()

        # Detecta duplo clique
        if (current_time - last_right_click_time) <= DOUBLE_CLICK_INTERVAL:
            caps_on = not caps_on
            toggle_capslock()
            print(">>> CapsLock ativado" if caps_on else ">>> CapsLock desativado")

        last_right_click_time = current_time


def on_press(key):
    global mouse_listener, keyboard_listener

    if key == keyboard.Key.esc:
        print("\nEncerrando programa...")

        mouse_listener.stop()
        keyboard_listener.stop()

        return False


mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

print("Programa iniciado.")
print("Dê duplo clique com o botão direito para alternar o CapsLock.")
print("Pressione ESC para sair.")

mouse_listener.join()
keyboard_listener.join()
