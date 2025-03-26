import pandas as pd
import re
from PyPDF2 import PdfReader

# Caminho do arquivo PDF
pdf_path = "../../media/Anexo I.pdf"
# Caminho do arquivo CSV de saída
csv_output_path = "output.csv"

# Função para verificar a extração de texto e formatar como tabela
def verify_pdf_extraction(pdf_path, csv_output_path):
    reader = PdfReader(pdf_path)
    data = []
    headers = ["PROCEDIMENTO", "RN(alteração)", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]

    rn_pattern = re.compile(r"\d{3}/\d{4}")
    vigencia_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        # Extrair valores
        values_start = text.find("alterações)") + len("alterações)")
        values_end = text.find("Legenda:")
        values_text = text[values_start:values_end].strip()
        lines = values_text.split('\n')

        # Join lines that end with "E "
        i = 0
        while i < len(lines) - 1:
            if lines[i].endswith("E ") or lines[i].endswith("E") or lines[i].endswith(" "):
                lines[i] = lines[i] + lines[i + 1].strip()
                del lines[i + 1]
            else:
                i += 1

        for line in lines:
            print(line)


# Verificando o PDF e salvando os dados em um arquivo CSV
verify_pdf_extraction(pdf_path, csv_output_path)