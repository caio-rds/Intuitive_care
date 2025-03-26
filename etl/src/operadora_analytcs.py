import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='', database='intuitive_care')
cursor = db.cursor()


def get_operadoras(query: str):
    cursor.execute(query)
    return cursor.fetchall()



print(get_operadoras("""
            SELECT reg_ans, SUM(vl_debito) AS total_vl_debito
            FROM demos_contabeis
            WHERE descricao_conta LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
            AND dateTime >= '2024-10-01'
            GROUP BY reg_ans
            ORDER BY total_vl_debito DESC LIMIT 10;
        """))


print(get_operadoras("""
            SELECT reg_ans, SUM(vl_debito) AS total_vl_debito
            FROM demos_contabeis
            WHERE descricao_conta LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
            AND dateTime >= '2024-01-01'
            GROUP BY reg_ans
            ORDER BY total_vl_debito DESC LIMIT 10;
        """))