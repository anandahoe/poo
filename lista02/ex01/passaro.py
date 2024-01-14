from animal import Animal

class Passaro(Animal):
    """Passaro representa um animal.
    
    Attributes
        nome (str): Nome do cachorro.
    """
    
    def __init__(self, nome: str):
        super().__init__(nome)


    def emitir_som(self):
        """Realiza a ação de emitir som do pássaro"""
        super().emitir_som()
        print(f"A {self.nome} é uma ave e então ela canta!")

    def mover(self):
        """Realiza a ação de mover do pássaro"""
        super().mover()
        print(f"A {self.nome} é uma ave e então ela voa!")
    
if __name__ == "__main__":
    passaro = Passaro("Flor")

    passaro.emitir_som()
    passaro.mover()
    