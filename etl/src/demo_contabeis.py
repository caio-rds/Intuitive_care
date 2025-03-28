import logging
import os
from datetime import datetime
import mysql.connector
import csv
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="intuitive_care"
        )
        logging.info("Connection to MySQL DB successful")
    except Error as e:
        logging.error(f"The error '{e}' occurred")

    return connection

db = create_connection()
cursor = db.cursor()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


data_dir = '../data/financial'


def parse_date(date_str):
    for fmt in ('%Y-%m-%d', '%d/%m/%Y'):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            pass
    raise ValueError(f"Date format for {date_str} is not supported")




def transform_and_insert(filename_p):
    try:
        data_to_insert = []
        cursor = db.cursor()
        with open(f"{data_dir}/{filename_p}", mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)  # Skip the header
            for index, row in enumerate(csv_reader):
                # Skip rows where all values are null

                if all(not cell for cell in row):
                    continue

                print(f"Processing row {index} in {filename}")
                data_to_insert.append((
                    parse_date(row[0]),
                    row[1],
                    row[2],
                    row[3],
                    float(row[4].replace(',', '.')) if row[4] else 0,
                    float(row[5].replace(',', '.')) if row[5] else 0
                ))

            cursor.executemany(
                "INSERT INTO demos_contabeis (dateTime, reg_ans, cd_conta_contabil, descricao_conta, vl_saldo_inicial, vl_debito) VALUES (%s, %s, %s, %s, %s, %s)",
                data_to_insert
            )
            db.commit()
            file.close()
            cursor.close()
    except Error as e:
        logging.error(f"Error processing row {index}: {e}")
        if e.errno == 2013:  # Lost connection to MySQL server during query
            logging.error("Reconnecting to MySQL server...")
            create_connection()



for filename in os.listdir(data_dir):
    if filename.endswith('.csv'):
        transform_and_insert(filename)

logging.info("All CSV files have been processed and inserted into the database.")