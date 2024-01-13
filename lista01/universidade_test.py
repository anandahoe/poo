import pytest

from universidade import Universidade

@pytest.fixture(autouse=True)
def inicia_classe_universidade():
    Universidade.total_professores = 0
    Universidade.total_estudantes = 0

def test_matricular_estudantes():
    Universidade.matricular_estudantes()
    assert Universidade.total_estudantes == 1
    
def test_contratar_professores():
    Universidade.contratar_professores()
    assert Universidade.total_professores == 1
    
def test_obter_total_pessoas():
    Universidade.contratar_professores()
    Universidade.matricular_estudantes()
    
    assert Universidade.obter_total_pessoas() == 2