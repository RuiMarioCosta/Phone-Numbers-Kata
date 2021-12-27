# Run tests with html report:
# $ pytest pytest/ --html=report/report.html
# $ pytest --cov-report=html --cov=phonebook/ pytest/
# $ pytest --cov-report=html --cov-branch --cov=phonebook/ pytest/

import pytest


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
