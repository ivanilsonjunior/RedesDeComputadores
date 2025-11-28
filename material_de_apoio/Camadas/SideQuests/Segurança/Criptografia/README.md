# Criptografia Simétrica

Este diretório contém exemplos didáticos de **criptografia simétrica**, utilizados como
material de apoio para a disciplina de Redes de Computadores / IoT.

## Objetivos
- Compreender o conceito de chave simétrica
- Comparar cifras clássicas e modernas
- Entender modos de operação de cifras de bloco
- Aplicar criptografia na proteção de dados e arquivos
- Servir de base para discussões sobre segurança em redes e IoT

## Estrutura
- exemplos_basicos: cifras simples (didáticas)
- blocos: cifras de bloco modernas (AES)
- arquivos: criptografia aplicada a arquivos reais
- testes: scripts de validação e comparação

## Requisitos
- Python 3.9+
- Biblioteca `cryptography` (para exemplos com AES):
```bash
pip install cryptography

```

# 🔐 Exemplo 1 — Cifra de César (didático)

### `exemplos_basicos/cesar/README.md`

```markdown
# Cifra de César

Exemplo clássico de criptografia por substituição.
Usado apenas para fins didáticos.

⚠️ Não é segura e não deve ser usada em sistemas reais.
