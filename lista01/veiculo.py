"""8) Crie uma classe chamada Veiculo com os seguintes atributos:
Marca (str)
Ano (int)
Valor base (float)
A classe deve ter um método abstrato chamado calcular_imposto() que calcula e retorna o valor do imposto a ser pago pelo veículo.
O imposto é 2% do valor depreciado do veículo.
A depreciação é calculada como 5% por ano desde o ano de fabricação do veículo até o ano atual em cima do valor base."""

from datetime import datetime

class Veiculo:
    __depreciacao = 0.05
    __porcentagem_imposto = 0.02
    
    def __init__(self, marca: str, year: int, valor_base: float):
        self.marca = marca
        self.year = year
        self.valor_base = valor_base
        
    def calcular_imposto(self):
        veiculo_idade = datetime.now().year - self.year
        depreciacao_valor = self.valor_base * (1 - Veiculo.__depreciacao) ** veiculo_idade
        return depreciacao_valor * Veiculo.__porcentagem_imposto