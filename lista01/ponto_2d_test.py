import pytest

from ponto_2d import Ponto2D

def test_has_common_axis():
    pontoA = Ponto2D(1, 1)
    pontoB = Ponto2D(1, 2)

    assert Ponto2D.has_common_axis(pontoA, pontoB) == True

def test_does_not_have_common_axis():
    pontoA = Ponto2D(1, 1)
    pontoB = Ponto2D(3, 2)

    assert Ponto2D.has_common_axis(pontoA, pontoB) == False