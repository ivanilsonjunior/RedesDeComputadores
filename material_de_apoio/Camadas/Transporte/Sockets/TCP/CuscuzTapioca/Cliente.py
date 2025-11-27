import socket

def enviar_imagem(entrada, host="127.0.0.1", port=5000):
    """
    Envia ao servidor uma URL ou caminho local de imagem
    e imprime a resposta recebida.
    """

    try:
        # Cria o socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            print(f"Conectando ao servidor {host}:{port}...")
            cliente.connect((host, port))

            # Envia a entrada (URL ou caminho)
            cliente.sendall(entrada.encode())

            # Aguarda a resposta do servidor
            resposta = cliente.recv(4096).decode()

            print("🟦 Resposta do servidor:")
            print(resposta)

    except ConnectionRefusedError:
        print("❌ Erro: não foi possível conectar ao servidor. "
              "Verifique se ele está rodando.")
    except Exception as e:
        print("❌ Erro no cliente:", e)


# Modo interativo
if __name__ == "__main__":
    print("=== Cliente de Classificação (Tapioca vs Cuscuz) ===")
    while True:
        entrada = input("\nDigite uma URL ou caminho de arquivo (ou 'sair'): ").strip()

        if entrada.lower() in ("sair", "exit", "quit"):
            break

        enviar_imagem(entrada)
