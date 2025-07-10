from sqlalchemy import Column, String, Float
from database import Base

class ModeloVendedor(Base):
    __tablename__ = "vendedor"

    cpf = Column(String, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
    comissao_percentual = Column(Float, nullable=False)
