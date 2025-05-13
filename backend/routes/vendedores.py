from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelo.ModeloVendedor import ModeloVendedor
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

@router.get("/vendedores/{id}", response_model=VendedorBase)
def buscar_vendedor(id: int, db: Session = Depends(get_db)):
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.id == id).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.delete("/vendedores/{id}")
def remover_vendedor(id: int, db: Session = Depends(get_db)):
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.id == id).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    db.delete(vendedor)
    db.commit()
    return {"message": "Vendedor removido com sucesso!"}