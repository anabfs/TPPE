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
    id: Optional[int] = None
    nome: str
    comissao_percentual: float

    class Config:
        orm_mode = True

class VendedorCreate(VendedorBase):
    pass

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

class VendaCreate(VendaBase):
    pass

class ItemVendaBase(BaseModel):
    id: Optional[int] = None
    venda_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float
    subtotal: float

    class Config:
        orm_mode = True

class ItemVendaCreate(ItemVendaBase):
    pass