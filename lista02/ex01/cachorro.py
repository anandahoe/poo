from animal import Animal

class Cachorro(Animal):
    """Cachorro representa um animal.
    
    Attributes
        nome (str): Nome do cachorro.
    """
    
    def __init__(self, nome: str):
        super().__init__(nome)


    def emitir_som(self):
        """Realiza a ação de emitir som do cachorro"""
        super().emitir_som()
        print(f"A {self.nome} é um cachorro e então ela late.")
    
if __name__ == "__main__":
    cachorro = Cachorro("Amora")

    cachorro.emitir_som()
    cachorro.mover()
    