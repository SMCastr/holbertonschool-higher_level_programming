#!/usr/bin/python3
class Student:
    """
    A class that defines a student with attributes first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Sample usage for testing
if __name__ == "__main__":
    student_1 = Student("Tom", "Smith", 89)
    print(student_1)  # Correct output - Student(“Tom”, “Smith”, 89)

    student_2 = Student("I have a long name", "A very long name, not you?", -89)
    print(student_2)  # Correct output - Student(“I have a long name”, “A very long name, not you?”, -89)

    student_3 = Student("", "", 0)
    print(student_3)  # Correct output - Student("", "", 0)
