#!/usr/bin/env python3
"""assinar_pdf.py
Assina um PDF usando PyHanko e um certificado ICP-EDU convertido para PEM.

Requer:
    pip install pyhanko
    chave_privada.pem
    certificado_publico.pem
"""

from pyhanko.sign import signers
from pyhanko.sign.general import load_pem_private_key
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter

def assinar_pdf(pdf_in, pdf_out, chave_privada, certificado_publico):
    # Carrega chave privada
    with open(chave_privada, "rb") as f:
        private_key = load_pem_private_key(f.read(), password=None)

    # Carrega certificado
    with open(certificado_publico, "rb") as f:
        cert_bytes = f.read()

    signer = signers.SimpleSigner(
        signing_key=private_key,
        cert=cert_bytes,
        other_certs=None,
        signature_mechanism=signers.PdfSignatureMetadata(field_name="Sig1")
    )

    with open(pdf_in, "rb") as doc:
        writer = IncrementalPdfFileWriter(doc)
        signed_pdf = signer.sign_pdf(writer)

        with open(pdf_out, "wb") as saida:
            signed_pdf.write(saida)

    print(f"✔ PDF assinado com sucesso: {pdf_out}")

if __name__ == "__main__":
    assinar_pdf(
        pdf_in="documento.pdf",
        pdf_out="documento_assinado.pdf",
        chave_privada="chave_privada.pem",
        certificado_publico="certificado_publico.pem",
    )
