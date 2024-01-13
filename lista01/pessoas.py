"""9) Crie uma classe chamada Pessoa com os seguintes atributos:
Nome (str)
Idade (int)
A classe deve ter um atributo estático privado chamado total_pessoas para contar o número total de instâncias da classe Pessoa.

Implemente um método estático chamado get_total_pessoas() que retorna o valor do atributo total_pessoas.
"""

class Pessoa:
    __total_pessoas = 0
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        
        Pessoa.__total_pessoas += 1
        
    @classmethod
    def get_total_pessoas(cls):
        return cls.__total_pessoas