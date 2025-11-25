#!/usr/bin/env python3
"""
Envio simples de e-mail usando SMTP (Didático)
Camada de Aplicação — Redes de Computadores / ADS

Objetivo:
    - Demonstrar o protocolo SMTP de forma prática.
    - Enviar um e-mail simples sem anexos.
    - Mostrar a estrutura básica do comando SMTP.

Execução:
    $ python3 smtp_enviar_python3.py

IMPORTANTE:
    Este exemplo usa SMTP SEM autenticação (porta 25).
    Em redes modernas, muitos provedores bloqueiam essa porta.
    Use apenas em redes de laboratório, como no IFRN.
"""

import smtplib

SERVIDOR_SMTP = "smtp.ifrn.edu.br"  # Ajuste conforme seu ambiente
PORTA = 25

REMETENTE = "aluno@ifrn.edu.br"
DESTINATARIO = "professor@ifrn.edu.br"

def main():
    mensagem = """Subject: Teste de SMTP (Exemplo Didático)

Olá, professor!
Este e-mail foi enviado automaticamente usando Python.
Este script demonstra o funcionamento básico do protocolo SMTP.
"""

    print(f"[*] Conectando ao servidor SMTP {SERVIDOR_SMTP}:{PORTA} ...")

    with smtplib.SMTP(SERVIDOR_SMTP, PORTA) as servidor:
        print("[+] Conexão estabelecida!")
        print("[*] Enviando e-mail...")

        servidor.sendmail(REMETENTE, DESTINATARIO, mensagem)

        print("[+] E-mail enviado com sucesso!")

if __name__ == "__main__":
    main()
