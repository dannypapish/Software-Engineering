from person import Person
from tests import test_constructor, test_calculate_workload, test_get_student_id


class Student(Person):
    """
    Represents a student

    attributes:
        name (str): The name of the student (inherited from Person)
        birth_year (int): The year the student was born (inherited from Person)
        student_id (str): The student's ID
        credit_hours (int): The number of credit hours the student is taking
    """

    # TODO 3: Create a constructor that takes in the following parameters:
    # - name
    # - birth_year
    # - student_id
    # - credit_hours



    # Enter the name of the file: /Users/akanimohumoren/Downloads/w1/lab1/response.txt

    # TODO 4: Call the super constructor to initialize the `name` and `birth_year` attributes
    # - You can use the super() function to do this
    def __init__(self, name, birth_year, student_id, credit_hours):
        super().__init__(name, birth_year)
    # TODO 5: Initialize the `student_id` and `credit_hours` attributes to the values passed to the constructor
    # - remember to use the `self` keyword
        self.student_id = student_id
        self.credit_hours = credit_hours
    # TODO 6: Create a method called `get_student_id` that returns the `student_id` attribute
    def get_student_id(self):

    # - remember this method needs the `self` parameter to be tied to the object
        return self.student_id
    # TODO 7: Create a method called `calculate_workload` that returns the number of credit hours multiplied by 3
    def calculate_workload(self):
        return self.credit_hours * 3

def main():

    names_list = ["John", "Jane", "Joe", "Jill"]
    birthyear_list = [1990, 1991, 1992, 1993]
    student_id_list = ["12345", "23456", "34567", "45678"]
    credit_hours_list = [6, 9, 12, 15]

    student_list = [
        Student(names_list[0], birthyear_list[0],
                student_id_list[0], credit_hours_list[0]),
        Student(names_list[1], birthyear_list[1],
                student_id_list[1], credit_hours_list[1]),
        Student(names_list[2], birthyear_list[2],
                student_id_list[2], credit_hours_list[2]),
        Student(names_list[3], birthyear_list[3],
                student_id_list[3], credit_hours_list[3]),
    ]

    test_constructor(names_list, birthyear_list, student_id_list, student_list)
    test_calculate_workload(student_list, credit_hours_list)
    test_get_student_id(student_id_list, student_list)

    print("All tests passed!")


if __name__ == "__main__":
    main()
