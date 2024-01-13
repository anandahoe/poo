import pytest

from triangulo import Triangulo

def test_criacao_triangulo():
    triangulo = Triangulo(10, 9, 8)
    
    assert triangulo.a == 10
    assert triangulo.b == 9
    assert triangulo.c == 8

def test_invalida_criacao_triangulo():
    with pytest.raises(ValueError):
        triangulo = Triangulo(5, 10, 4)

def test_tipo_equilatero():
    triangulo = Triangulo(10, 10, 10)
    
    assert triangulo.get_type() == "Equilátero"
    
def test_tipo_escaleno():
    triangulo = Triangulo(10, 9, 8)
    
    assert triangulo.get_type() == "Escaleno"
    
def test_tipo_isosceles():
    triangulo = Triangulo(10, 10, 8)
    
    assert triangulo.get_type() == "Isósceles"