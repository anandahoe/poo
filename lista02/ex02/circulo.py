from forma_geometrica import FormaGeometrica
from math import pi

class Circulo(FormaGeometrica):
    """Circulo representa um círculo.
    
    Args:
        raio (float): Raio do círculo.
    """
    
    def __init__(self, raio: float):
        self.raio = raio
        
    def calcular_area(self) -> float:
        """Retorna a área do círculo."""
        return pi * self.raio ** 2
        
    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do círculo."""
        return 2 * pi * self.raio