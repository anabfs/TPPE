from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String, Float

class ModeloProduto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
