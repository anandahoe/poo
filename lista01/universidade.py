"""7) Crie uma classe chamada Universidade que representa uma universidade com os seguintes atributos estáticos:
Total de estudantes (int)
Total de professores (int)

A classe deve ter os seguintes métodos estáticos:
Um método matricular_estudante que incrementa o total de estudantes.
Um método contratar_professor que incrementa o total de professores.
Um método obter_total_pessoas que retorna o total de estudantes e professores juntos.
"""

class Universidade:
    total_estudantes = 0
    total_professores = 0
    
    @classmethod
    def matricular_estudantes(cls):
        cls.total_estudantes += 1
        
    @classmethod
    def contratar_professores(cls):
        cls.total_professores += 1
        
    @classmethod
    def obter_total_pessoas(cls):
        return cls.total_professores + cls.total_estudantes