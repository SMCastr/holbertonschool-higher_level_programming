#!/usr/bin/python3
class Student:
    """
    A class that represents a student with attributes first_name, last_name, and age.
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

    def to_json(self, attrs=None):
        """
        Convert the student object to a JSON-compatible dictionary with optional attribute filter.

        Args:
            attrs (list): A list of attribute names to include in the dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return {key: getattr(self, key) for key in self.__dict__.keys()}

        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary with attribute-value pairs.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the Student instance.

        Returns:
            str: A formatted string representing the Student object.
        """
        return "<Student {} {} {}>".format(self.first_name, self.last_name, self.age)
