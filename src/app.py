from fastapi import FastAPI
from cliente.router import router as clientes
from vendedor.router import router as vendedores
from produto.router import router as produtos
from venda.router import router as vendas
from itens_venda.router import router as itens_venda

app = FastAPI()

app.include_router(clientes, prefix="/clientes", tags=["Clientes"])
app.include_router(vendedores, prefix="/vendedores", tags=["Vendedores"])
app.include_router(produtos, prefix="/produtos", tags=["Produtos"])
app.include_router(vendas, prefix="/vendas", tags=["Vendas"])
app.include_router(itens_venda, prefix="/itens-venda", tags=["Itens de Venda"])

@app.get("/")
def root():
    return {"message": "Sistema de Vendas API"}