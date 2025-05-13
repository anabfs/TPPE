from fastapi import FastAPI
from routes import clientes, vendedores, produtos, vendas, itens_venda

app = FastAPI()

app.include_router(clientes.router, prefix="/api")
app.include_router(vendedores.router, prefix="/api")
app.include_router(produtos.router, prefix="/api")
app.include_router(vendas.router, prefix="/api")
app.include_router(itens_venda.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Sistema de Vendas API"}