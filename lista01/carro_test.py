import pytest

from carro import Carro

def test_carro_acelerar():
    carro = Carro("Toyota", "Corolla", 2018)
    
    carro.acelerar()
    
    assert carro.velocidade == 10
    
    
def test_carro_freiar():
    carro = Carro("Toyota", "Corolla", 2018)
    
    carro.acelerar()
    carro.freiar()
    
    assert carro.velocidade == 5
    
def test_carro_freia_parado():
    carro = Carro("Toyota", "Corolla", 2018)
    
    carro.freiar()
    
    assert carro.velocidade == 0