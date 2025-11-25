#!/usr/bin/env python3
"""
Script: wifi_scan_python3.py
Modulo 06 — Componentes Fisicos de Redes
DIATINF — IFRN

Objetivo:
    Realizar varredura de redes Wi‑Fi disponiveis no sistema
    utilizando o comando 'nmcli', comum em distribuições Linux.

Requisitos:
    - Sistema Linux com NetworkManager
    - Comando nmcli instalado

Execucao:
    $ python3 wifi_scan_python3.py
"""

import subprocess

def escanear_wifi():
    """
    Executa o comando nmcli para listar redes Wi‑Fi detectadas.
    """
    try:
        resultado = subprocess.check_output(
            ["nmcli", "-f", "SSID,SIGNAL,SECURITY,BARS", "device", "wifi", "list"],
            text=True
        )
        return resultado
    except Exception as e:
        return f"Erro ao escanear redes Wi‑Fi: {e}"

def main():
    print("\n===== VARREDURA WI-FI =====\n")

    saida = escanear_wifi()
    print(saida)

    print("""
Legenda:
    SSID     → Nome da rede Wi‑Fi
    SIGNAL   → Intensidade do sinal (0–100)
    SECURITY → Tipo de seguranca (WPA/WPA2/WPA3)
    BARS     → Barras de qualidade
""")

if __name__ == "__main__":
    main()
