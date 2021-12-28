import os
import csv


class Phonebook:
    def __init__(self, cache_directory):
        self.numbers = {}
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name: str, number: str) -> None:
        number = number.replace(" ", "").replace("-", "")
        if number.isnumeric():
            self.numbers[name] = number
        else:
            raise ValueError

    def lookup(self, name) -> str:
        return self.numbers[name]

    def is_consistent(self) -> bool:
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def names(self):
        return set(self.numbers.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename)

    def load_phone_data(self, filepath: str) -> None:
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if row:
                    self.add(row[0], row[1])
