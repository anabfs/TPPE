import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

cliente_exemplo = {
    "cpf": "12345678900",
    "nome": "João da Silva",
    "email": "joao@example.com",
    "telefone": "11999999999"
}

@pytest.fixture
def novo_cliente():
    """
    Fixture para criar um cliente antes do teste e removê-lo após o teste.
    """
    response = client.post("/clientes/clientes", json=cliente_exemplo)
    assert response.status_code == 200
    yield response
    client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")

def test_adicionar_cliente():
    """
    Testa o endpoint POST /clientes para adicionar um cliente.
    """
    response = client.post("/clientes/clientes", json=cliente_exemplo)
    assert response.status_code == 200
    assert response.json()["cpf"] == cliente_exemplo["cpf"]
    assert response.json()["nome"] == cliente_exemplo["nome"]
    client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")  # Cleanup

@pytest.mark.usefixtures("novo_cliente")
def test_listar_clientes():
    """
    Testa o endpoint GET /clientes para listar clientes.
    """
    response = client.get("/clientes/clientes")
    assert response.status_code == 200
    assert any(cliente["cpf"] == cliente_exemplo["cpf"] for cliente in response.json())

@pytest.mark.usefixtures("novo_cliente")
def test_buscar_cliente():
    """
    Testa o endpoint GET /clientes/{cpf} para buscar um cliente pelo CPF.
    """
    response = client.get(f"/clientes/clientes/{cliente_exemplo['cpf']}")
    assert response.status_code == 200
    assert response.json()["cpf"] == cliente_exemplo["cpf"]

@pytest.mark.usefixtures("novo_cliente")
def test_atualizar_cliente():
    """
    Testa o endpoint PUT /clientes/{cpf} para atualizar um cliente.
    """
    novo_dado = {"telefone": "11888888888"}
    response = client.put(f"/clientes/clientes/{cliente_exemplo['cpf']}", json=novo_dado)
    assert response.status_code == 200
    assert response.json()["telefone"] == novo_dado["telefone"]

def test_remover_cliente():
    """
    Testa o endpoint DELETE /clientes/{cpf} para remover um cliente.
    """
    client.post("/clientes/clientes", json=cliente_exemplo)
    response = client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Cliente removido com sucesso!"