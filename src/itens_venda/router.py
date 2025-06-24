from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from itens_venda.model import ModeloItemVenda
from produto.model import ModeloProduto
from venda.model import ModeloVenda
from vendedor.model import ModeloVendedor
from database import get_db
from schemas import ItemVendaCreate, ItemVendaBase

router = APIRouter()

@router.get("/itens-venda", response_model=list[ItemVendaBase])
def listar_itens_venda(db: Session = Depends(get_db)):
    return db.query(ModeloItemVenda).all()

@router.post("/itens-venda", response_model=ItemVendaBase)
def adicionar_item_venda(item_venda: ItemVendaCreate, db: Session = Depends(get_db)):
    produto = db.query(ModeloProduto).filter(ModeloProduto.id == item_venda.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    venda = db.query(ModeloVenda).filter(ModeloVenda.id == item_venda.venda_id).first()
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    novo_item = ModeloItemVenda(
        venda_id=item_venda.venda_id,
        produto_id=item_venda.produto_id,
        quantidade=item_venda.quantidade
    )
    db.add(novo_item)

    venda.total += produto.preco * item_venda.quantidade
    venda.comissao = venda.total * (db.query(ModeloVendedor).filter(ModeloVendedor.id == venda.vendedor_id).first().comissao_percentual / 100)
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

    produto = db.query(ModeloProduto).filter(ModeloProduto.id == item.produto_id).first()
    venda = db.query(ModeloVenda).filter(ModeloVenda.id == item.venda_id).first()

    venda.total -= produto.preco * item.quantidade
    venda.comissao = venda.total * (db.query(ModeloVendedor).filter(ModeloVendedor.id == venda.vendedor_id).first().comissao_percentual / 100)

    db.delete(item)
    db.commit()
    return {"message": "Item de venda removido com sucesso!"}