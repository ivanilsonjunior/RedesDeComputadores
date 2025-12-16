#!/usr/bin/env python3
"""verificar_assinatura.py
Verifica a assinatura digital de um arquivo usando um certificado/ chave pública em PEM.

Uso básico:
    python verificar_assinatura.py -c certificado_publico.pem -i documento.txt -s assinatura.bin

Requer:
    pip install cryptography
"""

import argparse
from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key


def verificar_assinatura(cert_publico: Path, arquivo_entrada: Path, arquivo_assinatura: Path) -> bool:
    """Verifica se a assinatura em arquivo_assinatura é válida para o conteúdo de arquivo_entrada."""
    if not cert_publico.is_file():
        raise FileNotFoundError(f"Certificado público não encontrado: {cert_publico}")
    if not arquivo_entrada.is_file():
        raise FileNotFoundError(f"Arquivo a ser verificado não encontrado: {arquivo_entrada}")
    if not arquivo_assinatura.is_file():
        raise FileNotFoundError(f"Arquivo de assinatura não encontrado: {arquivo_assinatura}")

    # Carrega chave pública a partir do certificado em PEM
    with cert_publico.open("rb") as f:
        public_key = load_pem_public_key(f.read())

    # Lê dados originais
    with arquivo_entrada.open("rb") as f:
        dados = f.read()

    # Lê assinatura
    with arquivo_assinatura.open("rb") as f:
        assinatura = f.read()

    try:
        public_key.verify(
            assinatura,
            dados,
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
        print("✔ Assinatura VÁLIDA!")
        print(f"  Arquivo verificado : {arquivo_entrada}")
        print(f"  Assinatura usada   : {arquivo_assinatura}")
        return True
    except Exception as e:
        print("❌ Assinatura INVÁLIDA!")
        print(f"  Motivo: {e}")
        return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verifica assinatura digital de arquivo usando certificado público em PEM."
    )
    parser.add_argument(
        "-c", "--cert",
        type=Path,
        required=True,
        help="Caminho para o certificado público em formato PEM (ex.: certificado_publico.pem)",
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        help="Arquivo original (documento que foi assinado)",
    )
    parser.add_argument(
        "-s", "--signature",
        type=Path,
        default=Path("assinatura.bin"),
        help="Arquivo contendo a assinatura (padrão: assinatura.bin)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    verificar_assinatura(args.cert, args.input, args.signature)
