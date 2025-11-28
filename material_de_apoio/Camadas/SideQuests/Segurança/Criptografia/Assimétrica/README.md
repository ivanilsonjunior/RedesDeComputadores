# 🔐 Criptografia Assimétrica

## Disciplina: Redes de Computadores / Internet das Coisas (IoT)

Criptografia assimétrica utiliza um par de chaves:
- Chave pública (divulgável)
- Chave privada (secreta)

É fundamental para a segurança em redes modernas, sendo a base
de protocolos como HTTPS, TLS e SSH.

---

## Diferença entre criptografia simétrica e assimétrica

| Simétrica | Assimétrica |
|---------|-------------|
| Uma chave | Duas chaves |
| Rápida | Mais lenta |
| Boa para grandes dados | Ideal para troca de chaves |
| AES | RSA |

---

## Usos principais
- Troca segura de chaves
- Assinatura digital
- Autenticação em rede
- Certificados digitais

---

## Estrutura
- `basico/` – uso básico do RSA
- `assinatura/` – assinatura e verificação
- `socket_rsa/` – uso em comunicação pela rede
