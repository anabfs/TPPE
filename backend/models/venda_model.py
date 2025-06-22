from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ModeloVenda(Base):
    __tablename__ = "venda"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    cliente_cpf = Column(String, ForeignKey("cliente.cpf"), nullable=False)
    vendedor_id = Column(Integer, ForeignKey("vendedor.id"), nullable=False)
    total = Column(Float, nullable=False, default=0.00)
    comissao = Column(Float, nullable=False, default=0.00)

    itens_venda = relationship("ModeloItemVenda", back_populates="venda")