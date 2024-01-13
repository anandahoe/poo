import pytest

from person import Person, InvalidNameError, InvalidPhoneError

def test_person_creation():
    person = Person("Ananda Hoefelmann", "+55 48 9 9851-9197")

    assert person.name == "Ananda Hoefelmann"
    assert person.phone == "+55 48 9 9851-9197"

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        person = Person ("Ananda", "+55 48 9 9851-9197")

def test_invalid_phone():
    with pytest.raises(InvalidPhoneError):
        person = Person ("Ananda Hoefelmann", "+55 48 9 9851-91")