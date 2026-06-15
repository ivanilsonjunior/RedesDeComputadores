"""
Medidor de som para a BitDogLab.

Objetivo:
    Ler o microfone da placa, mostrar o volume no terminal serial e acender a
    matriz de LEDs 5x5 conforme a intensidade do som.

Hardware usado neste exemplo:
    - Microfone ligado ao ADC do GPIO 28
    - Matriz NeoPixel 5x5 ligada ao GPIO 7

Observacao:
    A matriz possui 25 LEDs no total, organizados em 5 linhas por 5 colunas.
    Este arquivo usa MicroPython e deve ser enviado para a BitDogLab.
"""

from machine import ADC, Pin
import math
import neopixel
import time


# ----------------------------
# Configuracao do hardware
# ----------------------------

# Quantidade total de LEDs da matriz 5x5.
NUM_LEDS = 25

# Pino de dados da matriz de LEDs NeoPixel.
PINO_MATRIZ = 7

# Pino analogico usado pelo microfone da BitDogLab.
PINO_MICROFONE = 28

# Objeto que controla a matriz NeoPixel.
matriz = neopixel.NeoPixel(Pin(PINO_MATRIZ), NUM_LEDS)

# Objeto que le o sinal analogico do microfone.
microfone = ADC(Pin(PINO_MICROFONE))


# ----------------------------
# Ajustes do medidor
# ----------------------------

# Numero de leituras usadas para medir uma "janela" de som.
# Quanto maior o valor, mais estavel fica a medida, mas a resposta fica mais
# lenta. Valores entre 50 e 120 costumam funcionar bem para este exemplo.
AMOSTRAS_POR_LEITURA = 80

# Abaixo deste valor, consideramos silencio ou ruido de fundo.
# Se a matriz ficar acendendo mesmo em silencio, aumente este valor.
NIVEL_SILENCIO = 350

# Valor aproximado que sera tratado como som muito alto.
# Se a matriz quase nunca chegar ao maximo, diminua este valor.
# Se ela chegar ao maximo com facilidade demais, aumente este valor.
NIVEL_SOM_FORTE = 12000

# Intervalo entre atualizacoes no terminal, em milissegundos.
# A matriz atualiza sempre, mas o terminal nao precisa receber texto a cada loop.
INTERVALO_PRINT_MS = 250


# ----------------------------
# Cores
# ----------------------------

PRETO = (0, 0, 0)
AZUL = (0, 0, 60)
VERDE = (0, 45, 0)
AMARELO = (45, 35, 0)
VERMELHO = (70, 0, 0)


# ----------------------------
# Patamares da matriz 5x5
# ----------------------------

# Cada lista representa um nivel do medidor.
# Quanto maior o volume, mais LEDs sao acesos.
#
# Os numeros sao os indices dos LEDs na matriz NeoPixel. Esta ordem foi
# aproveitada do exemplo original da BitDogLab.
PATAMARES = [
    [2],
    [1, 2, 3],
    [7, 1, 2, 3],
    [12, 6, 7, 8, 0, 1, 2, 3, 4],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14, 15, 19],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14, 15, 19, 20, 21, 23, 24],
]


def limitar(valor, minimo, maximo):
    """Mantem um valor dentro de um intervalo."""
    if valor < minimo:
        return minimo

    if valor > maximo:
        return maximo

    return valor


def apagar_matriz():
    """Desliga todos os LEDs da matriz."""
    for indice in range(NUM_LEDS):
        matriz[indice] = PRETO

    matriz.write()


def escolher_cor(nivel):
    """
    Escolhe a cor de acordo com o nivel do volume.

    Niveis baixos ficam azulados, niveis medios ficam verdes/amarelos e niveis
    altos ficam vermelhos.
    """
    quantidade_de_niveis = len(PATAMARES)

    if nivel < quantidade_de_niveis * 0.35:
        return AZUL

    if nivel < quantidade_de_niveis * 0.65:
        return VERDE

    if nivel < quantidade_de_niveis * 0.85:
        return AMARELO

    return VERMELHO


def medir_amplitude():
    """
    Mede a variacao do sinal do microfone.

    O ADC da BitDogLab retorna valores entre 0 e 65535. Como som e uma onda, o
    valor sobe e desce rapidamente. Para estimar o volume, fazemos varias
    leituras e calculamos a diferenca entre a maior e a menor leitura.

    Essa diferenca e chamada aqui de amplitude.
    """
    menor = 65535
    maior = 0

    for _ in range(AMOSTRAS_POR_LEITURA):
        leitura = microfone.read_u16()

        if leitura < menor:
            menor = leitura

        if leitura > maior:
            maior = leitura

    return maior - menor


def calcular_volume(amplitude):
    """
    Converte a amplitude do microfone para um volume entre 0.0 e 1.0.

    0.0 representa silencio.
    1.0 representa volume alto.
    """
    amplitude_util = amplitude - NIVEL_SILENCIO
    proporcao = amplitude_util / (NIVEL_SOM_FORTE - NIVEL_SILENCIO)
    proporcao = limitar(proporcao, 0.0, 1.0)

    # A raiz quadrada deixa o medidor mais sensivel para sons baixos e medios.
    return math.sqrt(proporcao)


def atualizar_matriz(volume):
    """Acende a matriz de LEDs de acordo com o volume calculado."""
    if volume <= 0:
        apagar_matriz()
        return

    indice_patamar = int(volume * len(PATAMARES))
    indice_patamar = limitar(indice_patamar, 0, len(PATAMARES) - 1)
    cor = escolher_cor(indice_patamar)

    for indice in range(NUM_LEDS):
        matriz[indice] = PRETO

    for indice in PATAMARES[indice_patamar]:
        matriz[indice] = cor

    matriz.write()


def desenhar_barra_terminal(volume):
    """Cria uma barra de texto para visualizar o volume no terminal."""
    total_blocos = 20
    blocos_acesos = int(volume * total_blocos)
    blocos_apagados = total_blocos - blocos_acesos
    return "[" + "#" * blocos_acesos + "." * blocos_apagados + "]"


def mostrar_volume_no_terminal(amplitude, volume):
    """Mostra no terminal serial a amplitude e o volume em porcentagem."""
    porcentagem = int(volume * 100)
    barra = desenhar_barra_terminal(volume)

    print(
        "Amplitude: {:5d} | Volume: {:3d}% {}".format(
            amplitude,
            porcentagem,
            barra,
        )
    )


def main():
    """Loop principal do medidor de som."""
    apagar_matriz()

    print("Medidor de som iniciado.")
    print("Fale, bata palmas ou aproxime uma fonte de som do microfone.")
    print("Use Ctrl+C no terminal ou interrompa a execucao para parar.")

    ultimo_print = time.ticks_ms()

    while True:
        amplitude = medir_amplitude()
        volume = calcular_volume(amplitude)

        atualizar_matriz(volume)

        agora = time.ticks_ms()
        if time.ticks_diff(agora, ultimo_print) >= INTERVALO_PRINT_MS:
            mostrar_volume_no_terminal(amplitude, volume)
            ultimo_print = agora

        time.sleep_ms(20)


main()
