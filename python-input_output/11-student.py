#!/usr/bin/python3

class Student:
    """A class that represents a student with attributes first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the student object to a JSON-compatible dictionary with optional attribute filter."""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with values from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the Student instance."""
        return "<Student {} {} {}>".format(self.first_name, self.last_name, self.age)
