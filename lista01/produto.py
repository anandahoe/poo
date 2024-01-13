"""11) Crie uma classe chamada Produto com os seguintes atributos:
Nome (str)
Preço (float)
Quantidade em estoque (int)

A classe deve ter métodos para realizar as seguintes operações:
Vender produto: recebe a quantidade a ser vendida como parâmetro e atualiza a quantidade em estoque.
Comprar produto: recebe a quantidade a ser comprada como parâmetro e atualiza a quantidade em estoque.
Calcular valor total: retorna o valor total do estoque, multiplicando o preço pela quantidade em estoque."""

class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque
        
    @property
    def estoque(self):
        return self.__estoque
    
    def vender_produto(self, quantidade: int):
        if self.__estoque >= quantidade:
            self.__estoque -= quantidade
        else:
            print("Não há estoque para realizar a operação.")
    
    def comprar_produto(self, quantidade: int):
        self.__estoque += quantidade
    
    def calcular_valor_total(self):
        return self.__estoque * self.preco