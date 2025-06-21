from sqlalchemy import Column, String
from database import Base

class ModeloCliente(Base):
    __tablename__ = "cliente"

    cpf = Column(String, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
