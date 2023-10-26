#!/usr/bin/python3
"""
This module defines a Student class that has methods for JSON serialization and deserialization.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from
        a JSON dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
