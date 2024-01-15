from typing import Any, List
import sqlite3
from pokemon import Pokemon

class PokemonRepositorio:
    """Repositório de pokemons."""
    def __init__(self, db_nome: str) -> None:
        self.db_nome = db_nome

    def executar_query(self, query: str, *params: Any) -> None:
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def inserir_pokemon(self, pokemon: Pokemon) -> Pokemon:
        """Insere um pokemon no banco de dados. O objeto pokemon é atualizado com o ID do banco.
        
        Args:
            pokemon (Pokemon): Pokemon que será criado.
        """
        query = "INSERT INTO pokemons (id, name_pokemon, tipo_pokemon, vida) VALUES (?, ?, ?, ?)"
        self.executar_query(query, pokemon.id, pokemon.name_pokemon, pokemon.tipo_pokemon, pokemon.vida)
        return pokemon

    def atualizar_pokemon(self, pokemon: Pokemon) -> None:
        """Atualiza os dados de um pokemon no banco de dados."""
        query = "UPDATE pokemons SET nome_pokemon = ?, tipo_pokemon = ?, vida = ?, WHERE id = ?"
        self.executar_query(query, pokemon.nome_pokemon, pokemon.tipo_pokemon, pokemon.vida, pokemon.id)

    def remover_pokemon(self, pokemon: Pokemon) -> None:
        """Remove um pokemon do banco de dados."""
        query = "DELETE FROM pokemons WHERE id = ?"
        self.executar_query(query, pokemon.id)

    def obter_pokemons(self) -> List[Pokemon]:
        """Obtém todos os pokemons cadastrados no banco de dados."""
        query = "SELECT * FROM pokemons"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Pokemon(row[0], row[1], row[2], row[3]) for row in rows]