from forma_geometrica import FormaGeometrica
from math import sqrt

class Triangulo(FormaGeometrica):
    def __init__(self, lado_a: float, lado_b: float, lado_c: float):
        if not self.__is_triangle(lado_a, lado_b, lado_c):
            raise AttributeError("Triângulo não é válido.")
        
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        
    def __is_triangle(self, lado_a: float, lado_b: float, lado_c: float) -> bool:
        """Verifica se o triângulo é válido.
        
        Args:
            lado_a (float): Lado A do triângulo.
            lado_b (float): Lado B do triângulo.
            lado_c (float): Lado C do triângulo.
        """
        return (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a
    
    def calcular_area(self) -> float:
        """Retorna a área do triângulo."""
        semiperimetro = (self.lado_a + self.lado_b + self.lado_c) / 2
        
        return sqrt(semiperimetro * (semiperimetro - self.lado_a) * (semiperimetro - self.lado_b) * (semiperimetro - self.lado_c))
    
    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do triângulo"""
        return self.lado_a + self.lado_b + self.lado_c