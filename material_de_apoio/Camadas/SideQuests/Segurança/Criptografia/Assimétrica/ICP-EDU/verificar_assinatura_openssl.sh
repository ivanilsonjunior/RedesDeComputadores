#!/usr/bin/env bash
# verificar_assinatura_openssl.sh
# Verifica a assinatura digital de um arquivo usando certificado público em PEM.
#
# Uso:
#   ./verificar_assinatura_openssl.sh certificado_publico.pem documento.txt assinatura.bin

set -e

if [ "$#" -lt 3 ]; then
    echo "Uso: $0 <certificado_publico.pem> <documento.txt> <assinatura.bin>"
    exit 1
fi

CERT_PUB="$1"
DOCUMENTO="$2"
ASSINATURA="$3"

if [ ! -f "$CERT_PUB" ]; then
    echo "Erro: certificado público não encontrado: $CERT_PUB"
    exit 1
fi

if [ ! -f "$DOCUMENTO" ]; then
    echo "Erro: documento não encontrado: $DOCUMENTO"
    exit 1
fi

if [ ! -f "$ASSINATURA" ]; then
    echo "Erro: arquivo de assinatura não encontrado: $ASSINATURA"
    exit 1
fi

echo "Verificando assinatura..."
openssl dgst -sha256 -verify "$CERT_PUB" -signature "$ASSINATURA" "$DOCUMENTO"
