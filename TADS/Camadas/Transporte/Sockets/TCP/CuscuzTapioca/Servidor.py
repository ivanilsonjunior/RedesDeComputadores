import socket            # Biblioteca para comunicação TCP
import os                # Para checar arquivos locais, se quiser usar caminho de arquivo
from io import BytesIO   # Para manipular bytes em memória (imagem baixada)
import requests          # Para baixar a imagem quando a entrada for uma URL
from PIL import Image    # Para abrir e tratar a imagem
import tensorflow as tf  # TensorFlow para manipulação de tensores e sigmoid
from tensorflow import keras  # Keras para carregar o modelo e converter imagem em array


# ============================================================
# 1. CARREGAR MODELO TREINADO
# ============================================================
# Aqui o modelo é carregado UMA ÚNICA VEZ, na inicialização do servidor.
# Isso evita custo de recarregar o modelo a cada requisição.
# Certifique-se de que o arquivo 'Nordestino.keras' está na mesma pasta.
print("Carregando modelo 'Nordestino.keras'...")
model = keras.models.load_model("Nordestino.keras")
print("Modelo carregado com sucesso!")


# ============================================================
# 2. FUNÇÃO PARA CARREGAR IMAGEM (URL OU ARQUIVO LOCAL)
# ============================================================
def carregar_imagem(caminho_ou_url, image_size=(180, 180)):
    """
    Carrega uma imagem a partir de:
      - uma URL (http/https), ou
      - um caminho de arquivo local.

    Retorna um objeto PIL.Image já convertido para RGB
    e redimensionado para 'image_size', que por padrão é (180, 180)
    pois é o tamanho esperado pelo modelo.
    """

    # Caso seja URL (começa com http)
    if caminho_ou_url.startswith("http://") or caminho_ou_url.startswith("https://"):
        print("Baixando imagem da URL...")
        resp = requests.get(caminho_ou_url)
        resp.raise_for_status()  # Lança exceção se o HTTP não for 200 OK
        img = Image.open(BytesIO(resp.content)).convert("RGB")
    else:
        # Caso contrário, assume que é um arquivo local
        if not os.path.exists(caminho_ou_url):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_ou_url}")
        img = Image.open(caminho_ou_url).convert("RGB")

    # Redimensiona para o tamanho que o modelo espera
    img = img.resize(image_size)

    return img


# ============================================================
# 3. FUNÇÃO DE CLASSIFICAÇÃO
# ============================================================
def classificar_imagem(caminho_ou_url, model, image_size=(180, 180)):
    """
    Recebe uma URL ou caminho de arquivo, prepara a imagem
    e executa a predição no modelo 'model'.

    IMPORTANTE:
    - NÃO fazemos normalização manual (tipo /255) aqui,
      pois o seu modelo já foi treinado com a normalização
      embutida (por exemplo, camadas de Rescaling).
    - Vamos seguir exatamente a lógica que você usou no script original.

    Retorna:
      - classe_str: "tapioca" ou "cuscuz"
      - score_tapioca: probabilidade (entre 0 e 1) de ser tapioca
      - score_cuscuz: probabilidade (entre 0 e 1) de ser cuscuz
    """
    # Carrega a imagem (URL ou arquivo)
    img = carregar_imagem(caminho_ou_url, image_size)

    # Converte a imagem PIL para array numérico (valores 0–255)
    img_array = keras.utils.img_to_array(img)

    # Adiciona dimensão de batch: de (180, 180, 3) para (1, 180, 180, 3)
    img_array = tf.expand_dims(img_array, 0)

    # Predição do modelo: aqui o modelo devolve um logit (sem sigmoid final)
    logits = model.predict(img_array)[0][0]

    # Aplica sigmoid no logit para obter probabilidade entre 0 e 1
    score = float(tf.sigmoid(logits))

    # Interpretação:
    # score = probabilidade de ser Tapioca
    score_tapioca = score
    score_cuscuz = 1.0 - score

    if score > 0.5:
        classe_str = "tapioca"
    else:
        classe_str = "cuscuz"

    # Logs no servidor para depuração
    print("\n🔍 RESULTADO DA CLASSIFICAÇÃO")
    print(f"Logit bruto do modelo: {logits:.4f}")
    print(f"Probabilidade de Tapioca: {100 * score_tapioca:.2f}%")
    print(f"Probabilidade de Cuscuz:  {100 * score_cuscuz:.2f}%")
    print(f"👉 Classe escolhida: {classe_str}")
    print("-" * 50)

    return classe_str, score_tapioca, score_cuscuz


# ============================================================
# 4. FUNÇÃO QUE ATENDE UMA ÚNICA REQUISIÇÃO TCP
# ============================================================
def tratar_conexao(cliente_socket, endereco):
    """
    Função que atende UMA conexão de cliente.

    Protocolo simples:
      1. O cliente envia uma linha de texto contendo a URL
         (ou caminho local da imagem).
      2. O servidor lê essa linha, classifica a imagem.
      3. O servidor devolve uma string com o resultado.

    Exemplo de resposta:
      "tapioca; prob_tapioca=0.8765; prob_cuscuz=0.1235"
    """
    try:
        print(f"\nConexão recebida de {endereco}")

        # Recebe até 4096 bytes (mais que suficiente pra uma URL)
        data = cliente_socket.recv(4096)
        if not data:
            print("Nenhum dado recebido. Encerrando conexão.")
            return

        # Decodifica de bytes para string e remove espaços/quebras de linha
        entrada = data.decode().strip()
        print(f"Entrada recebida do cliente: {entrada}")

        # Executa a classificação usando o mesmo pipeline do seu script
        classe, prob_tap, prob_cus = classificar_imagem(entrada, model)

        # Monta uma string de resposta (pode simplificar para só a classe se quiser)
        resposta = (
            f"{classe}; "
            f"prob_tapioca={prob_tap:.4f}; "
            f"prob_cuscuz={prob_cus:.4f}"
        )

        # Envia a resposta de volta ao cliente
        cliente_socket.sendall(resposta.encode())
        print(f"Resposta enviada para {endereco}: {resposta}")

    except Exception as e:
        # Em caso de erro, retorna mensagem de erro para o cliente
        msg_erro = f"ERRO: {str(e)}"
        print("Erro ao processar requisição:", e)
        try:
            cliente_socket.sendall(msg_erro.encode())
        except Exception:
            pass  # Se nem conseguir enviar erro, só ignora
    finally:
        # Garante que o socket será fechado ao final
        cliente_socket.close()
        print(f"Conexão com {endereco} encerrada.")


# ============================================================
# 5. SERVIDOR TCP PRINCIPAL
# ============================================================
def iniciar_servidor_tcp(host="0.0.0.0", port=5000):
    """
    Inicia um servidor TCP que fica escutando conexões.

    Para cada conexão:
      - Lê uma URL/caminho enviada pelo cliente
      - Classifica a imagem como tapioca ou cuscuz
      - Retorna o resultado pelo próprio socket

    Uso típico:
      iniciar_servidor_tcp("0.0.0.0", 5000)
    """
    print(f"Servidor TCP iniciando em {host}:{port}...")

    # Cria o socket TCP (IPv4, orientado a conexão)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # Permite reusar rapidamente a porta após reiniciar o servidor
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Associa o socket ao endereço/porta
        servidor.bind((host, port))

        # Coloca o socket em modo de escuta
        servidor.listen()
        print(f"Servidor escutando em {host}:{port} (CTRL+C para parar).")

        # Loop infinito de atendimento
        while True:
            # Aguarda uma conexão
            cliente_socket, endereco = servidor.accept()

            # Aqui estamos atendendo de forma sequencial (uma conexão por vez).
            # Se quiser multithread, dá pra criar uma thread por conexão.
            tratar_conexao(cliente_socket, endereco)


# ============================================================
# 6. PONTO DE ENTRADA DO SCRIPT
# ============================================================
if __name__ == "__main__":
    # Inicia o servidor TCP.
    # Você pode mudar a porta se quiser (ex: 6000, 8000, etc.).
    iniciar_servidor_tcp(host="0.0.0.0", port=5000)
