CREATE DATABASE IF NOT EXISTS intuitive_care CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE intuitive_care;

CREATE TABLE IF NOT EXISTS demos_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dateTime DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao_conta VARCHAR(255) NOT NULL,
    vl_saldo_inicial DECIMAL(20,2) NOT NULL,
    vl_debito DECIMAL(20,2)
);

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
);