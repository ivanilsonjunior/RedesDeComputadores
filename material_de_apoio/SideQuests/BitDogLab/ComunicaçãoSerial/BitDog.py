"""
Codigo para rodar dentro da BitDogLab.

Objetivo:
    Receber comandos enviados pelo computador pela porta serial USB e controlar
    o LED RGB ligado aos pinos GPIO 11, 12 e 13.

Comandos aceitos pela placa:
    STATUS          -> mostra o estado atual dos tres LEDs
    SET 11 1        -> liga o LED do pino 11
    SET 11 0        -> desliga o LED do pino 11
    ALL 1           -> liga todos os LEDs
    ALL 0           -> desliga todos os LEDs

Observacao:
    Este arquivo usa MicroPython, por isso deve ser enviado para a BitDogLab,
    nao executado diretamente no Python do computador.
"""

from machine import Pin
import select
import sys
import time


# Dicionario que associa cada numero de pino ao objeto Pin correspondente.
# Pin.OUT indica que o pino sera usado como saida, ou seja, a placa vai enviar
# nivel logico 0 ou 1 para controlar o LED.
LEDS = {
    11: Pin(11, Pin.OUT),
    12: Pin(12, Pin.OUT),
    13: Pin(13, Pin.OUT),
}


def texto_do_estado(valor):
    """Converte 0/1 em um texto mais amigavel para mostrar ao usuario."""
    if valor:
        return "LIGADO"
    return "DESLIGADO"


def estado_leds():
    """
    Monta uma frase com o estado atual de cada pino.

    Exemplo de retorno:
        pino 11=LIGADO, pino 12=DESLIGADO, pino 13=DESLIGADO
    """
    estados = []

    for pino, led in LEDS.items():
        estados.append("pino {}={}".format(pino, texto_do_estado(led.value())))

    return ", ".join(estados)


def enviar_estado():
    """Envia pela serial o estado atual dos tres LEDs."""
    print("ESTADO: " + estado_leds())


def valor_valido(texto):
    """Verifica se o valor recebido representa ligar ou desligar."""
    return texto in ("0", "1", "ON", "OFF", "LIGAR", "DESLIGAR")


def converter_valor(texto):
    """
    Converte o texto recebido pela serial em 0 ou 1.

    Sao aceitos valores numericos e tambem palavras, para facilitar testes:
        1, ON, LIGAR       -> 1
        0, OFF, DESLIGAR   -> 0
    """
    if texto in ("1", "ON", "LIGAR"):
        return 1
    return 0


def definir_led(pino, valor):
    """
    Liga ou desliga um LED especifico.

    Parametros:
        pino: numero do pino GPIO. Neste exemplo, 11, 12 ou 13.
        valor: 1 para ligar, 0 para desligar.
    """
    if pino not in LEDS:
        print("ERRO: pino {} invalido. Use 11, 12 ou 13.".format(pino))
        return

    LEDS[pino].value(valor)
    print("OK: pino {} {}".format(pino, texto_do_estado(valor)))
    enviar_estado()


def definir_todos(valor):
    """Liga ou desliga todos os LEDs ao mesmo tempo."""
    for led in LEDS.values():
        led.value(valor)

    if valor:
        print("OK: todos os LEDs LIGADOS")
    else:
        print("OK: todos os LEDs DESLIGADOS")

    enviar_estado()


def processar_comando(comando):
    """
    Interpreta uma linha de texto recebida pela serial.

    A comunicacao serial envia e recebe bytes. Neste exemplo, trabalhamos com
    linhas de texto para deixar o protocolo mais facil de enxergar:
        computador envia: SET 11 1
        placa responde:   OK: pino 11 LIGADO
    """
    partes = comando.strip().upper().split()

    if not partes:
        return

    if partes[0] == "STATUS" and len(partes) == 1:
        enviar_estado()
        return

    if partes[0] == "ALL" and len(partes) == 2:
        if not valor_valido(partes[1]):
            print("ERRO: use ALL <0 ou 1>.")
            return

        valor = converter_valor(partes[1])
        definir_todos(valor)
        return

    if partes[0] == "SET" and len(partes) == 3:
        try:
            pino = int(partes[1])
        except ValueError:
            print("ERRO: o pino deve ser um numero. Exemplo: SET 11 1.")
            return

        if not valor_valido(partes[2]):
            print("ERRO: use SET <pino> <0 ou 1>.")
            return

        valor = converter_valor(partes[2])
        definir_led(pino, valor)
        return

    print("ERRO: comando invalido. Use STATUS, ALL <0|1> ou SET <pino> <0|1>.")


# Ao iniciar o programa, todos os LEDs comecam apagados.
for led in LEDS.values():
    led.value(0)

print("BitDogLab pronta para receber comandos pela serial USB.")
print("Comandos: STATUS, ALL <0|1>, SET <pino> <0|1>.")
enviar_estado()

# O poll permite verificar se chegou algum texto na entrada serial sem travar
# o programa esperando indefinidamente.
entrada = select.poll()
entrada.register(sys.stdin, select.POLLIN)

while True:
    # A cada 100 ms, o programa verifica se chegou uma linha nova pela serial.
    if entrada.poll(100):
        linha = sys.stdin.readline()
        processar_comando(linha)

    # Pequena pausa para evitar que o loop rode de forma desnecessariamente
    # acelerada.
    time.sleep_ms(10)
