"""4) Implemente as classes abaixo:

Classe Imovel: Esta será a classe base.
Atributos:
endereco: Uma string que armazena o endereço do imóvel.
preco: Um valor numérico representando o preço do imóvel.

Métodos:
Um construtor para inicializar os atributos endereco e preco.
Métodos de acesso (getters) para ambos os atributos.
Um método de impressão que exibe o endereço e o preço do imóvel.

Classe Novo (herda de Imovel): Esta classe representa um imóvel novo e tem um adicional no preço.
Atributos:
adicional: Um valor numérico que representa o adicional no preço do imóvel novo.

Métodos:
Um construtor que inicializa o endereço, o preço e o valor adicional.
Métodos de acesso e modificação (getters e setters) para o atributo adicional.
Um método de impressão que exibe o endereço, o preço base, o adicional e o preço final (preço base + adicional).

Classe Velho (herda de Imovel): Esta classe representa um imóvel antigo e tem um desconto no preço.

Atributos:
desconto: Um valor numérico que representa o desconto no preço do imóvel antigo.

Métodos:
Um construtor que inicializa o endereço, o preço e o valor do desconto.
Métodos de acesso e modificação (getters e setters) para o atributo desconto.
Um método de impressão que exibe o endereço, o preço base, o desconto e o preço final (preço base - desconto).
"""

from __future__ import annotations
from abc import ABC

class Imovel(ABC):
    """Imovel representa um imóvel.

    Attributes:
    endereco(str): endereço do imóvel.
    preco(float): preço do imóvel.
    """
    
    def __init__(self, endereco: str, preco: float) -> None:
        self.endereco = endereco
        self.preco = preco
    
    def __str__(self):
        return f"O endereço do imóvel é {self.endereco} e custa o preço de R${self.preco:.2f}"
    
    # Getters
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    # Getters
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

if __name__ == "__main__":
    imovel = Imovel("Rua Libéria 340", 1900.00)
    print(imovel)
        
        