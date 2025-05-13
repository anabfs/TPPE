from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelo.ModeloProduto import ModeloProduto
from database import get_db
from schemas import ProdutoCreate, ProdutoBase

router = APIRouter()

@router.get("/produtos", response_model=list[ProdutoBase])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ModeloProduto).all()

@router.post("/produtos", response_model=ProdutoBase)
def adicionar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ModeloProduto(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@router.get("/produtos/{id}", response_model=ProdutoBase)
def buscar_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(ModeloProduto).filter(ModeloProduto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.delete("/produtos/{id}")
def remover_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(ModeloProduto).filter(ModeloProduto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
    return {"message": "Produto removido com sucesso!"}