#!/usr/bin/env python3
"""
Script: ethernet_info_python3.py
Modulo 06 — Componentes Fisicos de Redes
DIATINF — IFRN

Objetivo:
    Exibir informacoes detalhadas das interfaces Ethernet no Linux,
    incluindo velocidade, duplex, autonegociacao e estado do link.

Requisitos:
    - Sistema Linux
    - Pacote ethtool instalado

Execucao:
    $ python3 ethernet_info_python3.py
"""

import os
import subprocess

def listar_interfaces():
    """
    Lista interfaces disponiveis no sistema.
    Considera apenas interfaces Ethernet (ethX, enpXsY, ensX, etc.).
    """
    interfaces = []
    caminho = "/sys/class/net/"

    for iface in os.listdir(caminho):
        # Ignorar Wi-Fi (wlanX), loopback (lo) e docker
        if iface.startswith("wl") or iface == "lo" or iface.startswith("docker"):
            continue
        interfaces.append(iface)

    return interfaces


def obter_info_interface(interface):
    """
    Usa o comando 'ethtool' para extrair informacoes da interface.
    """
    try:
        resultado = subprocess.check_output(["ethtool", interface], text=True)
        return resultado
    except Exception as e:
        return f"Erro ao consultar {interface}: {e}"


def main():
    print("\n===== INFORMACOES DE INTERFACES ETHERNET =====\n")

    interfaces = listar_interfaces()

    if not interfaces:
        print("Nenhuma interface Ethernet encontrada.")
        return

    for iface in interfaces:
        print(f"--- Interface: {iface} ---")
        print(obter_info_interface(iface))
        print("---------------------------------------------\n")


if __name__ == "__main__":
    main()
