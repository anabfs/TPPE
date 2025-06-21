from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.item_model import ModeloItemVenda
from database import get_db
from schemas import ItemVendaCreate, ItemVendaBase

router = APIRouter()

@router.get("/itens-venda", response_model=list[ItemVendaBase])
def listar_itens_venda(db: Session = Depends(get_db)):
    return db.query(ModeloItemVenda).all()

@router.post("/itens-venda", response_model=ItemVendaBase)
def adicionar_item_venda(item_venda: ItemVendaCreate, db: Session = Depends(get_db)):
    novo_item = ModeloItemVenda(**item_venda.dict())
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return novo_item

@router.get("/itens-venda/{item_id}", response_model=ItemVendaBase)
def buscar_item_venda(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ModeloItemVenda).filter(ModeloItemVenda.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item de venda não encontrado")
    return item

@router.delete("/itens-venda/{item_id}")
def remover_item_venda(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ModeloItemVenda).filter(ModeloItemVenda.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item de venda não encontrado")
    db.delete(item)
    db.commit()
    return {"message": "Item de venda removido com sucesso!"}