#!/usr/bin/python3
"""creation of class student"""


class Student:
    """public attributes of student"""
    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the public method"""
        if (isinstance(attrs, list) and
                all(isinstance(i, str) for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
