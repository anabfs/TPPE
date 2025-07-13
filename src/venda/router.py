from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from venda.model import ModeloVenda
from cliente.model import ModeloCliente
from vendedor.model import ModeloVendedor
from produto.model import ModeloProduto
from database import get_db
from schemas import VendaCreate, VendaBase
from sqlalchemy.orm import joinedload
import schemas

router = APIRouter()

@router.get("/vendas", response_model=list[schemas.VendaResponse])
def listar_vendas(db: Session = Depends(get_db)):
    vendas = db.query(ModeloVenda).all()
    return vendas


@router.post("/vendas", response_model=VendaBase)
def adicionar_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    cliente = db.query(ModeloCliente).filter(ModeloCliente.cpf == venda.cliente_cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    vendedor = db.query(ModeloVendedor).filter(ModeloVendedor.cpf == venda.vendedor_cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")

    produto = db.query(ModeloProduto).filter(ModeloProduto.id == venda.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if produto.estoque < venda.quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente para esta venda")

    produto.estoque -= venda.quantidade

    total_venda = produto.preco * venda.quantidade
    comissao = total_venda * (vendedor.comissao_percentual / 100)

    nova_venda = ModeloVenda(
        data=venda.data,
        cliente_cpf=venda.cliente_cpf,
        vendedor_cpf=venda.vendedor_cpf,
        produto_id=venda.produto_id,
        quantidade=venda.quantidade,
        total=total_venda,
        comissao=comissao
    )

    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)

    return nova_venda

@router.get("/vendas/{venda_id}", response_model=schemas.VendaResponse)
def buscar_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = db.query(ModeloVenda)\
        .options(
            joinedload(ModeloVenda.cliente),
            joinedload(ModeloVenda.vendedor),
            joinedload(ModeloVenda.produto),
        )\
        .filter(ModeloVenda.id == venda_id)\
        .first()

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

@router.get("/vendas/cliente/{cpf}", response_model=list[schemas.VendaResponse])
def listar_vendas_por_cliente(cpf: str, db: Session = Depends(get_db)):
    vendas = db.query(ModeloVenda)\
        .options(
            joinedload(ModeloVenda.cliente),
            joinedload(ModeloVenda.vendedor),
            joinedload(ModeloVenda.produto),
        )\
        .filter(ModeloVenda.cliente_cpf == cpf)\
        .all()

    if not vendas:
        raise HTTPException(status_code=404, detail="Nenhuma venda encontrada para este CPF")

    return vendas
