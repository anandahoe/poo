"""6) Crie uma classe chamada Carro que represente um carro com os seguintes atributos:
Marca (String)
Modelo (String)
Ano (int)
Velocidade (int)

A classe deve ter os seguintes métodos:
Um método construtor que recebe os valores iniciais para marca, modelo e ano, e inicializa a velocidade com 0.
Um método "acelerar" que aumenta a velocidade do carro em 10 unidades.
Um método "frear" que diminui a velocidade do carro em 5 unidades.
"""

class Carro:
    """Carro representa um carro."""
    
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__velocidade = 0
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    def acelerar(self):
        """Acelera o carro."""
        self.__velocidade += 10
        
    def freiar(self):
        """Freia o carro."""
        if self.__velocidade >= 5:
            self.__velocidade -= 5
        else:
            self.__velocidade = 0