LOAD DATA INFILE '/var/lib/mysql-files/financial/1T2023.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');

LOAD DATA INFILE '/var/lib/mysql-files/financial/1T2024.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');



LOAD DATA INFILE '/var/lib/mysql-files/financial/2T2023.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');

LOAD DATA INFILE '/var/lib/mysql-files/financial/2T2024.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');



LOAD DATA INFILE '/var/lib/mysql-files/financial/3T2023.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');

LOAD DATA INFILE '/var/lib/mysql-files/financial/3T2024.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');



LOAD DATA INFILE '/var/lib/mysql-files/financial/4T2023.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');

LOAD DATA INFILE '/var/lib/mysql-files/financial/4T2024.csv'
INTO TABLE demos_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@date_str, reg_ans, cd_conta_contabil, descricao_conta, @vl_saldo_inicial, @vl_debito)
SET
    dateTime = CASE
        WHEN @date_str LIKE '%/%/%' THEN STR_TO_DATE(@date_str, '%d/%m/%Y')
        WHEN @date_str LIKE '%-%-%' THEN STR_TO_DATE(@date_str, '%Y-%m-%d')
        ELSE NULL
    END,
    vl_saldo_inicial = NULLIF(REPLACE(@vl_saldo_inicial, ',', '.'), ''),
    vl_debito = NULLIF(REPLACE(@vl_debito, ',', '.'), '');



