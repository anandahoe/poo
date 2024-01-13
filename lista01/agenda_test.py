import pytest
from io import StringIO
import sys

from agenda_contato import Agenda
from person import Person

def test_add_person():
    person = Person("Célia Diva", "+55 (47) 9 9958-8585")

    agenda_contato = Agenda("Agenda teste")
    agenda_contato.add_person(person)

    assert person in agenda_contato.people
    assert len(agenda_contato.people) == 1

def test_add_person_failed(capfd):
    agenda_contato = Agenda("Agenda teste")
    for i in range(10):
        agenda_contato.add_person(Person)
    extra_person = Person("Cesar Emiliano", "+55 (48) 9 5252-8595")
    agenda_contato.add_person(extra_person)

    out, _ = capfd.readouterr()
    assert extra_person not in agenda_contato.people
    assert "A agenda está cheia." in out

def test_remove_person():
    agenda_contato = Agenda("Agenda teste")
    person = Person("Célia Diva", "+55 (47) 9 9958-8585")
    agenda_contato.add_person(person)
    agenda_contato.remove_person("Célia Diva")
    assert person not in agenda_contato.people

def test_remove_person_failed(capfd):
    agenda_contato = Agenda("Agenda teste")
    agenda_contato.remove_person("Guilherme")
    out, _ = capfd.readouterr()
    assert "A pessoa não foi encontrada." in out

def test_search_person(capfd):
    agenda_contato = Agenda("Agenda teste")
    person = Person("Célia Diva", "+55 (47) 9 9958-8585")
    agenda_contato.add_person(person)
    agenda_contato.search_person("Célia Diva")
    out, _ = capfd.readouterr()
    assert out == "Nome: Célia Diva | Telefone: +55 (47) 9 9958-8585\n"

def test_search_person_failed(capfd):
    agenda_contato = Agenda("Agenda teste")
    person = Person("Cesar Emiliano", "+55 (48) 9 5252-8595")
    agenda_contato.search_person("Cesar Emiliano")
    out, _ = capfd.readouterr()
    assert "A pessoa não foi encontrada na agenda.\n" in out

def test_list_people(capfd):
    agenda_contato = Agenda("Agenda teste")
    agenda_contato.add_person(Person("Célia Diva", "+55 (47) 9 9958-8585"))
    agenda_contato.add_person(Person("Cesar Emiliano", "+55 (48) 9 5252-8595"))
    agenda_contato.list_people()
    out, _ = capfd.readouterr()
    print_esperado = "Nome: Célia Diva | Telefone: +55 (47) 9 9958-8585\n" "Nome: Cesar Emiliano | Telefone: +55 (48) 9 5252-8595\n"
    assert out == print_esperado