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
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            try:
                dic[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
            return dic

    def reload_from_json(self, json):
        """reloading"""
        for a in json:
            try:
                setattr(self, a, jason[a])
            except FileNotFoundError:
                pass
