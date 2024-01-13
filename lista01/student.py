from typing import List
from random import randint

from person import InvalidNameError
"""
2) Implemente a classe Aluno que possua os atributos: número de matrícula, nome, notas.
Essa classe deve conter os seguintes métodos: 
get_media() - Calcula a média do aluno com base nas notas.
get_situacao() - Informa a situação do aluno com base no critérios:
    0 à 4 - Reprovado
    5 à 6 - Recuperação
    7 à 10 - Aprovado
"""
class InvalidGradeError (Exception):
    """Exceção para nota inválida."""
    pass

class Student:
    """Student representa um aluno.
    
    Attributes:
        name (str): Nome do aluno.
        grade (List[float]): Notas do aluno.
    """
    
    def __init__(self, name: str, grades: List[float]):
        self.__registration = randint(1, 100_000)
        self.name = name
        self.grades = grades
    
    @property
    def registration(self):
        """(int): Número da matrícula do aluno."""
        return self.__registration
    
    @property
    def name(self):
        """(str): Nome do aluno."""
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if not self.__is_name__valid(name):
            raise InvalidNameError()
        self.__name = name
    
    @property
    def grades(self):
        """List[float]: Notas do aluno."""
        return self.__grades
    
    @grades.setter
    def grades(self, grades: List[float]):
        if not self.__is_grades__valid(grades):
            raise InvalidGradeError()
        self.__grades = grades

    def __is_name__valid(self, name: str) -> bool:
        """Verifica se o nome do aluno é válido.
        
        Args:
            name(str): Nome do aluno.
        
        Returns:
            True caso o nome seja válido, False caso contrário.
        """
        return len(name.strip().split()) > 1
    
    def __is_grades__valid(self, grades: List[float]) -> bool:
        """Verifica se as notas do aluno são válidas.
        
        Args:
            grades(List[float]): Notas do aluno.
        
        Returns:
            True caso as notas seja válidas, False caso contrário.
        """
        return not any(grade < 0 or grade > 10 for grade in grades)

    def get_average(self) -> float:
        """Calcula a média do aluno baseado nas notas."""
        if not self.grades:
            return 0
        
        return sum(self.grades) / len(self.grades)
    
    def get_situation(self) -> str:
        """Retorna a situação do aluno com base na média.
        
        Returns:
            A situação do aluno ("Aprovado", "Recuperação", "Reprovado")
        """
        media = self.get_average()

        if 0 <= media <= 4:
            return "Reprovado"
        
        if 4 <= media <= 6:
            return "Recuperação"
        
        return "Aprovado"
