#!/usr/bin/env python3
"""assinar_documento.py
Assina digitalmente um arquivo usando uma chave privada em formato PEM.

Uso básico:
    python assinar_documento.py -k chave_privada.pem -i documento.txt -o assinatura.bin

Requer:
    pip install cryptography
"""

import argparse
from pathlib import Path

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def assinar_documento(caminho_privada: Path, arquivo_entrada: Path, arquivo_assinatura: Path) -> None:
    """Assina o conteúdo de arquivo_entrada e grava a assinatura em arquivo_assinatura."""
    if not caminho_privada.is_file():
        raise FileNotFoundError(f"Chave privada não encontrada: {caminho_privada}")
    if not arquivo_entrada.is_file():
        raise FileNotFoundError(f"Arquivo a ser assinado não encontrado: {arquivo_entrada}")

    # Carrega chave privada (sem senha)
    with caminho_privada.open("rb") as f:
        private_key = load_pem_private_key(f.read(), password=None)

    # Lê dados a serem assinados
    with arquivo_entrada.open("rb") as f:
        dados = f.read()

    # Gera assinatura
    assinatura = private_key.sign(
        dados,
        padding.PKCS1v15(),
        hashes.SHA256(),
    )

    # Grava assinatura em arquivo
    with arquivo_assinatura.open("wb") as f:
        f.write(assinatura)

    print(f"✔ Documento assinado com sucesso!")
    print(f"  Arquivo de entrada : {arquivo_entrada}")
    print(f"  Assinatura gerada : {arquivo_assinatura}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assina digitalmente um arquivo usando chave privada em PEM (ICP-EDU, por exemplo)."
    )
    parser.add_argument(
        "-k", "--key",
        type=Path,
        required=True,
        help="Caminho para a chave privada em formato PEM (ex.: chave_privada.pem)",
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        help="Arquivo de entrada (documento a ser assinado)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("assinatura.bin"),
        help="Arquivo de saída para a assinatura (padrão: assinatura.bin)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    assinar_documento(args.key, args.input, args.output)
