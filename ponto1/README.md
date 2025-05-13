# Sistema de Vendas de Cosméticos

Link para o repositorio de OO: [aqui](ttps://github.com/anabfs/OO/tree/master/Trabalho%205)

## Diagrama

![Diagrama](/ponto1/assets/img.png)

## Histórias de Usuario

 Usuário: Gerente / Atendente / Vendedor

### HU01 - Cadastro de Produtos

**Como** gerente da loja
**Quero** cadastrar novos produtos com suas características (nome, marca, tipo, preço)
**Para** que estejam disponíveis para venda

**Critérios de Aceitação:**

- [ ] O sistema deve permitir inserir nome, marca, tipo e preço
- [ ] O produto deve ser persistido no banco de dados
- [ ] O produto deve estar visível no catálogo de vendas

---

### HU02 - Cadastro de Cliente

**Como** atendente
**Quero** cadastrar os dados dos clientes (nome, CPF, telefone, e-mail)
**Para** poder associá-los às vendas

**Critérios de Aceitação:**

- [ ] Todos os campos devem ser obrigatórios
- [ ] CPF deve ser único e válido
- [ ] Dados devem ser persistidos corretamente

---

### HU03 - Cadastro de Vendedor

**Como** administrador
**Quero** cadastrar vendedores no sistema
**Para** registrar corretamente quem realizou cada venda

**Critérios de Aceitação:**

- [ ] Campos obrigatórios: nome, matrícula, comissão
- [ ] Comissão deve ser um percentual numérico
- [ ] ID do vendedor deve ser único

---

### HU04 - Realizar Venda

**Como** vendedor
**Quero** registrar uma venda incluindo cliente, itens e quantidades
**Para** gerar o total e calcular a comissão

**Critérios de Aceitação:**

- [ ] Selecionar cliente e vendedor
- [ ] Adicionar múltiplos produtos com quantidades
- [ ] Total e comissão calculados automaticamente

---

### HU05 - Visualizar Histórico de Vendas

**Como** gerente
**Quero** acessar o histórico de vendas por data, cliente ou vendedor
**Para** analisar o desempenho da loja

**Critérios de Aceitação:**

- [ ] Filtro por data, cliente e vendedor
- [ ] Exibir total e comissão em cada venda
- [ ] Possível exportar para CSV

---

### HU06 - Calcular Comissão de Vendedor

**Como** gerente
**Quero** que o sistema calcule automaticamente a comissão do vendedor
**Para** garantir justiça e motivação

**Critérios de Aceitação:**

- [ ] Percentual deve vir do cadastro do vendedor
- [ ] Comissão calculada com base no valor total da venda
- [ ] Mostrar valor da comissão na nota da venda

---

### HU07 - Atualizar Preço de Produto

**Como** gerente
**Quero** poder atualizar o preço de um produto
**Para** refletir mudanças no custo ou na política comercial

**Critérios de Aceitação:**

- [ ] Preço deve ser atualizado sem alterar o histórico de vendas anteriores
- [ ] Deve haver controle de versão ou log da alteração

---

### HU08 - Remover Produto do Catálogo

**Como** gerente
**Quero** poder desativar ou excluir produtos que não são mais vendidos
**Para** manter o catálogo limpo

**Critérios de Aceitação:**

- [ ] Produto desativado não deve aparecer para clientes
- [ ] Produto não pode ser excluído se houver vendas associadas

---

### HU9 - Emitir Relatório de Vendas por Cliente

**Como** administrador
**Quero** gerar relatórios com todas as vendas de um cliente
**Para** fins de controle e fidelização

**Critérios de Aceitação:**

- [ ] Relatório deve incluir datas, produtos e total de cada venda
- [ ] Exportável em PDF ou CSV

## Banco de Dados

### Scripts para teste

Popula

```
USE sistema_vendas;

INSERT INTO cliente (cpf, nome, email) VALUES
('123.456.789-00', 'Ana Beatriz', 'ana@example.com'),
('987.654.321-00', 'Carlos Souza', 'carlos@example.com');

INSERT INTO vendedor (nome, percentual_comissao) VALUES
('João Vendas', 10.0),
('Maria Vendedora', 10.0);

INSERT INTO produto (nome, preco, tipo_produto) VALUES
('Perfume A', 120.00, 'perfume'),
('Desodorante B', 25.00, 'desodorante'),
('Hidratante C', 45.00, 'hidratante');

INSERT INTO venda (data, cliente_cpf, vendedor_id, total, comissao) VALUES
(CURRENT_DATE, '123.456.789-00', 1, 140.00, 14.00);

INSERT INTO item_venda (venda_id, produto_id, quantidade, preco_unitario, subtotal) VALUES
(1, 1, 1, 120.00, 120.00),
(1, 2, 1, 20.00, 20.00);

```

Consulta

```
USE sistema_vendas;

SELECT
  v.id AS venda_id,
  v.data,
  c.nome AS cliente,
  vd.nome AS vendedor,
  p.nome AS produto,
  iv.quantidade,
  iv.preco_unitario,
  iv.subtotal,
  v.total,
  v.comissao
FROM venda v
JOIN cliente c ON v.cliente_cpf = c.cpf
JOIN vendedor vd ON v.vendedor_id = vd.id
JOIN item_venda iv ON v.id = iv.venda_id
JOIN produto p ON iv.produto_id = p.id
WHERE v.id = 1;
```
