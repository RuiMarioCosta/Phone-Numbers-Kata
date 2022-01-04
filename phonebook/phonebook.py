import csv
import os


class Phonebook:
    def __init__(self, cache_directory: str) -> None:
        self.numbers: dict[str, str] = {}
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name: str, number: str) -> None:
        number = number.replace(" ", "").replace("-", "")
        if number.isnumeric():
            self.numbers[name] = number
        else:
            raise ValueError

    def lookup(self, name: str) -> str:
        return self.numbers[name]

    def _flatten(self, numbers: list) -> list:
        out = []
        for sublist in numbers:
            out.extend(sublist)
        return out

    def is_consistent(self) -> bool:
        numbers = list(self.numbers.values())
        for i in range(len(numbers)):
            number = numbers.pop(0)
            for number2 in numbers:
                if number in number2:
                    return False
            numbers.append(number)
        return True

    def names(self) -> set[str]:
        return set(self.numbers.keys())

    def clear(self) -> None:
        self.cache.close()
        os.remove(self.filename)

    def load_phone_data(self, filepath: str) -> None:
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if row:
                    self.add(row[0], row[1])


if __name__ == "__main__":
    import cProfile

    phonebook = Phonebook(".")
    with cProfile.Profile() as pr:
        phonebook.load_phone_data("../phone_data_65535.txt")

        result = phonebook.is_consistent()

    pr.print_stats()
    pr.dump_stats("phonebook.prof")
