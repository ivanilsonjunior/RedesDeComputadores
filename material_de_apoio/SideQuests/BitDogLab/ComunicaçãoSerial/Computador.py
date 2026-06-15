"""
Codigo para rodar no computador.

Objetivo:
    Abrir uma conexao serial com a BitDogLab e oferecer um menu para controlar
    o LED RGB da placa.

Requisitos no computador:
    pip install pyserial

Importante:
    Antes de executar este arquivo, envie o arquivo BitDog.py para a BitDogLab
    e deixe a placa conectada ao computador pela USB.
"""

import time

import serial
from serial.tools import list_ports


# Velocidade da comunicacao serial. A BitDogLab pela USB costuma trabalhar bem
# com 115200 bps, que tambem e um valor muito usado em exemplos de MicroPython.
BAUD_RATE = 115200

# Tempo maximo, em segundos, que o computador espera por uma resposta da serial.
TIMEOUT = 1


def listar_portas():
    """
    Mostra as portas seriais detectadas no computador.

    Exemplos comuns:
        Windows: COM3, COM4, COM5...
        Linux:   /dev/ttyACM0, /dev/ttyUSB0...
        macOS:   /dev/tty.usbmodem...
    """
    portas = list(list_ports.comports())

    if not portas:
        print("Nenhuma porta serial encontrada automaticamente.")
        print("Confira se a BitDogLab esta conectada pela USB.")
        return portas

    print("Portas seriais encontradas:")
    for indice, porta in enumerate(portas, start=1):
        print("  {}. {} - {}".format(indice, porta.device, porta.description))

    return portas


def escolher_porta(portas):
    """
    Permite escolher a porta pelo numero da lista ou pelo nome completo.

    Exemplo:
        Se o programa mostrou:
            33. /dev/ttyACM0 - Board in FS mode - Board CDC

        O usuario pode digitar:
            33

        ou:
            /dev/ttyACM0
    """
    escolha = input("\nDigite o numero da lista ou o nome da porta serial: ").strip()

    if escolha.isdigit():
        indice = int(escolha)

        if 1 <= indice <= len(portas):
            porta_escolhida = portas[indice - 1].device
            print("Porta escolhida:", porta_escolhida)
            return porta_escolhida

        print("Numero invalido. Digite um numero entre 1 e {}.".format(len(portas)))
        return None

    return escolha


def abrir_serial():
    """
    Pede ao usuario a porta serial e abre a conexao com a BitDogLab.

    O nome da porta depende do sistema operacional. Por isso, o programa lista
    as portas encontradas, mas deixa o usuario digitar a porta correta.
    """
    portas = listar_portas()
    porta = escolher_porta(portas)

    if porta is None:
        return None

    conexao = serial.Serial(porta, BAUD_RATE, timeout=TIMEOUT)

    # Quando a serial e aberta, algumas placas reiniciam automaticamente.
    # A pausa abaixo da tempo para a BitDogLab reiniciar e preparar o programa.
    time.sleep(2)

    # Limpa mensagens antigas que possam ter ficado no buffer de entrada.
    conexao.reset_input_buffer()

    print("\nConectado em {} a {} bps.".format(porta, BAUD_RATE))
    return conexao


def ler_respostas(conexao):
    """
    Le todas as linhas de resposta que a BitDogLab enviou pela serial.

    Cada resposta e uma linha de texto terminada por quebra de linha, pois o
    programa da BitDogLab usa print().
    """
    respostas = []

    while conexao.in_waiting:
        linha = conexao.readline().decode("utf-8", errors="replace").strip()

        if linha:
            respostas.append(linha)

    return respostas


def enviar_comando(conexao, comando):
    """
    Envia um comando de texto para a BitDogLab e mostra a resposta recebida.

    O caractere '\n' no final e importante, pois a BitDogLab le uma linha por
    vez usando sys.stdin.readline().
    """
    print("\nEnviando comando:", comando)
    conexao.write((comando + "\n").encode("utf-8"))

    # Pequena espera para dar tempo da placa processar e responder.
    time.sleep(0.2)

    respostas = ler_respostas(conexao)

    if respostas:
        print("Resposta da BitDogLab:")
        for resposta in respostas:
            print("  " + resposta)
    else:
        print("Sem resposta da BitDogLab.")


def escolher_pino():
    """
    Pergunta qual pino do LED RGB sera controlado.

    O aluno pode digitar tanto a opcao do menu quanto o proprio numero do pino.
    """
    print("\nEscolha o LED/pino:")
    print("1 - Pino 11")
    print("2 - Pino 12")
    print("3 - Pino 13")

    opcao = input("Opcao ou numero do pino: ").strip()

    mapa = {
        "1": 11,
        "2": 12,
        "3": 13,
        "11": 11,
        "12": 12,
        "13": 13,
    }

    return mapa.get(opcao)


def mostrar_menu():
    """Mostra o menu principal do programa do computador."""
    print("\n" + "=" * 45)
    print("Controle serial do LED RGB da BitDogLab")
    print("=" * 45)
    print("1 - Ligar um LED especifico")
    print("2 - Desligar um LED especifico")
    print("3 - Ligar todos os LEDs")
    print("4 - Desligar todos os LEDs")
    print("5 - Consultar estado dos LEDs")
    print("0 - Sair")


def executar_opcao(conexao, opcao):
    """Executa a acao escolhida no menu."""
    if opcao == "0":
        return False

    if opcao in ("1", "2"):
        pino = escolher_pino()

        if pino is None:
            print("Opcao de pino invalida. Use 11, 12 ou 13.")
            return True

        if opcao == "1":
            enviar_comando(conexao, "SET {} 1".format(pino))
        else:
            enviar_comando(conexao, "SET {} 0".format(pino))

        return True

    if opcao == "3":
        enviar_comando(conexao, "ALL 1")
        return True

    if opcao == "4":
        enviar_comando(conexao, "ALL 0")
        return True

    if opcao == "5":
        enviar_comando(conexao, "STATUS")
        return True

    print("Opcao invalida. Escolha uma das opcoes do menu.")
    return True


def main():
    """Funcao principal do programa."""
    try:
        conexao = abrir_serial()
    except serial.SerialException as erro:
        print("Nao foi possivel abrir a porta serial.")
        print("Detalhes:", erro)
        return

    if conexao is None:
        return

    try:
        # Logo apos conectar, pedimos o estado atual para confirmar que a
        # comunicacao entre computador e BitDogLab esta funcionando.
        enviar_comando(conexao, "STATUS")

        continuar = True
        while continuar:
            mostrar_menu()
            opcao = input("Escolha uma opcao: ").strip()
            continuar = executar_opcao(conexao, opcao)

        print("\nEncerrando o programa do computador.")
    finally:
        conexao.close()
        print("Porta serial fechada.")


if __name__ == "__main__":
    main()
