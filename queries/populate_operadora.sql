LOAD DATA INFILE '/var/lib/mysql-files/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro,
 numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, email,
 representante_legal, cargo_representante, @regiao_operacao, data_registro)
SET regiao_operacao = NULLIF(@regiao_operacao, '');

UPDATE operadoras
SET data_registro =
    CASE
        WHEN STR_TO_DATE(data_registro, '%Y-%m-%d') IS NOT NULL
        THEN STR_TO_DATE(data_registro, '%Y-%m-%d')
        ELSE STR_TO_DATE(data_registro, '%d/%m/%Y')
    END;