import socket
import urllib.request
import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models


# ============================================================
# 1. Carrega e pré-processa a imagem no tamanho correto (180x180)
# ============================================================
def load_image(img_path):
    """
    Carrega e pré-processa a imagem no formato esperado pelo modelo.
    - Redimensiona para 180x180 (CORRETO PARA ESTE MODELO)
    - Converte para array
    - Normaliza para [0,1]
    - Expande dimensão para formar lote (batch)
    """
    img = image.load_img(img_path, target_size=(180, 180))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# ============================================================
# 2. Classificação da imagem
# ============================================================
def classificar_imagem(caminho):
    """
    Faz a predição usando modelo.keras.
    Retorna 'cuscuz' ou 'tapioca'.
    """
    model = models.load_model("Nordestino.keras")
    img = load_image(caminho)

    pred = model.predict(img)[0][0]

    if pred >= 0.5:
        return "cuscuz"
    else:
        return "tapioca"


# ============================================================
# 3. Download da imagem
# ============================================================
def baixar_imagem(url, destino="entrada.jpg"):
    try:
        urllib.request.urlretrieve(url, destino)
        return destino
    except Exception as e:
        print("Erro ao baixar imagem:", e)
        return None


# ============================================================
# 4. Junta download + classificação
# ============================================================
def processar_url(url):
    caminho = baixar_imagem(url)

    if caminho is None:
        return "ERRO: não foi possível baixar a imagem."

    try:
        resultado = classificar_imagem(caminho)
        return resultado
    except Exception as e:
        print("Erro ao classificar a imagem:", e)
        return "ERRO: falha ao classificar a imagem."
    finally:
        if os.path.exists(caminho):
            os.remove(caminho)


# ============================================================
# 5. Servidor TCP
# ============================================================
def iniciar_servidor():
    HOST = "0.0.0.0"
    PORT = 5000

    print(f"Servidor TCP iniciado em {HOST}:{PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen()

        while True:
            print("\nAguardando conexão...")
            cliente, endereco = servidor.accept()
            print(f"Conexão recebida de {endereco}")

            with cliente:
                url = cliente.recv(4096).decode().strip()
                print("URL recebida:", url)

                resposta = processar_url(url)

                cliente.sendall(resposta.encode())


# ============================================================
# 6. Entrada principal
# ============================================================
if __name__ == "__main__":
    iniciar_servidor()
