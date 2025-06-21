from fastapi import FastAPI
from routes import clientes, vendedores, produtos, vendas, itens_venda

app = FastAPI()

app.include_router(clientes, prefix="/clientes", tags=["Clientes"])
app.include_router(vendedores, prefix="/vendedores", tags=["Vendedores"])
app.include_router(produtos, prefix="/produtos", tags=["Produtos"])
app.include_router(vendas, prefix="/vendas", tags=["Vendas"])
app.include_router(itens_venda, prefix="/itens-venda", tags=["Itens de Venda"])

@app.get("/")
def root():
    return {"message": "Sistema de Vendas API"}