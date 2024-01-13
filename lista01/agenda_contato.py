from person import Person

"""
3) Crie uma classe agenda que pode armazenar 10 pessoas e que seja capaz de realizar as seguintes operações:
    adicionar_pessoa() - Adiciona uma pessoa na agenda.
    remover_pessoa() - Remove uma pessoa pelo nome da agenda.
    buscar_pessoa() - Busca uma pessoa pelo nome na agenda (Mostra todas as informações da pessoa encontrada).
    listar_pessoas() - Mostra as informações de todas as pessoas da agenda.

    As pessoas da agenda devem ser objetos da classe Pessoa (ex. 1).
"""

class Agenda:
    """Agenda representa uma agenda
    Attributes:
        name(str): Nome da agenda.
    """

    def __init__(self, name: str):
        self.name = name
        self.__people = []

    @property
    def people(self):
        """List[People] representa as pessoas da agenda."""
        return self.__people

    def add_person(self, person: Person):
        """Adiciona uma pessoa na agenda.
        
        Args:
            person(Person): Pessoa a ser adicionada.
        """
        if len(self.__people) < 10:
            self.__people.append(person)
        else:
            print("A agenda está cheia.")

    def remove_person(self, name: str):
        """Remove uma pessoa da agenda.
        
        Args:
            name(str): Nome da pessoa a ser removida.
        """
        for person in self.__people:
            if person.name == name:
                self.__people.remove(person)
                return
        print("A pessoa não foi encontrada.")

    def search_person(self, name: str):
        """Pesquisa e mostra as informações de uma pessoa se ela estiver na agenda.
        
        Args:
            name(str): Nome da pessoa a ser procurada.
        """
        for person in self.__people:
            if person.name == name:
                print(person)
                return
        print("A pessoa não foi encontrada na agenda.")

    def list_people(self):
        """Lista as pessoas da agenda."""
        for person in self.__people:
            print(person)

