from abc import ABC, abstractclassmethod

class IHabilidadeEspecial(ABC):
    """IHabilidadeEspecial é uma interface que define as habilidades especiais
    que os personagens devem ter."""

    @abstractclassmethod
    def usar_super_habilidade(self):
        """Utilizar a super habilidade do personagem."""
        