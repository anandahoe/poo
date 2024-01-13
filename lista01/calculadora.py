from functools import reduce

"""5) Crie uma classe Calculadora que implemente os métodos estáticos:
soma, subtracacao, multiplicacao e divisao."""

class Calculadora:
    """Calculadora representa uma calculadora"""

    def sum(*args):
        return sum(args)
    
    def sub(*args):
        return reduce(lambda acc, curr: acc - curr, args)

    def div(*args):
        return reduce(lambda acc, curr: acc/curr, args)
    
    def multi(*args):
        return reduce(lambda acc, curr: acc * curr, args)