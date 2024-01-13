import pytest

from calculadora import Calculadora


def test_sum():
    assert Calculadora.sum(1, 2, 3) == 6
    
def test_sub():
    assert Calculadora.sub(1, 2, 3) == -4
    
def test_multi():
    assert Calculadora.multi(1, 2, 3) == 6
    
def test_div():
    assert Calculadora.div(6, 2, 3) == 1
    
def test_div():
    with pytest.raises(ZeroDivisionError):
        assert Calculadora.div(2, 0)