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

    def to_json(self):
        """
        Convert the student object to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return {key: getattr(self, key) for key in self.__dict__.keys()}

# Sample usage for testing
if __name__ == "__main__":
    student_1 = Student("John", "Snow", 25)
    print(student_1.to_json())  # Correct output - to_json()
    
    print(student_1.to_json(['first_name']))  # Correct output - to_json(['first_name'])
    
    print(student_1.to_json(['first_name', 'age']))  # Correct output - to_json(['first_name', 'age'])
    
    print(student_1.to_json([]))  # Correct output - to_json([])
    
    print(student_1.to_json(['first_name', 'saymyname', 'last_name', 'Age']))  # Correct output - to_json(['first_name', 'saymyname', 'last_name', 'Age'])
