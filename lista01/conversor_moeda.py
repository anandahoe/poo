"""12) Crie uma classe chamada ConversorMoeda com os seguintes atributos estáticos:
Taxa de conversão (float)
Moeda base (str)

A classe deve ter os seguintes métodos estáticos:
Um método converter_para_real() que recebe um valor em outra moeda como parâmetro e retorna o valor convertido para reais.
Um método converter_de_real() que recebe um valor em reais como parâmetro e retorna o valor convertido para a moeda base.
"""

class ConversorMoeda:
    taxa_conversão = 4.89
    moeda_base = "USD"
    

    @classmethod
    def converter_para_real(cls, value: float):
        return cls.taxa_conversão * value
    

    @classmethod
    def converter_de_real(cls, value: float):
        return value / cls.taxa_conversão