from forma_geometrica import FormaGeometrica

class Retangulo(FormaGeometrica): 
    def __init__(self, lado_a: float, lado_b: float):
        self.lado_a = lado_a
        self.lado_b = lado_b
        
    def calcular_area(self) -> float:
        """Calcula a área do retângulo."""
        return self.lado_a * self.lado_b
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.lado_a + self.lado_b)