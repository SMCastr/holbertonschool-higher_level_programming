#!/usr/bin/python3
"""
This module defines a Student class that has methods for JSON serialization and deserialization.
"""

class Student:
    """
    Defines a student with first_name, last_name, and age attributes.

    Methods:
        to_json(self, attrs=None): Retrieves a dictionary representation of a Student instance.
        reload_from_json(self, json): Replaces all attributes of the Student instance from a JSON dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attributes to include in the dictionary (default is None).

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

# Sample usage for testing
if __name__ == "__main__":
    import os
    import sys

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
