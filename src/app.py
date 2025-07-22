from fastapi import FastAPI
from cliente.router import router as clientes
from vendedor.router import router as vendedores
from produto.router import router as produtos
from venda.router import router as vendas
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(clientes, prefix="/clientes", tags=["Clientes"])
app.include_router(vendedores, prefix="/vendedores", tags=["Vendedores"])
app.include_router(produtos, prefix="/produtos", tags=["Produtos"])
app.include_router(vendas, prefix="/vendas", tags=["Vendas"])

@app.get("/")
def root():
    return {"message": "Sistema de Vendas API"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, use o domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
