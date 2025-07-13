from pydantic import BaseModel
from typing import Optional
from datetime import date


# ========================
# Cliente Schemas
# ========================

class ClienteBase(BaseModel):
    cpf: str
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None

    class Config:
        orm_mode = True

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None


# ========================
# Vendedor Schemas
# ========================

class VendedorBase(BaseModel):
    cpf: str
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None
    comissao_percentual: float

    class Config:
        orm_mode = True

class VendedorCreate(VendedorBase):
    pass

class VendedorResponse(BaseModel):
    cpf: str
    nome: str
    comissao_percentual: float

    class Config:
        orm_mode = True


# ========================
# Produto Schemas
# ========================

class ProdutoBase(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    estoque: int

    class Config:
        orm_mode = True

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    estoque: int

class ProdutoResponse(BaseModel):
    id: Optional[int]
    nome: str
    preco: float

    class Config:
        orm_mode = True


# ========================
# Venda Schemas
# ========================

class VendaBase(BaseModel):
    id: Optional[int] = None
    data: date
    cliente_cpf: str
    vendedor_cpf: str
    produto_id: int
    quantidade: int = 1
    total: Optional[float] = None
    comissao: Optional[float] = None

    class Config:
        orm_mode = True

class VendaCreate(BaseModel):
    data: date
    cliente_cpf: str
    vendedor_cpf: str
    produto_id: int
    quantidade: int = 1

    class Config:
        orm_mode = True

class VendaResponse(BaseModel):
    id: int
    data: date
    quantidade: int
    total: float
    comissao: float
    cliente: ClienteResponse
    produto: ProdutoResponse
    vendedor: VendedorResponse

    class Config:
        orm_mode = True
