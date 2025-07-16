from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class ModeloVenda(Base):
    __tablename__ = "venda"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    cliente_cpf = Column(String, ForeignKey("cliente.cpf"), nullable=False)
    vendedor_cpf = Column(String, ForeignKey("vendedor.cpf"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    total = Column(Float, nullable=False, default=0.00)
    comissao = Column(Float, nullable=False, default=0.00)
    quantidade = Column(Integer, nullable=False, default=1)

    cliente = relationship("ModeloCliente", backref="vendas")
    vendedor = relationship("ModeloVendedor", backref="vendas")
    produto = relationship("ModeloProduto", backref="vendas")