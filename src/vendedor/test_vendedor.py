import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Vendedor de exemplo
vendedor_exemplo = {
    "nome": "João Vendedor",
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
    client.delete(f"/vendedores/vendedores/{response.json()['id']}")

def test_adicionar_vendedor():
    """
    Testa o endpoint POST /vendedores para adicionar um vendedor.
    """
    response = client.post("/vendedores/vendedores", json=vendedor_exemplo)
    assert response.status_code == 200
    assert response.json()["nome"] == vendedor_exemplo["nome"]
    assert response.json()["comissao_percentual"] == vendedor_exemplo["comissao_percentual"]
    client.delete(f"/vendedores/vendedores/{response.json()['id']}")  # Cleanup

@pytest.mark.usefixtures("novo_vendedor")
def test_listar_vendedores():
    """
    Testa o endpoint GET /vendedores para listar vendedores.
    """
    response = client.get("/vendedores/vendedores")
    assert response.status_code == 200
    assert any(vendedor["nome"] == vendedor_exemplo["nome"] for vendedor in response.json())

@pytest.mark.usefixtures("novo_vendedor")
def test_buscar_vendedor():
    """
    Testa o endpoint GET /vendedores/{id} para buscar um vendedor pelo ID.
    """
    vendedor_id = client.post("/vendedores/vendedores", json=vendedor_exemplo).json()["id"]
    response = client.get(f"/vendedores/vendedores/{vendedor_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == vendedor_exemplo["nome"]

@pytest.mark.usefixtures("novo_vendedor")
def test_atualizar_vendedor():
    """
    Testa o endpoint PUT /vendedores/{id} para atualizar um vendedor.
    """
    vendedor_id = client.post("/vendedores/vendedores", json=vendedor_exemplo).json()["id"]
    novo_dado = {"nome": "João Atualizado", "comissao_percentual": 15.0}
    response = client.put(f"/vendedores/vendedores/{vendedor_id}", json=novo_dado)
    assert response.status_code == 200
    assert response.json()["nome"] == novo_dado["nome"]
    assert response.json()["comissao_percentual"] == novo_dado["comissao_percentual"]

@pytest.mark.usefixtures("novo_vendedor")
def test_remover_vendedor():
    """
    Testa o endpoint DELETE /vendedores/{id} para remover um vendedor.
    """
    vendedor_id = client.post("/vendedores/vendedores", json=vendedor_exemplo).json()["id"]
    response = client.delete(f"/vendedores/vendedores/{vendedor_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Vendedor removido com sucesso!"