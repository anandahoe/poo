"""
Classe - É um modelo para o objeto.
* Atributos - Características do objeto.
* Métodos - Ações do objeto (função que está dentro de uma classe).
"""

class NomeClasse:
    """ Docstring da classe"""

    # Método construtor: método utilizado para inicializar um objeto da classe.
    # Ele sempre retorna None, então pode-se omitir

    def __init__(self, parametro1: int = 10) -> None:
        # self -> referência ao próprio objeto.
        self.atributo1 = parametro1

        # Declarar um atributo privado.
        self.__atributo_privado = 0
    
    # Getters (acessar atributos privados do objeto)
    @property
    # Adicionando um comportamento para uma função
    def atributo_privado(self):
        return self.__atributo_privado
    
    # Setters
    @atributo_privado.setter
    def atributo_privado(self, novo_valor: int):
        self.__atributo_privado = novo_valor

    # Métodos do objeto
    def metodo1(self):
        """Docstring do método."""
        print("Chamando o método do objeto.")


if __name__ == '__main__':
    objeto_teste = NomeClasse(20)
    print(objeto_teste.atributo1)
    objeto_teste.metodo1()