"""2) Crie a superclasse FormaGeometrica com os métodos calcular_area() e calcular_perimetro().
Crie subclasses como Círculo, Retângulo e Triângulo que implementam um método construtor de
acordo com os dados necessários e sobrescreva os métodos para cálculo de área e perímetro."""

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula a área da forma geométrica."""
        
    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Calcula o perímetro da forma geométrica."""