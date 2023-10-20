#!/usr/bin/python3
"""
This module defines a Student class that has methods for JSON serialization and deserialization.
"""


class Student:
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
