from sqlalchemy import Column, Integer, String, Float
from database import Base

class ModeloVendedor(Base):
    __tablename__ = "vendedor"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    comissao_percentual = Column(Float, nullable=False)