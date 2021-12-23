import pytest
from phonebook.phonebook import Phonebook

@pytest.fixture
def phonebook(tmpdir):
    phonebook = Phonebook(tmpdir)
    yield phonebook
    phonebook.clear() #


# @pytest.fixture
# def phonebook(tmpdir):
#     return Phonebook(tmpdir)
