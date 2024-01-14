import pytest

from triangulo_2 import Triangulo

def test_triangulo_valido():
    triangulo = Triangulo(10, 5, 6)
    
    assert triangulo.lado_a == 10
    assert triangulo.lado_b == 5
    assert triangulo.lado_c == 6
    
def test_triangulo_invalido():
    with pytest.raises(AttributeError):
        triangulo = Triangulo(10, 20, 30)
        
def test_calcular_area():
    triangulo_isosceles = Triangulo(10, 11, 11)
    triangulo_escaleno = Triangulo(10, 5, 6)
    triangulo_equilatero = Triangulo(10, 10, 10)
    
    assert triangulo_isosceles.calcular_area() == pytest.approx(48.98, 0.1)
    assert triangulo_escaleno.calcular_area() == pytest.approx(11.39, 0.1)
    assert triangulo_equilatero.calcular_area() == pytest.approx(43.3, 0.1)
    
def test_calcular_perimetro():
    triangulo = Triangulo(10, 5, 6)
    
    assert triangulo.calcular_perimetro() == 21