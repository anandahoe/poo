from personagem import Personagem
from mago import Mago
from guerreiro import Guerreiro

class Combate:
    """Combate representa uma partida do jogo.
    
    Attributes:
        personagem1 (Personagem): Personagem 1.
        personagem2 (Personagem): Personagem 2.
    """

    def __init__(self, personagem1, personagem2):
        if not isinstance(personagem1, Personagem):
            raise TypeError("Personagem 1 precisa ser do tipo Personagem")
        
        if not isinstance(personagem2, Personagem):
            raise TypeError("Personagem 2 precisa ser do tipo Personagem")
        
        self.personagem1 = personagem1
        self.personagem2 = personagem2
    
    def iniciar_combate(self):
        """Inicia Combate entre dois personagens."""
        print(f"Início do combate entre {self.personagem1.nome} e {self.personagem2.nome}.")

        self.personagem1.atacar()
        self.personagem2.defender()

        self.personagem2.atacar()
        self.personagem1.defender()

        self.personagem1.atacar()
        self.personagem2.morrer()

        print("Fim do combate!")
    
if __name__ == "__main__":
    maga_ananda = Mago("Maga Ananda", 1, 20, 30)
    guerreira_roeschen = Guerreiro("Guerreira Roeschen", 1, 50, 30)

    combate = Combate(maga_ananda, guerreira_roeschen)
    combate.iniciar_combate()
