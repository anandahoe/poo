import pytest

from circulo import Circulo

def test_criacao_circulo():
    circulo = Circulo(20)
    
    assert circulo.raio == 20
    
def test_calcular_area():
    circulo = Circulo(20)
    
    assert circulo.calcular_area() == pytest.approx(1256.64, 0.1)
    
def test_calcular_perimetro():
    circulo = Circulo(20)
    
    assert circulo.calcular_perimetro() == pytest.approx(125.6, 0.1)