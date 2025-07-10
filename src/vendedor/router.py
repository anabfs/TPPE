from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from vendedor.model import ModeloVendedor
from database import get_db
from schemas import VendedorCreate, VendedorBase

router = APIRouter()

@router.get("/vendedores", response_model=list[VendedorBase])
def listar_vendedores(db: Session = Depends(get_db)):
    """
    Lista todos os vendedores cadastrados no banco de dados.
    """
    return db.query(ModeloVendedor).all()

@router.post("/vendedores", response_model=VendedorBase)
def adicionar_vendedor(vendedor: VendedorCreate, db: Session = Depends(get_db)):
    """
    Adiciona um novo vendedor ao banco de dados.
    """
    novo_vendedor = ModeloVendedor(**vendedor.dict())
    db.add(novo_vendedor)
    db.commit()
    db.refresh(novo_vendedor)
    return novo_vendedor

@router.get("/vendedores/{vendedor_cpf}", response_model=VendedorBase)
def buscar_vendedor(vendedor_cpf: str, db: Session = Depends(get_db)):
    """
    Busca um vendedor pelo CPF.
    """
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.cpf == vendedor_cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.put("/vendedores/{vendedor_cpf}", response_model=VendedorBase)
def atualizar_vendedor(vendedor_cpf: str, vendedor_update: VendedorCreate, db: Session = Depends(get_db)):
    """
    Atualiza os dados de um vendedor existente.
    """
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.cpf == vendedor_cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    for chave, valor in vendedor_update.dict(exclude_unset=True).items():
        setattr(vendedor, chave, valor)
    
    db.commit()
    db.refresh(vendedor)
    return vendedor

@router.delete("/vendedores/{vendedor_cpf}")
def remover_vendedor(vendedor_cpf: str, db: Session = Depends(get_db)):
    """
    Remove um vendedor pelo CPF.
    """
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.cpf == vendedor_cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    db.delete(vendedor)
    db.commit()
    return {"message": "Vendedor removido com sucesso!"}