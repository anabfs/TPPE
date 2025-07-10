CREATE DATABASE IF NOT EXISTS sistema_vendas;
USE sistema_vendas;
CREATE TABLE cliente (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(15)
);
CREATE TABLE vendedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    comissao_percentual DECIMAL(5, 2) NOT NULL
);
CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);
CREATE TABLE venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    cliente_cpf VARCHAR(14) NOT NULL,
    vendedor_id INT NOT NULL,
    total DECIMAL(10, 2) DEFAULT 0.00,
    comissao DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf),
    FOREIGN KEY (vendedor_id) REFERENCES vendedor(id)
);