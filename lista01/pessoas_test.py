import pytest

from pessoas import Pessoa

def test_get_total_pessoas():
    person1 = Pessoa("Ananda", 31)
    person2 = Pessoa("Roeschen", 89)
    
    assert Pessoa.get_total_pessoas() == 2