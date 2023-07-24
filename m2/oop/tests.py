def test_greetings(names_list: list, person_list: list):
    """
    Tests the greetings of the people in the list.

    args:
        - names_list: list of strings
        - person_list: list of Person objects

    raises:
        - AssertionError if the greetings don't match
    """

    for i in range(len(names_list)):
        assert (
            person_list[i].get_greeting(
            ) == f"Hello, my name is {names_list[i]}."
        ), f"Expected 'Hello, my name is {names_list[i]}.', got {person_list[i].get_greeting()}."


def test_ages(ages_list: list, person_list: list):
    """
    Tests the ages of the people in the list.

    args:
        - ages_list: list of ints
        - person_list: list of Person objects

    raises:
        - AssertionError if the ages don't match
    """

    for i in range(len(ages_list)):
        assert ages_list[i] == person_list[
            i].get_age(), f"Expected {ages_list[i]}, got {person_list[i].get_age()}."


def test_constructor(names_list, birthyear_list, student_id_list, student_list):
    """
    Tests the constructor of the Student class.

    args:
        - names_list: list of strings
        - birthyear_list: list of ints
        - student_id_list: list of strings
        - student_list: list of Student objects

    raises:
        - AssertionError if the attributes don't match
    """

    for i in range(len(names_list)):
        assert (
            student_list[i].name == names_list[i]
        ), f"Expected {names_list[i]}, got {student_list[i].name}."
        assert (
            student_list[i].birth_year == birthyear_list[i]
        ), f"Expected {birthyear_list[i]}, got {student_list[i].birth_year}."
        assert (
            student_list[i].student_id == student_id_list[i]
        ), f"Expected {student_id_list[i]}, got {student_list[i].student_id}."


def test_get_student_id(student_id_list, student_list):

    for i in range(len(student_list)):
        assert (
            student_list[i].get_student_id() == student_id_list[i]
        ), f"Expected {student_id_list[i]}, got {student_list[i].get_student_id()}."


def test_calculate_workload(student_list, credit_hours_list):
    """
    Tests the calculate_workload method of the Student class.

    args:
        - student_list: list of Student objects
        - credit_hours_list: list of ints

    raises:
        - AssertionError if the workload doesn't match
    """

    for i in range(len(student_list)):
        assert (
            student_list[i].calculate_workload() == credit_hours_list[i] * 3
        ), f"Expected {credit_hours_list[i] * 3}, got {student_list[i].calculate_workload()}."


def test_SoftwareStudent_constructor(names_list, birthyear_list, student_id_list, credit_hours_list, major_list, software_student_list):
    """
    Tests the constructor of the SoftwareStudent class.

    Parameters:
        names_list (list): A list of names
        birthyear_list (list): A list of birth years
        student_id_list (list): A list of student IDs
        credit_hours_list (list): A list of credit hours
        major_list (list): A list of majors
        software_student_list (list): A list of SoftwareStudent objects
    """
    for i in range(len(names_list)):
        assert software_student_list[i].name == names_list[i]
        assert software_student_list[i].birth_year == birthyear_list[i]
        assert software_student_list[i].student_id == student_id_list[i]
        assert software_student_list[i].credit_hours == credit_hours_list[i]
        assert software_student_list[i].major == major_list[i]


def test_SoftwareStudent_get_major(major_list, software_student_list):
    """
    Tests the get_major method of the SoftwareStudent class.

    Parameters:
        major_list (list): A list of majors
        software_student_list (list): A list of SoftwareStudent objects
    """
    for i in range(len(major_list)):
        assert software_student_list[i].get_major() == major_list[i]


def test_SoftwareStudent_get_greeting(names_list, major_list, software_student_list):
    """
    Tests the get_greeting method of the SoftwareStudent class.

    Parameters:
        names_list (list): A list of names
        major_list (list): A list of majors
        software_student_list (list): A list of SoftwareStudent objects
    """
    for i in range(len(names_list)):
        assert software_student_list[i].get_greeting(
        ) == f"Hello, my name is {names_list[i]} and I am a {major_list[i]} major."


def test_SoftwareStudent_calculate_workload(credit_hours_list, software_student_list):
    """
    Tests the calculate_workload method of the SoftwareStudent class.

    Parameters:
        credit_hours_list (list): A list of credit hours
        software_student_list (list): A list of SoftwareStudent objects
    """
    for i in range(len(credit_hours_list)):
        assert software_student_list[i].calculate_workload(
        ) == credit_hours_list[i] * 3 + 10
