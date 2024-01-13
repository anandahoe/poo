from personagem import Personagem

class Guerreiro(Personagem):
    """Guerreiro representa um personagem da classe Guerreiro no jogo.
    
    Atributtes:
        nome(str): Nome do personagem.
        nivel (int): Nível do personagem.
        vida(int): Vida do personagem.
        força(int): Quantidade de força do guerreiro.
    """

    def __init__(self, nome:str, nivel:int, vida:int, forca:int):
        # Personagem.__init__(nome, nivel, vida):
        super().__init__(nome, nivel, vida)
        self.forca = forca

    def atacar(self):
        """Realiza a ação de ataque do guerreiro."""
        super().atacar()
        print(f"{self.nome} desfere um golpe com {self.forca} de força!")

    def equipar_escudo(self):
        """Realiza a ação de equipar o escudo."""
        print(f"{self.nome} equipa o seu escudo! A vida de {self.nome} aumentou!")

if __name__ == '__main__':
    guerreiro = Guerreiro("Guerreira Roeschen", 1, 50, 11)
    print(guerreiro.nome)
    guerreiro.atacar()
    guerreiro.equipar_escudo()
