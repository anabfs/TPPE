from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class ModeloVenda(Base):
    __tablename__ = "venda"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    data = Column(Date, nullable=False)
    cliente_cpf = Column(String(14), ForeignKey("cliente.cpf"), nullable=False)
    vendedor_id = Column(Integer, ForeignKey("vendedor.id"), nullable=False)
    total = Column(Float, nullable=True)
    comissao = Column(Float, nullable=True)

    cliente = relationship("ModeloCliente")
    vendedor = relationship("ModeloVendedor")