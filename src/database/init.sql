-- Tabela cliente
CREATE TABLE cliente (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(15)
);
-- Tabela vendedor
CREATE TABLE vendedor (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(15),
    comissao_percentual NUMERIC(5, 2) NOT NULL
);
-- Tabela produto
CREATE TABLE produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    estoque INTEGER NOT NULL DEFAULT 0
);
-- Tabela venda
CREATE TABLE venda (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    cliente_cpf VARCHAR(14) NOT NULL,
    vendedor_cpf VARCHAR(14) NOT NULL,
    produto_id INTEGER NOT NULL,
    total NUMERIC(10, 2) DEFAULT 0.00,
    comissao NUMERIC(10, 2) DEFAULT 0.00,
    quantidade INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf),
    FOREIGN KEY (vendedor_cpf) REFERENCES vendedor(cpf),
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);