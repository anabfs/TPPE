from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelo.ModeloVenda import ModeloVenda
from database import get_db
from schemas import VendaCreate, VendaBase

router = APIRouter()

@router.get("/vendas", response_model=list[VendaBase])
def listar_vendas(db: Session = Depends(get_db)):
    return db.query(ModeloVenda).all()

@router.post("/vendas", response_model=VendaBase)
def adicionar_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    nova_venda = ModeloVenda(**venda.dict())
    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)
    return nova_venda

@router.get("/vendas/{venda_id}", response_model=VendaBase)
def buscar_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = db.query(ModeloVenda).filter(ModeloVenda.id == venda_id).first()
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return venda

@router.delete("/vendas/{venda_id}")
def remover_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = db.query(ModeloVenda).filter(ModeloVenda.id == venda_id).first()
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    db.delete(venda)
    db.commit()
    return {"message": "Venda removida com sucesso!"}