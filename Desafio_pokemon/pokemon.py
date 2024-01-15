class Pokemon:
    """Pokemon representa um pokemon.

    Attributes:
        id (int): ID do pokemon.
        nome_pokemon (str): Nome do pokemon.
        tipo_pokemon (str): Tipo do pokemon.
        vida (int): Vida do pokemon.
    """
    def __init__(self, id: int, nome_pokemon: str, tipo_pokemon: str, vida: int) -> None:
        self.id = id
        self.nome_pokemon = nome_pokemon
        self.tipo_pokemon = tipo_pokemon
        self.vida = vida

    def __repr__(self) -> str:
        return f"Pokemon{self.nome_pokemon} | tipo {self.tipo_pokemon} | vida: {self.vida}"
    
    def __str__(self) -> str:
        return f"Pokemon{self.nome_pokemon} | tipo {self.tipo_pokemon} | vida: {self.vida}"
    
