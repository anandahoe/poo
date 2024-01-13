import pytest

from student import Student, InvalidGradeError, InvalidNameError

def test_student_creation():
    student = Student("Ananda Hoefelmann", [10, 10, 10])
    assert student.name == "Ananda Hoefelmann"
    assert student.grades == [10, 10, 10]

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        student = Student ("Ananda", [10, 10, 10])

def test_invalid_grades():
    with pytest.raises(InvalidGradeError):
        student = Student("Ananda Hoefelmann", [-1, 10, 10])

def test_student_registration():
    student = Student("Ananda Hoefelmann", [10, 10, 10])
    assert 1 < student.registration < 100_000

def test_student_average():
    student = Student("Ananda Hoefelmann", [10, 10, 10])
    assert student.get_average() == 10

def test_student_average_without_grades():
    student = Student("Ananda Hoefelmann", [])
    assert student.get_average() == 0

def test_get_situation_aprovado():
    student = Student("Ananda Hoefelmann", [10, 10, 10])
    assert student.get_situation() == "Aprovado"

def test_get_situation_recuperacao():
    student = Student("Ananda Hoefelmann", [5, 5, 5])
    assert student.get_situation() == "Recuperação"

def test_get_situation_reprovado():
    student = Student("Ananda Hoefelmann", [2, 2, 2])
    assert student.get_situation() == "Reprovado"
