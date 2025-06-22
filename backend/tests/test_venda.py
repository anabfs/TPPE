import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

cliente_exemplo = {
    "cpf": "12345678900",
    "nome": "Cliente Teste",
    "email": "cliente@teste.com",
    "telefone": "123456789"
}

@pytest.fixture
def novo_cliente():
    """
    Fixture para criar um cliente antes do teste e removê-lo após o teste.
    """
    response = client.post("/clientes/clientes", json=cliente_exemplo)
    assert response.status_code == 200
    yield response
    # Remover todas as vendas associadas ao cliente antes de deletá-lo
    vendas_response = client.get("/vendas/vendas")
    vendas = vendas_response.json()
    for venda in vendas:
        if venda["cliente_cpf"] == cliente_exemplo["cpf"]:
            client.delete(f"/vendas/vendas/{venda['id']}")
    client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")

def test_criar_venda(novo_cliente):
    """
    Testa o endpoint POST /vendas para adicionar uma venda.
    """
    response = client.post("/vendas/vendas", json={
        "data": "2023-10-01",
        "cliente_cpf": cliente_exemplo["cpf"],
        "vendedor_id": 4  # Vendedor já existente
    })
    assert response.status_code == 200
    venda = response.json()
    assert venda["cliente_cpf"] == cliente_exemplo["cpf"]
    assert venda["vendedor_id"] == 4
    assert venda["total"] == 0.00
    assert venda["comissao"] == 0.00

def test_listar_vendas():
    """
    Testa o endpoint GET /vendas para listar vendas.
    """
    response = client.get("/vendas/vendas")
    assert response.status_code == 200
    vendas = response.json()
    assert isinstance(vendas, list)