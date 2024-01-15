import sqlite3

class InicializadorBD:
    """Classe responsável por iniciar o banco de dados."""
    
    @staticmethod
    def criar_tabelas(db_nome: str):
        """Cria as tabelas no banco de dados.

        Args:
            db_nome (str): Nome do banco de dados.
        """

        connection = sqlite3.connect('db_nome')
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INT PRIMARY KEY AUTOINCREMENT,
                nome_pokemon VARCHAR(256) NOT NULL,
                tipo_pokemon VARCHAR(256) NOT NULL,
                vida INT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS ataques(
                id INTEGER PRIMARY KEY,
                nome_ataque VARCHAR(256) NOT NULL,
                dano_ataque INT NOT NULL,
                tipo_ataque VARCHAR(256) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS efeitos(
                id INTEGER PRIMARY KEY,
                nome VARCHAR(256) NOT NULL,
                tipo VARCHAR(256) NOT NULL
            );                      
            CREATE TABLE IF NOT EXISTS pokemons_attacks (
                id INTEGER PRIMARY KEY, 
                pokemon_id INT NOT NULL, 
                ataque_id INT NOT NULL,
                FOREIGN KEY(pokemon_id) REFERENCES pokemons(id),
                FOREIGN KEY(ataque_id) REFERENCES ataque(id)
            );         
        """)

        connection.commit()
        connection.close()

if __name__ == "__main__":
    InicializadorBD.create_tables("db.db")