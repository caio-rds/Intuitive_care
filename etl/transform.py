import os
import zipfile, pdfplumber
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

legend = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

def main():
    try:
        os.makedirs('./output', exist_ok=True)

        with pdfplumber.open("./download/Anexo I.pdf") as pdf:
            tables_df: list = []

            logging.info("Extracting tables from PDF...")
            for page in pdf.pages:
                table = page.extract_table()

                if table is not None:
                    tables_df.append(pd.DataFrame(table[1:], columns=table[0]))

            result = pd.concat(tables_df)
            logging.info("Table extracted!")

            result = result.map(lambda x: legend[x] if x in legend else x)
            result.to_csv("./output/demos_contabeis.csv", index=False)
            logging.info("Table saved!")

        with zipfile.ZipFile('./output/Teste_Caio_Reis.zip', 'w') as zip_file:
            zip_file.write("./output/demos_contabeis.csv", arcname="anexo1.csv")

        logging.info("Zip file created!")
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()