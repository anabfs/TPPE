import pytest
import uuid
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Gera CPF aleatório válido para evitar conflito de dados
def gerar_cpf():
    return uuid.uuid4().hex[:11]

@pytest.fixture
def setup_venda():
    cpf_cliente = gerar_cpf()
    cpf_vendedor = gerar_cpf()

    cliente_exemplo = {
        "cpf": cpf_cliente,
        "nome": "Cliente Teste",
        "email": "cliente@teste.com",
        "telefone": "123456789"
    }

    vendedor_exemplo = {
        "cpf": cpf_vendedor,
        "nome": "Vendedor Teste",
        "email": "vendedor@teste.com",
        "telefone": "987654321",
        "comissao_percentual": 10.0
    }

    produto_exemplo = {
        "nome": "Produto Teste",
        "preco": 100.0,
        "estoque": 10
    }

    # Criar cliente
    resp_cliente = client.post("/clientes/clientes", json=cliente_exemplo)
    assert resp_cliente.status_code == 200

    # Criar vendedor
    resp_vendedor = client.post("/vendedores/vendedores", json=vendedor_exemplo)
    assert resp_vendedor.status_code == 200

    # Criar produto
    resp_produto = client.post("/produtos/produtos", json=produto_exemplo)
    assert resp_produto.status_code == 200
    produto_id = resp_produto.json()["id"]

    yield {
        "cliente": cliente_exemplo,
        "vendedor": vendedor_exemplo,
        "produto_id": produto_id,
        "preco": produto_exemplo["preco"],
        "quantidade": 2
    }

    # Limpeza dos dados após o teste
    vendas = client.get("/vendas/vendas").json()
    for venda in vendas:
        if venda["cliente"]["cpf"] == cliente_exemplo["cpf"]:
            client.delete(f"/vendas/vendas/{venda['id']}")
    client.delete(f"/clientes/clientes/{cliente_exemplo['cpf']}")
    client.delete(f"/vendedores/vendedores/{vendedor_exemplo['cpf']}")
    client.delete(f"/produtos/produtos/{produto_id}")

def test_criar_venda(setup_venda):
    dados = setup_venda
    payload = {
        "data": "2025-07-11",
        "cliente_cpf": dados["cliente"]["cpf"],
        "vendedor_cpf": dados["vendedor"]["cpf"],
        "produto_id": dados["produto_id"],
        "quantidade": dados["quantidade"]
    }

    response = client.post("/vendas/vendas", json=payload)
    assert response.status_code == 200
    venda_criada = response.json()
    venda_id = venda_criada["id"]

    # Usar GET /vendas/vendas (lista completa)
    response_get = client.get("/vendas/vendas")
    assert response_get.status_code == 200
    vendas = response_get.json()

    # Filtrar pela ID
    venda = next(v for v in vendas if v["id"] == venda_id)

    assert venda["cliente"]["cpf"] == dados["cliente"]["cpf"]
    assert venda["cliente"]["nome"] == dados["cliente"]["nome"]
    assert venda["produto"]["id"] == dados["produto_id"]
    assert venda["quantidade"] == dados["quantidade"]
    assert venda["vendedor"]["cpf"] == dados["vendedor"]["cpf"]


def test_listar_vendas(setup_venda):
    payload = {
        "data": "2023-10-01",
        "cliente_cpf": setup_venda["cliente"]["cpf"],
        "vendedor_cpf": setup_venda["vendedor"]["cpf"],
        "produto_id": setup_venda["produto_id"],
        "quantidade": 1
    }
    resp = client.post("/vendas/vendas", json=payload)
    assert resp.status_code == 200
    venda_id = resp.json()["id"]

    lista_resp = client.get("/vendas/vendas")
    assert lista_resp.status_code == 200
    vendas = lista_resp.json()
    assert isinstance(vendas, list)
    assert any(v["cliente"]["nome"] == "Cliente Teste" for v in vendas)

    client.delete(f"/vendas/vendas/{venda_id}")

def test_remover_venda(setup_venda):
    payload = {
        "data": "2023-10-01",
        "cliente_cpf": setup_venda["cliente"]["cpf"],
        "vendedor_cpf": setup_venda["vendedor"]["cpf"],
        "produto_id": setup_venda["produto_id"],
        "quantidade": 1
    }
    resp = client.post("/vendas/vendas", json=payload)
    assert resp.status_code == 200
    venda_id = resp.json()["id"]

    del_resp = client.delete(f"/vendas/vendas/{venda_id}")
    assert del_resp.status_code == 200
    assert del_resp.json()["message"] == "Venda removida com sucesso!"

    busca_resp = client.get(f"/vendas/vendas/{venda_id}")
    assert busca_resp.status_code == 404
