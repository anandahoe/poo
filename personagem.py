from abc import ABC

class Personagem(ABC):
    """Personagem representa um personagem em um jogo.
    
    Attributes:
        nome(str): Nome do personagem.
        nivel (int): Nível do personagem.
        vida(int): Vida do personagem.
    """
    def __init__(self, nome:str, nivel:int, vida:int):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
    
    def atacar(self):
        """Realiza a ação de atacar do personagem."""
        print(f"{self.nome} está atacando!")
    
    def defender(self):
        """Realiza a ação de defender do personagem."""
        print(f"{self.nome} está defendendo!")

    def morrer(self):
        """Realiza a ação de morte do personagem."""
        print(f"{self.nome} foi derrotado!")      

if __name__ == "__main__":
    personagem = Personagem("Ananda", 1, 10)

    personagem.atacar()
    personagem.defender()
    personagem.morrer()