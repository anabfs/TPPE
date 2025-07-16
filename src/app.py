from fastapi import FastAPI
from cliente.router import router as clientes
from vendedor.router import router as vendedores
from produto.router import router as produtos
from venda.router import router as vendas
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine  

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
allow_origins=[
    "http://localhost:3000",  # Front local
    "https://sistema-vendas-front.vercel.app",  # Front em produção
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
