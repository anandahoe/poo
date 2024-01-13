from personagem import Personagem
from habilidade_especial import IHabilidadeEspecial

class Mago(Personagem, IHabilidadeEspecial):
    """Mago representa um personagem da classe Mago no jogo.
    
    Atributtes:
        nome(str): Nome do personagem.
        nivel (int): Nível do personagem.
        vida(int): Vida do personagem.
        magia(int): Quantidade de magia do mago.
    """

    def __init__(self, nome:str, nivel:int, vida:int, magia:int):
        # Personagem.__init__(nome, nivel, vida):
        super().__init__(nome, nivel, vida)
        self.magia = magia

    def atacar(self):
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f"{self.nome} lança um feitiço poderoso com {self.magia} de magia!")

    def equipar_cajado(self):
        """Realiza a ação de equipar o cajado do mago."""
        print(f"{self.nome} equipe o seu cajado! O próximo ataque causará dano em área.")

    def usar_super_habilidade(self):
        """Utiliza a super habilidade do mago."""
        print(f"{self.nome} utiliza a habilidade especial! Meteoro! Todos os inimigos perdem 99% da vida!")

if __name__ == '__main__':
    mago = Mago("Maga Ananda", 1, 10, 11)
    print(mago.nome)
    mago.atacar()
    mago.equipar_cajado()
    mago.usar_super_habilidade()
