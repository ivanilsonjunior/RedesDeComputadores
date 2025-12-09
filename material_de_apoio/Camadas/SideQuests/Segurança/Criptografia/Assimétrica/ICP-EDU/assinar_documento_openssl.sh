#!/usr/bin/env bash
# assinar_documento_openssl.sh
# Assina digitalmente um arquivo usando chave privada em PEM (ex.: extraída de certificado ICP-EDU).
#
# Uso:
#   ./assinar_documento_openssl.sh chave_privada.pem documento.txt assinatura.bin
#
# Se o terceiro argumento não for informado, será usado 'assinatura.bin' como padrão.

set -e

if [ "$#" -lt 2 ]; then
    echo "Uso: $0 <chave_privada.pem> <documento.txt> [assinatura.bin]"
    exit 1
fi

CHAVE_PRIVADA="$1"
DOCUMENTO="$2"
ASSINATURA="${3:-assinatura.bin}"

if [ ! -f "$CHAVE_PRIVADA" ]; then
    echo "Erro: chave privada não encontrada: $CHAVE_PRIVADA"
    exit 1
fi

if [ ! -f "$DOCUMENTO" ]; then
    echo "Erro: documento não encontrado: $DOCUMENTO"
    exit 1
fi

echo "Assinando documento '$DOCUMENTO' com chave '$CHAVE_PRIVADA'..."
openssl dgst -sha256 -sign "$CHAVE_PRIVADA" -out "$ASSINATURA" "$DOCUMENTO"
echo "Assinatura gerada em: $ASSINATURA"
