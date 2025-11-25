#!/usr/bin/env python3
"""
Simulador de Roteador IP (Encaminhamento de Pacotes)
Camada de Rede — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Simular o funcionamento básico de um roteador IP:

    - Tabela de rotas
    - Escolha da rota mais específica (longest prefix match)
    - Decremento do TTL
    - Encaminhamento ou descarte
    - Fragmentação didática (se payload > MTU)
    - Interface de entrada e saída

Observação:
    Este é um simulador lógico — não envia pacotes reais.
    É ideal para ensinar encaminhamento IP em sala de aula.

Execução:
    $ python3 roteador_simples_python3.py
"""

import ipaddress


class Roteador:
    def __init__(self, mtu=50):
        # Tabela de rotas
        # Cada rota contém: rede, next-hop, interface
        self.rotas = []
        self.mtu = mtu  # tamanho máximo do payload para simulação

    def adicionar_rota(self, rede, next_hop, interface):
        """
        Adiciona uma entrada na tabela de roteamento.
        Exemplo: adicionar_rota("192.168.1.0/24", "192.168.1.1", "eth0")
        """
        rede_obj = ipaddress.ip_network(rede, strict=False)
        self.rotas.append({
            "rede": rede_obj,
            "next_hop": next_hop,
            "interface": interface
        })

    def mostrar_rotas(self):
        print("\n===== TABELA DE ROTAS =====")
        for r in self.rotas:
            print(f"{r['rede']}   via {r['next_hop']}   dev {r['interface']}")
        print("============================\n")

    def selecionar_rota(self, destino):
        """
        Escolhe a rota mais específica usando Longest Prefix Match.
        """
        destino_ip = ipaddress.ip_address(destino)
        rotas_validas = []

        for r in self.rotas:
            if destino_ip in r["rede"]:
                rotas_validas.append(r)

        if not rotas_validas:
            return None

        # Longest Prefix = maior prefixo (/24 melhor que /16)
        rotas_validas.sort(key=lambda x: x["rede"].prefixlen, reverse=True)
        return rotas_validas[0]

    def fragmentar(self, payload):
        """
        Simula fragmentação caso o payload ultrapasse o MTU.
        """
        if len(payload) <= self.mtu:
            return [payload]

        print(f"[ROTEADOR] Fragmentando payload grande (size={len(payload)}).")

        partes = []
        for i in range(0, len(payload), self.mtu):
            partes.append(payload[i:i+self.mtu])

        return partes

    def encaminhar(self, pacote):
        """
        Simula todo o processo de encaminhamento IP.
        O pacote contém:
            - origem
            - destino
            - ttl
            - payload (dados)
        """
        print("\n===== RECEBENDO PACOTE =====")
        print(f"Origem:    {pacote['origem']}")
        print(f"Destino:   {pacote['destino']}")
        print(f"TTL:       {pacote['ttl']}")
        print(f"Payload:   \"{pacote['payload']}\"")

        # TTL
        pacote["ttl"] -= 1
        if pacote["ttl"] <= 0:
            print("[-] TTL expirou! Pacote descartado.")
            return

        # Tabela de roteamento
        rota = self.selecionar_rota(pacote["destino"])
        if rota is None:
            print("[-] Sem rota para este destino. Pacote descartado.")
            return

        print(f"[+] Rota encontrada: {rota['rede']} via {rota['next_hop']} dev {rota['interface']}")

        # Fragmentação
        fragmentos = self.fragmentar(pacote["payload"])

        for i, frag in enumerate(fragmentos):
            print(f"[+] Enviando fragmento {i+1}/{len(fragmentos)} pela interface {rota['interface']}")
            print(f"    Next-hop: {rota['next_hop']}")
            print(f"    Conteúdo: \"{frag}\"")

        print("===== PACOTE ENCAMINHADO =====\n")


def main():
    roteador = Roteador(mtu=20)

    # Tabela de rotas padrão (didática)
    roteador.adicionar_rota("10.0.0.0/24", "10.0.0.1", "eth0")
    roteador.adicionar_rota("10.0.1.0/24", "10.0.1.1", "eth1")
    roteador.adicionar_rota("0.0.0.0/0", "192.168.0.1", "eth0")  # rota default

    roteador.mostrar_rotas()

    # Pacote de teste
    pacote = {
        "origem": "10.0.0.50",
        "destino": "10.0.1.25",
        "ttl": 5,
        "payload": "Mensagem muito longa para demonstrar fragmentacao."
    }

    roteador.encaminhar(pacote)


if __name__ == "__main__":
    main()
