from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ModeloItemVenda(Base):
    __tablename__ = "item_venda"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    venda_id = Column(Integer, ForeignKey("venda.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)

    venda = relationship("ModeloVenda", back_populates="itens_venda")
    produto = relationship("ModeloProduto")