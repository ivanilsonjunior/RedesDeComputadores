#!/usr/bin/env python3
"""
Leitor de Tabela de Roteamento do Sistema Operacional
Camada de Rede — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar como visualizar e interpretar a tabela de roteamento
    usando Python. O script roda comandos nativos do sistema:

    Linux:   ip route
    Windows: route print

Conceitos reforçados:
    - Rota padrão (default)
    - Rota de rede
    - Gateway
    - Métrica
    - Interface de saída
    - Relação IP -> Roteamento -> Encaminhamento

Execução:
    $ python3 tabela_de_roteamento_python3.py
"""

import platform
import subprocess
import sys


def obter_tabela_linux():
    """
    Executa 'ip route' no Linux.
    """
    try:
        resultado = subprocess.check_output(["ip", "route"], text=True)
        print("Tabela de Roteamento (Linux):\n")
        print(resultado)
    except Exception as e:
        print("Erro ao executar 'ip route':", e)


def obter_tabela_windows():
    """
    Executa 'route print' no Windows.
    """
    try:
        resultado = subprocess.check_output(["route", "print"], text=True)
        print("Tabela de Roteamento (Windows):\n")
        print(resultado)
    except Exception as e:
        print("Erro ao executar 'route print':", e)


def main():
    sistema = platform.system().lower()

    print("\n===== LEITOR DE TABELA DE ROTEAMENTO =====\n")

    if "linux" in sistema:
        obter_tabela_linux()

    elif "windows" in sistema:
        obter_tabela_windows()

    else:
        print("Sistema operacional não suportado:", sistema)
        sys.exit(1)

    print("\nInterprete a saída:")
    print("- default / 0.0.0.0   → rota padrão")
    print("- via X.X.X.X         → gateway")
    print("- dev ethX / wlanX    → interface de saída")
    print("- metric N            → custo para decisão de rota")
    print("- redes específicas   → rotas mais específicas prevalecem")


if __name__ == "__main__":
    main()
