from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.venda_model import ModeloVenda
from models.cliente_model import ModeloCliente
from models.vendedor_model import ModeloVendedor
from database import get_db
from schemas import VendaCreate, VendaBase

router = APIRouter()

@router.get("/vendas", response_model=list[VendaBase])
def listar_vendas(db: Session = Depends(get_db)):
    return db.query(ModeloVenda).all()

@router.post("/vendas", response_model=VendaBase)
def adicionar_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    cliente = db.query(ModeloCliente).filter(ModeloCliente.cpf == venda.cliente_cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.id == venda.vendedor_id).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    nova_venda = ModeloVenda(
        data=venda.data,
        cliente_cpf=venda.cliente_cpf,
        vendedor_id=venda.vendedor_id,
        total=0.00,
        comissao=0.00
    )
    db.add(nova_venda)
    db.commit()
    nova_venda.comissao = nova_venda.total * (vendedor.comissao_percentual / 100)
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