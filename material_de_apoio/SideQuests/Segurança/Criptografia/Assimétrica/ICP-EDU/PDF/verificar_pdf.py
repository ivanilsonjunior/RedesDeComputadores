#!/usr/bin/env python3
"""verificar_pdf.py
Verifica assinaturas internas de um PDF assinado no padrão PAdES usando PyHanko.

Requer:
    pip install pyhanko
    documento_assinado.pdf
"""

from pyhanko.sign.validation import validate_pdf_signature
from pyhanko.pdf_utils.reader import PdfFileReader


def verificar_assinatura(pdf_assinado: str):
    with open(pdf_assinado, "rb") as f:
        reader = PdfFileReader(f)

        # Lista campos de assinatura
        sig_fields = reader.root.get("/AcroForm", {}).get("/Fields", [])

        if not sig_fields:
            print("❌ Nenhuma assinatura encontrada no PDF.")
            return

        print(f"🔍 Assinaturas encontradas: {len(sig_fields)}")

        for index, field in enumerate(sig_fields):
            name = field.get_object().get("/T")
            print(f"→ Validando assinatura {index+1}: campo '{name}'")

            status = validate_pdf_signature(reader, field)

            if status.bottom_line:
                print(f"✔ Assinatura VÁLIDA ({name})")
            else:
                print(f"❌ Assinatura INVÁLIDA ({name})")

            print(status.summary())


if __name__ == "__main__":
    verificar_assinatura("documento_assinado.pdf")
