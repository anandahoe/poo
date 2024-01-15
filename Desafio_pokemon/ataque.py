class Ataque:
    """Ataque representa um ataque.
    
    Attributes:
        id (int): ID do ataque
        nome_ataque (str): Nome do ataque
        tipo_ataque (str): Tipo do ataque
        dano_ataque (int): Quantidade de dano do ataque
    """
    def __init__(self, id: int, nome_ataque: str, dano_ataque: int, tipo_ataque: str) -> None:
        self.id = id
        self.nome_ataque = nome_ataque
        self.tipo_ataque = tipo_ataque
        self.type = type
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def __str__(self) -> str:
        return f"{self.name}"
