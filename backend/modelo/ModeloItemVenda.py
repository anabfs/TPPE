from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ModeloItemVenda(Base):
    __tablename__ = "item_venda"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    venda_id = Column(Integer, ForeignKey("venda.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    venda = relationship("ModeloVenda")
    produto = relationship("ModeloProduto")