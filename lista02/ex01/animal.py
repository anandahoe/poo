"""1) Implemente uma superclasse Animal com métodos como emitir_som() e mover().
Crie subclasses como Cachorro, Gato, Pássaro.
Sobrescreva os métodos para representar o nome específico de cada animal.
"""
from abc import ABC

class Animal(ABC):
    """Animal representa um animal.
    
    Attributes
        nome (str): Nome do animal.
    """

    def __init__(self, nome: str):
        self.nome = nome


    def emitir_som(self):
        """Realiza a ação de emitir som do animal."""
        print(f"A {self.nome} está emitindo som!")

    def mover(self):
        """Realiza a ação de mover do animal."""
        print(f"A {self.nome} está se movendo!")

if __name__ == "__main__":
    animal = Animal("Amora")

    animal.emitir_som()
    animal.mover()