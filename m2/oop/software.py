from tests import test_SoftwareStudent_constructor, test_SoftwareStudent_get_major, test_SoftwareStudent_get_greeting, test_SoftwareStudent_calculate_workload

# TODO 8: Import the Student class from student.py
# - see the other files for examples of how to do this

from student import Student

# TODO 9: Create a class called `SoftwareStudent` that does the following:
# - inherits from the `Student` class
# - has a constructor that takes in the following parameters:
#   - name
#   - birth_year
#   - student_id
#   - credit_hours
#   - major
# - calls the super constructor to initialize the `name`, `birth_year`, `student_id`, and `credit_hours` attributes
# - initializes a new attribute called `major` and sets it to the `major` parameter

class SoftwareStudent(Student):
    def __init__(self, name, birth_year, student_id, credit_hours, major):
        super().__init__(name, birth_year, student_id, credit_hours)
        self.major=major

# TODO 10: Create a new method for the `SoftwareStudent` class called `get_major` that returns the `major` attribute

    def get_major(self):
        return self.major

# TODO 11: Update the `get_greeting` method to return the following message:
# - "Hello, my name is <self.name> and I am a <self.major> major."
    
    def get_greeting(self):
        return f"Hello, my name is {self.name} and I am a {self.major} major."



# TODO 12: Update the `calculate_workload` method to return the following:
# - the number of credit hours multiplied by 3 plus 10

    def calculate_workload(self):
        return self.credit_hours * 3 + 10   


def main():

    names_list = ["John", "Jane", "Joe", "Jill"]
    birthyear_list = [1990, 1991, 1992, 1993]
    student_id_list = ["12345", "23456", "34567", "45678"]
    credit_hours_list = [6, 9, 12, 15]
    major_list = ["Computer Science", "Computer Engineering",
                  "Information Technology", "Software Engineering"]

    student_list = [
        SoftwareStudent(names_list[0], birthyear_list[0], student_id_list[0],
                        credit_hours_list[0], major_list[0]),
        SoftwareStudent(names_list[1], birthyear_list[1], student_id_list[1],
                        credit_hours_list[1], major_list[1]),
        SoftwareStudent(names_list[2], birthyear_list[2], student_id_list[2],
                        credit_hours_list[2], major_list[2]),
        SoftwareStudent(names_list[3], birthyear_list[3], student_id_list[3],
                        credit_hours_list[3], major_list[3]),
    ]

    test_SoftwareStudent_constructor(names_list, birthyear_list,
                                     student_id_list, credit_hours_list, major_list, student_list)
    test_SoftwareStudent_get_major(major_list, student_list)
    test_SoftwareStudent_get_greeting(names_list, major_list, student_list)
    test_SoftwareStudent_calculate_workload(credit_hours_list, student_list)

    print("All tests passed!")


if __name__ == "__main__":
    main()
