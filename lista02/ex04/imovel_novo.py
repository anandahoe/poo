from imovel import Imovel

class ImovelNovo(Imovel):
    """ImovelNovo representa um imóvel novo.
    
    Attributes:
        endereco(str): endereço do imóvel.
        preco(float): preço do imóvel.
        adicional (float): Adicional no preço do imóvel novo.
    """

    def __init__(self, endereco: str, preco: float, adicional: float) -> None:
        super().__init__(endereco, preco)
        self.adicional = adicional
    
    def __str__(self):
        return f"O endereço do imóvel é {self.endereco}, o preço é de R${self.preco:.2f} com um valor adicional de R${self.adicional:.2f}, tendo o preço final de R${(self.preco + self.adicional):.2f}""" 
    
    @property
    def adicional(self):
        return self.__adicional
    
    @adicional.setter
    def adicional(self, adicional):
        self.__adicional = adicional
    
if __name__ == '__main__':
    imovel_novo = ImovelNovo("Rua Libéria", 2000, 100)
    print(imovel_novo)