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


def test_is_consistent(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Alice", "01234")

    result = phonebook.is_consistent()

    assert result is True


def test__add__same_number__inconsistent(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Alice", "12345")

    result = phonebook.is_consistent()

    assert result is False


def test__add__same_prefix_number__inconsistent(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Alice", "123")

    result = phonebook.is_consistent()

    assert result is False


def test__add_entry__with_letter__raise_error(phonebook):
    with pytest.raises(ValueError):
        phonebook.add("Bob", "a12345")


def test__add_entry__with_backslash__raise_error(phonebook):
    with pytest.raises(ValueError):
        phonebook.add("Bob", "12\\345")


def test__add_entry__with_spaces_or_dashes__strip_them(phonebook):
    phonebook.add("Bob", "1 23-45")

    result = phonebook.lookup("Bob")

    assert result == "12345"


def test__load_phone_data__is_consistent(phonebook):
    phonebook.load_phone_data('../phone_data.txt')

    result = phonebook.is_consistent()

    assert result is True


def test__load_phone_data__10000_entries__is_consistent(phonebook):
    phonebook.load_phone_data('../phone_data_10000.txt')

    result = phonebook.is_consistent()

    assert result is True
