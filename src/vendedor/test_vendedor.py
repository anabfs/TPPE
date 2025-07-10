import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Vendedor de exemplo
vendedor_exemplo = {
    "cpf": "12345678901",
    "nome": "João Vendedor",
    "email": "joao@email.com",
    "telefone": "11999999999",
    "comissao_percentual": 10.5
}

@pytest.fixture
def novo_vendedor():
    """
    Fixture para criar um vendedor antes do teste e removê-lo após o teste.
    """
    response = client.post("/vendedores/vendedores", json=vendedor_exemplo)
    assert response.status_code == 200
    yield response.json()
    client.delete(f"/vendedores/vendedores/{vendedor_exemplo['cpf']}")

def test_adicionar_vendedor():
    """
    Testa o endpoint POST /vendedores para adicionar um vendedor.
    """
    response = client.post("/vendedores/vendedores", json=vendedor_exemplo)
    assert response.status_code == 200
    assert response.json()["cpf"] == vendedor_exemplo["cpf"]
    assert response.json()["nome"] == vendedor_exemplo["nome"]
    assert response.json()["email"] == vendedor_exemplo["email"]
    assert response.json()["telefone"] == vendedor_exemplo["telefone"]
    assert response.json()["comissao_percentual"] == vendedor_exemplo["comissao_percentual"]
    client.delete(f"/vendedores/vendedores/{vendedor_exemplo['cpf']}")


@pytest.mark.usefixtures("novo_vendedor")
def test_listar_vendedores():
    """
    Testa o endpoint GET /vendedores para listar vendedores.
    """
    response = client.get("/vendedores/vendedores")
    assert response.status_code == 200
    assert any(vendedor["cpf"] == vendedor_exemplo["cpf"] for vendedor in response.json())

@pytest.mark.usefixtures("novo_vendedor")
def test_buscar_vendedor():
    """
    Testa o endpoint GET /vendedores/{cpf} para buscar um vendedor pelo CPF.
    """
    response = client.get(f"/vendedores/vendedores/{vendedor_exemplo['cpf']}")
    assert response.status_code == 200
    assert response.json()["cpf"] == vendedor_exemplo["cpf"]


@pytest.mark.usefixtures("novo_vendedor")
def test_atualizar_vendedor():
    """
    Testa o endpoint PUT /vendedores/{cpf} para atualizar um vendedor.
    """
    vendedor_cpf = vendedor_exemplo["cpf"]
    novo_dado = {"cpf": vendedor_cpf,
    "nome": "João Vendedor",
    "email": "joaonovo@email.com",
    "telefone": "15999999999",
    "comissao_percentual": 10.0}
    response = client.put(f"/vendedores/vendedores/{vendedor_cpf}", json=novo_dado)
    assert response.status_code == 200
    assert response.json()["nome"] == novo_dado["nome"]
    assert response.json()["email"] == novo_dado["email"]
    assert response.json()["telefone"] == novo_dado["telefone"]
    assert response.json()["comissao_percentual"] == novo_dado["comissao_percentual"]

def test_remover_vendedor():
    """
    Testa o endpoint DELETE /vendedores/{cpf} para remover um vendedor.
    """
    vendedor_cpf = client.post("/vendedores/vendedores", json=vendedor_exemplo).json()["cpf"]
    response = client.delete(f"/vendedores/vendedores/{vendedor_exemplo['cpf']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Vendedor removido com sucesso!"