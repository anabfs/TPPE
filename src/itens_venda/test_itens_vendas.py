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

@pytest.mark.usefixtures("novo_cliente")
def novo_cliente():
    """
    Cria um cliente antes do teste e remove após.
    """
    # Apaga se já existir
    client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")
    # Cria cliente
    response = client.post("/clientes/clientes", json=cliente_exemplo)
    assert response.status_code == 200
    yield cliente_exemplo
    # Apaga todas as vendas do cliente
    vendas = client.get("/vendas/vendas").json()
    for venda in vendas:
        if venda["cliente_cpf"] == cliente_exemplo["cpf"]:
            client.delete(f"/vendas/vendas/{venda['id']}")
    client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")

@pytest.fixture 
def nova_venda():
    """
    Cria uma venda e retorna seu ID.
    """
    response = client.post("/vendas/vendas", json={
        "data": "2023-10-01",
        "cliente_cpf": novo_cliente["cpf"],
        "vendedor_id": 4
    })
    assert response.status_code == 200, f"Erro ao criar venda: {response.text}"
    venda = response.json()
    venda_id = venda.get("id")
    assert venda_id is not None, f"ID da venda ausente: {venda}"
    return venda_id

@pytest.fixture
def test_adicionar_item_venda(nova_venda):# pylint: disable=redefined-outer-name
    """
    Testa o endpoint de adicionar item à venda.
    """
    response = client.post("/itens-venda/itens-venda", json={
        "venda_id": nova_venda["venda_id"],
        "produto_id": 4,
        "quantidade": 2
    })
    assert response.status_code == 200, f"Erro ao adicionar item: {response.text}"
    item = response.json()
    assert item["venda_id"] == nova_venda
    assert item["produto_id"] == 4
    assert item["quantidade"] == 2
