import pandas as pd
import re
from PyPDF2 import PdfReader

# Caminho do arquivo CSV de saída
csv_output_path = "output.csv"
pdf_path = "../../media/Anexo I.pdf"

# Função para verificar a extração de texto e formatar como tabela
def verify_pdf_extraction():
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
            procedimento = line.split()[0] if line.split() else None
            rn = None
            vigencia = None
            od = None
            amb = None
            hco = None
            hso = None
            ref = None
            pac = None
            dut = None
            subgrupo = "Subgrupo"  # Exemplo de valor padrão
            grupo = "Grupo"  # Exemplo de valor padrão
            capitulo = "Capítulo"  # Exemplo de valor padrão
            if rn_match := rn_pattern.search(line):
                rn = rn_match.group()
            if vigencia_match := vigencia_pattern.search(line):
                vigencia = vigencia_match.group()

            if "OD" in line:
                od = "OD"
            if "AMB" in line:
                amb = "AMB"
            if "HCO" in line:
                hco = "HCO"
            if "HSO" in line:
                hso = "HSO"
            if "REF" in line:
                ref = "REF"
            if "PAC" in line:
                pac = "PAC"
            if "DUT" in line:
                dut = "DUT"

            # Adicionar os valores extraídos à lista de dados
            data.append([procedimento, rn, vigencia, od, amb, hco, hso, ref, pac, dut, subgrupo, grupo, capitulo])

    # Verificar se os dados foram extraídos corretamente
    if not data:
        print("Nenhum dado foi extraído do PDF.")
        return

    # Criar um DataFrame do pandas e salvar em um arquivo CSV
    df = pd.DataFrame(data, columns=["PROCEDIMENTO", "RN(alteração)", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"])

    # **Garantir que o DataFrame tenha os headers corretos ao salvar**
    print(df.head())  # Visualizar os dados antes de salvar
    df.to_csv(csv_output_path, index=False, header=True, columns=headers)  # header=True para garantir que os headers sejam salvos corretamente

# Verificando o PDF e salvando os dados em um arquivo CSV
verify_pdf_extraction()
