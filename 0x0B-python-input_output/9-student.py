#!/usr/bin/python3
"""creation of class student"""


class Student:
    """public attributes of student"""
    def __init__(self, first_name, las_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
 
    def to_json(self):
        """the public method"""
        return (self.__dict__)
