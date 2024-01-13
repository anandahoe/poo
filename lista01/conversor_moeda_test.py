import pytest

from conversor_moeda import ConversorMoeda

def test_converter_para_real():
    valor_convertido = ConversorMoeda.converter_para_real(10)
    
    assert valor_convertido == pytest.approx(49.28, 0.5)
    
def test_converter_de_real():
    valor_convertido = ConversorMoeda.converter_de_real(10)
    
    assert valor_convertido == pytest.approx(2.03, 0.5)