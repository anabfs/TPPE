from database import Base, engine
from modelo.ModeloCliente import ModeloCliente
from modelo.ModeloVendedor import ModeloVendedor
from modelo.ModeloProduto import ModeloProduto
from modelo.ModeloVenda import ModeloVenda
from modelo.ModeloItemVenda import ModeloItemVenda

# Cria as tabelas no banco de dados
print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")