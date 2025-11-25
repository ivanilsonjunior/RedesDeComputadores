#!/usr/bin/env python3
"""
Envio simples de e-mail com SMTP (didático)

Objetivo didático:
    - Demonstrar o protocolo SMTP com Python.
    - Não cobre segurança (TLS, autenticação)
    - Apenas para mostrar o fluxo: HELO, MAIL FROM, RCPT TO, DATA, QUIT.
"""

import smtplib

def main():
    servidor = "smtp.ifrn.edu.br"
    remetente = "aluno@ifrn.edu.br"
    destinatario = "professor@ifrn.edu.br"
    mensagem = """Subject: Teste SMTP

Olá! Este é um e-mail enviado via script Python (exemplo didático).
"""

    with smtplib.SMTP(servidor, 25) as smtp:
        smtp.sendmail(remetente, destinatario, mensagem)

    print("[*] E-mail enviado com sucesso (conceito).")


if __name__ == "__main__":
    main()
