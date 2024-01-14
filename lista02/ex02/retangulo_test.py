import pytest

from retangulo import Retangulo

def test_criacao_retangulo():
    retangulo = Retangulo(5, 10)
    
    assert retangulo.lado_a == 5
    assert retangulo.lado_b == 10
    
def test_calcular_area():
    retangulo = Retangulo(5, 10)
    
    assert retangulo.calcular_area() == 50
    
def test_calcular_perimetro():
    retangulo = Retangulo(5, 10)
    
    assert retangulo.calcular_perimetro() == 30