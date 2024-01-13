"""10) Crie uma classe chamada Triangulo com os seguintes atributos:
Lado1 (float)
Lado2 (float)
Lado3 (float)

A classe deve ter um método chamado verificar_tipo que verifica e retorna o tipo do triângulo com base nos valores dos lados.
Os tipos de triângulos podem ser: equilátero, isósceles ou escaleno."""

class Triangulo:
    def __init__(self, a: float, b: float, c: float):
        if not self.__triangulo(a, b, c):
            raise ValueError("Os valores fornecidos não forma um triângulo")
        
        self.__a = a
        self.__b = b
        self.__c = c
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
        
    def __triangulo(self, a: float, b: float, c: float) -> bool:
        return (a + b > c) and (a + c > b) and (b + c > a)
        
    def get_type(self) -> str:
        if self.__b == self.__a == self.__c:
            return "Equilátero"
        
        if self.__b != self.__a != self.__c:
            return "Escaleno"

        return "Isósceles"