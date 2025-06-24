from pydantic import BaseModel
from typing import Optional
from datetime import date

class ClienteBase(BaseModel):
    cpf: str
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    class Config:
        orm_mode = True

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str]
class VendedorBase(BaseModel):
    id: int
    nome: str
    comissao_percentual: float

    class Config:
        orm_mode = True

class VendedorCreate(BaseModel):
    nome: str
    comissao_percentual: float

class ProdutoBase(BaseModel):
    id: Optional[int] = None
    nome: str
    categoria: str
    preco: float

    class Config:
        orm_mode = True

class ProdutoCreate(BaseModel):
    nome: str
    categoria: str
    preco: float

class VendaBase(BaseModel):
    id: Optional[int] = None
    data: date
    cliente_cpf: str
    vendedor_id: int
    total: Optional[float] = None
    comissao: Optional[float] = None

    class Config:
        orm_mode = True

class VendaCreate(BaseModel):
    data: date
    cliente_cpf: str
    vendedor_id: int

    class Config:
        orm_mode = True

class ItemVendaBase(BaseModel):
    id: int
    venda_id: int
    produto_id: int
    quantidade: int

    class Config:
        orm_mode = True

class ItemVendaCreate(BaseModel):
    venda_id: int
    produto_id: int
    quantidade: int