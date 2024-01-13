import pytest
from datetime import datetime

from veiculo import Veiculo

def test_calcular_imposto():
    current_year = datetime.now().year
    veiculo = Veiculo("Toyota", 2018, 50000)
    
    depreciacao_esperada = (1 - 0.05) ** (current_year - 2018)
    imposto_esperado = 50000 * depreciacao_esperada * 0.02
    
    assert veiculo.calcular_imposto() == pytest.approx(imposto_esperado)
    
def test_calcular_imposto_veiculo_novo():
    current_year = datetime.now().year
    veiculo = Veiculo("Tesla", 2024, 60000)
    
    imposto_esperado = 60000 * 0.02
    
    assert veiculo.calcular_imposto() == pytest.approx(imposto_esperado)
    
def test_calcular_imposto_veiculo_velho():
    current_year = datetime.now().year
    veiculo = Veiculo("Ford", 2000, 30000)
    
    depreciacao_esperada = (1 - 0.05) ** (current_year - 2000)
    imposto_esperado = 30000 * depreciacao_esperada * 0.02
    
    assert veiculo.calcular_imposto() == pytest.approx(imposto_esperado)