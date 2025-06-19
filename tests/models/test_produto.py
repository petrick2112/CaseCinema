import pytest
from models.produto import Produto

def test_produto_initialization():
    produto = Produto(nome="Camiseta", preco=29.99)
    assert produto.nome == "Camiseta"
    assert produto.preco == 29.99

def test_produto_nome_type():
    produto = Produto(nome="Ingresso", preco=50)
    assert isinstance(produto.nome, str)

def test_produto_preco_type():
    produto = Produto(nome="Caneca", preco=15.5)
    assert isinstance(produto.preco, (int, float))