from sqlalchemy import Column, String
from database import Base

class ModeloCliente(Base):
    __tablename__ = "cliente"

    cpf = Column(String(14), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100))
    telefone = Column(String(15))