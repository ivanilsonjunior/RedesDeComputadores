"""
Monitor de Vagas — Agendamento de Identidade (PCI-RN)
SideQuest — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Ficar de olho no site de agendamento da Carteira de Identidade Nacional
    do Rio Grande do Norte (https://agendamento.pci.rn.gov.br) e avisar,
    com uma notificação do sistema, assim que surgir uma vaga na cidade
    escolhida pelo usuário.

Conceitos reforçados:
    - cliente HTTP consumindo uma API REST (requests)
    - parsing de JSON
    - laço de repetição com espera (polling)
    - notificação do sistema operacional via subprocess

Como funciona (engenharia reversa do site — ver README.md para detalhes):
    1. GET /api/get-locais/public
           -> lista de cidades/unidades de atendimento
    2. GET /api/ordens/public
           -> "lotes" de vagas por cidade/dia, cada um com um id (ordem) e
              um status (LIBERADO/DESLIBERADO)
    3. GET /api/ordens/public/datas?ordem=<id>
           -> datas com vaga para aquele lote
    4. GET /api/vagas/horas?ordem=<id>&data=<data>
           -> horários ainda livres naquela data

    Se o passo 3 não retornar datas, ou o passo 4 não retornar horários,
    é exatamente a mesma situação que o site mostra como a mensagem
    "Novas vagas no próximo dia útil às 8h".

Importante:
    Este script é só de MONITORAMENTO — ele nunca tenta agendar sozinho.
    A etapa final de agendamento no site exige resolver um captcha, que é
    justamente o que garante que um humano confirme o horário. Quando uma
    vaga é encontrada, o script só avisa; agendar é sempre feito por você,
    manualmente, no site.

Dependências:
    - requests -> pip install requests

Execução:
    $ python3 monitor_vagas.py

Teste:
    Ao rodar, escolha uma cidade da lista numerada exibida no terminal.
    O script consulta a API a cada alguns minutos e imprime o resultado de
    cada consulta; quando encontrar vaga, dispara uma notificação do
    sistema (via notify-send, no Linux) além de imprimir no terminal.
"""

import subprocess
import sys
import time
from datetime import datetime

import requests

BASE_URL = "https://agendamento.pci.rn.gov.br/api"
SERVICO = "identidade"          # único serviço oferecido pelo site hoje
INTERVALO_SEGUNDOS = 5 * 60     # tempo de espera entre cada rodada de consulta

# Identificar o script no cabeçalho é uma boa prática ao consumir uma API
# que não foi documentada oficialmente para uso por terceiros.
HEADERS = {"User-Agent": "MonitorVagasPCI-RN-fins-educacionais/1.0"}


def buscar_localidades() -> list:
    """Retorna a lista de cidades/unidades de atendimento disponíveis."""
    resposta = requests.get(f"{BASE_URL}/get-locais/public", headers=HEADERS, timeout=10)
    resposta.raise_for_status()
    return resposta.json()


def escolher_localidades(localidades: list) -> list:
    """Mostra um menu numerado no terminal e devolve as localidades escolhidas
    (o usuário pode digitar mais de um número, separado por vírgula)."""
    print("Localidades disponíveis para agendamento de identidade:\n")
    for indice, localidade in enumerate(localidades, start=1):
        print(f"  {indice:2d} - {localidade['nome']}")

    while True:
        escolha = input("\nDigite o(s) número(s) das localidades (ex.: 1 ou 1,5,10): ")
        numeros = [n.strip() for n in escolha.split(",") if n.strip()]

        if numeros and all(n.isdigit() and 1 <= int(n) <= len(localidades) for n in numeros):
            # dict.fromkeys remove duplicatas mantendo a ordem digitada
            indices_escolhidos = dict.fromkeys(int(n) - 1 for n in numeros)
            return [localidades[i] for i in indices_escolhidos]

        print("Opção inválida, tente novamente.")


def buscar_ordens_da_localidade(nome_localidade: str) -> list:
    """Retorna os lotes de vagas (ordens) LIBERADOS para a localidade escolhida."""
    resposta = requests.get(f"{BASE_URL}/ordens/public", headers=HEADERS, timeout=10)
    resposta.raise_for_status()
    ordens = resposta.json()
    return [
        ordem for ordem in ordens
        if ordem["servico"] == SERVICO
        and ordem["status"] == "LIBERADO"
        and ordem["localizacao"]["nome"] == nome_localidade
    ]


def buscar_datas_da_ordem(id_ordem: int) -> list:
    resposta = requests.get(
        f"{BASE_URL}/ordens/public/datas", params={"ordem": id_ordem}, headers=HEADERS, timeout=10
    )
    resposta.raise_for_status()
    return resposta.json()


def buscar_horarios_livres(id_ordem: int, data: str) -> list:
    resposta = requests.get(
        f"{BASE_URL}/vagas/horas", params={"ordem": id_ordem, "data": data}, headers=HEADERS, timeout=10
    )
    resposta.raise_for_status()
    return resposta.json()


def notificar(titulo: str, mensagem: str):
    """Mostra uma notificação do sistema (Linux, via notify-send). Se não
    estiver disponível, cai para um aviso sonoro + texto no terminal."""
    try:
        subprocess.run(["notify-send", titulo, mensagem], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("\a" + f"[NOTIFICAÇÃO] {titulo}: {mensagem}")


def verificar_vaga(nome_localidade: str, ja_notificados: set) -> None:
    """Faz uma rodada de checagem e avisa de cada vaga nova encontrada."""
    agora = datetime.now().strftime("%H:%M:%S")
    ordens = buscar_ordens_da_localidade(nome_localidade)

    encontrou_alguma = False
    for ordem in ordens:
        datas = buscar_datas_da_ordem(ordem["id"])
        for data in datas:
            chave = (ordem["id"], data)
            horarios = buscar_horarios_livres(ordem["id"], data)
            if horarios and chave not in ja_notificados:
                ja_notificados.add(chave)
                encontrou_alguma = True
                mensagem = f"{nome_localidade}: {len(horarios)} horário(s) livre(s) em {data}!"
                print(f"[{agora}] VAGA ENCONTRADA! {mensagem}")
                notificar("Vaga de identidade disponível!", mensagem + " Acesse o site para agendar.")

    if not encontrou_alguma:
        print(f"[{agora}] {nome_localidade}: Novas vagas no próximo dia útil às 8h")


def main():
    try:
        localidades = buscar_localidades()
    except requests.RequestException as erro:
        sys.exit(f"Não foi possível consultar o site de agendamento: {erro}")

    localidades_escolhidas = escolher_localidades(localidades)
    nomes_escolhidos = ", ".join(loc["nome"] for loc in localidades_escolhidas)
    print(
        f"\nMonitorando {nomes_escolhidos} a cada {INTERVALO_SEGUNDOS // 60} minuto(s)."
        " Pressione Ctrl+C para parar.\n"
    )

    # Um único conjunto para todas as localidades: cada vaga é identificada
    # por (id_da_ordem, data), e uma ordem sempre pertence a uma única
    # localidade, então não há risco de misturar vagas de cidades diferentes.
    ja_notificados = set()
    while True:
        for localidade in localidades_escolhidas:
            try:
                verificar_vaga(localidade["nome"], ja_notificados)
            except requests.RequestException as erro:
                print(f"Erro ao consultar a API para {localidade['nome']}: {erro}")
        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")
