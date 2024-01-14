from animal import Animal

class Gato(Animal):
    """Gato representa um animal.
    
    Attributes
        nome (str): Nome do gato.
    """
    
    def __init__(self, nome: str):
        super().__init__(nome)


    def emitir_som(self):
        """Realiza a ação de emitir som do gato"""
        super().emitir_som()
        print(f"A {self.nome} é uma gata e então ela mia")
    
if __name__ == "__main__":
    gato = Gato("Marie")

    gato.emitir_som()
    gato.mover()
    