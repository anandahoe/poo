import pytest

from produto import Produto

def test_criacao_produto():
    produto = Produto("Produto 01", 100, 10)
    
    assert produto.estoque == 10
    
def test_comprar_produto():
    produto = Produto("Produto 01", 100, 10)
    
    produto.comprar_produto(5)
    
    assert produto.estoque == 15
    
def test_vender_produto():
    produto = Produto("Produto 01", 100, 10)
    
    produto.vender_produto(5)
    
    assert produto.estoque == 5
    
def test_vender_produto_sem_estoque(capfd):
    produto = Produto("Produto 01", 100, 10)
    
    produto.vender_produto(11)
    
    out, _ = capfd.readouterr()
    
    assert out == "Não há estoque para realizar a operação.\n"
    
def test_calcular_valor_total():
    produto = Produto("Produto 01", 100, 10)
    
    assert produto.calcular_valor_total() == 1000