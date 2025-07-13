import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Produto de exemplo
produto_exemplo = {
    "nome": "Produto Teste",
    "preco": 99.99,
    "estoque": 50
}

@pytest.fixture
def novo_produto():
    """
    Fixture para criar um produto antes do teste e removê-lo após o teste.
    """
    response = client.post("/produtos/produtos", json=produto_exemplo)
    assert response.status_code == 200
    yield response.json()
    client.delete(f"/produtos/produtos/{response.json()['id']}")

def test_adicionar_produto():
    """
    Testa o endpoint POST /produtos para adicionar um produto.
    """
    response = client.post("/produtos/produtos", json=produto_exemplo)
    assert response.status_code == 200
    assert response.json()["nome"] == produto_exemplo["nome"]
    assert response.json()["preco"] == produto_exemplo["preco"]
    assert response.json()["estoque"] == produto_exemplo["estoque"]
    client.delete(f"/produtos/produtos/{response.json()['id']}")  # Cleanup

@pytest.mark.usefixtures("novo_produto")
def test_listar_produtos():
    """
    Testa o endpoint GET /produtos para listar produtos.
    """
    response = client.get("/produtos/produtos")
    assert response.status_code == 200
    assert any(produto["nome"] == produto_exemplo["nome"] for produto in response.json())

def test_buscar_produto(novo_produto):
    """
    Testa o endpoint GET /produtos/{id} para buscar um produto pelo ID.
    """
    produto_id = novo_produto["id"]
    response = client.get(f"/produtos/produtos/{produto_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == produto_exemplo["nome"]


def test_atualizar_produto(novo_produto):
    """
    Testa o endpoint PUT /produtos/{id} para atualizar um produto.
    """
    produto_id = novo_produto["id"]
    novo_dado = {
        "nome": "Produto Atualizado",
        "preco": 120.0,
        "estoque": 30
    }
    response = client.put(f"/produtos/produtos/{produto_id}", json=novo_dado)
    assert response.status_code == 200
    assert response.json()["nome"] == novo_dado["nome"]
    assert response.json()["preco"] == novo_dado["preco"]
    assert response.json()["estoque"] == novo_dado["estoque"]


@pytest.mark.usefixtures("novo_produto")
def test_remover_produto():
    """
    Testa o endpoint DELETE /produtos/{id} para remover um produto.
    """
    produto_id = client.post("/produtos/produtos", json=produto_exemplo).json()["id"]
    response = client.delete(f"/produtos/produtos/{produto_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Produto removido com sucesso!"