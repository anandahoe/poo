from __future__ import annotations
"""4) Crie uma classe chamada Ponto2D para representar um ponto no espaço cartesiano. 
Essa classe deve ter os atributos: x e y.
Essa classe deve ter o método estático tem_eixo_comum(ponto_a, ponto_b)
que retorna True se dois objetos tiverem as mesmas coordenadas para algum dos eixos.
"""

class Ponto2D:
    def __inti__(self, x:int, y:int):
        self.x = x
        self.y = y

    @staticmethod
    def has_common_axis(pontoA: Ponto2D, pontoB: Ponto2D) -> bool:
        """Verifica se dois pontos possuem eixos em comum.
        
        Args:
            pontoA (Ponto2D) : Ponto A
            pontoB (Ponto2D) : Ponto B
        
        Returns:
            True caso possua um eixo em comum, False caso contrário.
        """
        return pontoA.x == pontoB.x or pontoA.y == pontoB.y 