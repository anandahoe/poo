from imovel import Imovel

class ImovelVelho(Imovel):
    """ImovelVelho representa um imóvel velho.
    
    Attributes:
        endereco(str): endereço do imóvel.
        preco(float): preço do imóvel.
        desconto(float): desconto no preço do imóvel antigo.
    """
    def __init__(self, endereco: str, preco: float, desconto: float) -> None:
        super().__init__(endereco, preco)
        self.desconto = desconto
    
    def __str__(self):
        return f"O endereço do imóvel é {self.endereco}, o preço é de R${self.preco:.2f} com um desconto de R${self.desconto:.2f}, tendo o preço final de R${(self.preco - self.desconto):.2f}""" 
        
    @property
    def desconto(self):
        return self.__desconto
        
    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto
        
    
if __name__ == '__main__':
    imovel_velho = ImovelVelho("Rua Libéria", 2000, 100)
    print(imovel_velho)
