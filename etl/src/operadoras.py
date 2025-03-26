import csv
import logging
from datetime import datetime

from mysql import connector
from mysql.connector import Error
import mysql

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        crs = connection.cursor()
        crs.execute("CREATE DATABASE IF NOT EXISTS intuitive_care")
        crs.close()
        connection.database = "intuitive_care"
        logging.info("Database created/connected successfully")
    except Error as e:
        logging.error(e)

    return connection

con = create_connection()


def create_table(connection):
    crs = connection.cursor()
    try:
        crs.execute("""
             CREATE TABLE IF NOT EXISTS operadoras (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 registro_ans VARCHAR(6) NOT NULL,
                 cnpj VARCHAR(18) NOT NULL,
                 razao_social VARCHAR(255) NOT NULL,
                 nome_fantasia VARCHAR(255),
                 modalidade VARCHAR(50),
                 logradouro VARCHAR(40) NOT NULL,
                 numero VARCHAR(20) NOT NULL,
                 complemento VARCHAR(40),
                 bairro VARCHAR(40) NOT NULL,
                 cidade VARCHAR(40) NOT NULL,
                 uf VARCHAR(2) NOT NULL,
                 cep VARCHAR(8) NOT NULL,
                 ddd VARCHAR(4),
                 telefone VARCHAR(20),
                 fax VARCHAR(20),
                 email VARCHAR(255),
                 representante_legal VARCHAR(50) NOT NULL,
                 cargo_representante VARCHAR(40) NOT NULL,
                 regiao_operacao INT,
                 data_registro DATE NOT NULL
             )
         """)
        connection.commit()
        crs.close()
        logging.info("Table created successfully")
    except Error as e:
        logging.error(e)


def parse_date(date_str):
    for fmt in ('%Y-%m-%d', '%d/%m/%Y'):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            pass
    raise ValueError(f"Date format for {date_str} is not supported")

with open("../data/Relatorio_cadop.csv", mode='r', encoding='utf-8') as file:
    create_table(con)
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)  # Skip the header
    logging.info("Skipping the header")
    cursor = con.cursor()
    for row in csv_reader:
        cursor.execute("""
            INSERT INTO operadoras (registro_ans,cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, email, representante_legal, cargo_representante, regiao_operacao, data_registro)
            VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)
        """, (
        row[0],row[1], row[2], row[3], row[4] if row[4] else None, row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18] if row[18] else None, parse_date(row[19])))
        con.commit()
    cursor.close()
    con.close()

    logging.info("All data inserted successfully in table operadoras")