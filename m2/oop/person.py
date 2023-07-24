from tests import test_greetings, test_ages
from datetime import datetime as date


class Person:
    """
    Base class for the Person -> Student -> SoftwareStudent inheritance hierarchy

    attributes:
        name (str): The name of the person
        birth_year (int): The year the person was born
    """

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_greeting(self):
        # TODO 1: Complete this method so that it returns the message "Hello, my name is <self.name>."
        # - You can use f-strings, string concatenation, or string formatting (see moreSyntax folder)
        return "Hello, my name is {}.".format(self.name)

    def get_age(self):
        # TODO 2: Use the datetime module to get the year, then calculate and return the age
        # - This is already imported for you, so reference it as `date` (see README/docs for more)
        current_year = date.now().year
        age = current_year - self.birth_year
        return age


def main():
    """
    Runs tests on the Person class.
    """
    names_list = ["Agatha", "Bert", "Cruella"]
    ages_list = [34, 33, 435]

    person_list = [
        Person(names_list[0], 1989),
        Person(names_list[1], 1990),
        Person(names_list[2], 1588),
    ]

    test_greetings(names_list, person_list)
    test_ages(ages_list, person_list)

    print("All tests passed!")


if __name__ == "__main__":
    main()
