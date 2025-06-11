from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.ModeloCliente import ModeloCliente
from database import get_db
from schemas import ClienteCreate, ClienteResponse

router = APIRouter()

@router.get("/clientes", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    """
    Lista todos os clientes cadastrados no banco de dados.
    """
    return db.query(ModeloCliente).all()

@router.post("/clientes", response_model=ClienteResponse)
def adicionar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    """
    Adiciona um novo cliente ao banco de dados.
    """
    novo_cliente = ModeloCliente(**cliente.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

@router.get("/clientes/{cpf}", response_model=ClienteResponse)
def buscar_cliente(cpf: str, db: Session = Depends(get_db)):
    """
    Busca um cliente pelo CPF.
    """
    cliente = db.query(ModeloCliente).filter(ModeloCliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.delete("/clientes/{cpf}")
def remover_cliente(cpf: str, db: Session = Depends(get_db)):
    """
    Remove um cliente pelo CPF.
    """
    cliente = db.query(ModeloCliente).filter(ModeloCliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(cliente)
    db.commit()
    return {"message": "Cliente removido com sucesso!"}