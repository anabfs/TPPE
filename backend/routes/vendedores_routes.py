from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.vendedor_model import ModeloVendedor
from database import get_db
from schemas import VendedorCreate, VendedorBase

router = APIRouter()

@router.get("/vendedores", response_model=list[VendedorBase])
def listar_vendedores(db: Session = Depends(get_db)):
    return db.query(ModeloVendedor).all()

@router.post("/vendedores", response_model=VendedorBase)
def adicionar_vendedor(vendedor: VendedorCreate, db: Session = Depends(get_db)):
    novo_vendedor = ModeloVendedor(**vendedor.dict())
    db.add(novo_vendedor)
    db.commit()
    db.refresh(novo_vendedor)
    return novo_vendedor

@router.get("/vendedores/{vendedor_id}", response_model=VendedorBase)
def buscar_vendedor(vendedor_id: int, db: Session = Depends(get_db)):
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.id == vendedor_id).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.delete("/vendedores/{vendedor_id}")
def remover_vendedor(vendedor_id: int, db: Session = Depends(get_db)):
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.id == vendedor_id).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    db.delete(vendedor)
    db.commit()
    return {"message": "Vendedor removido com sucesso!"}