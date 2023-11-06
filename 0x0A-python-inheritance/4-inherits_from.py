#!/usr/bin/python3

'''write a function that returns true subclass else false'''


def inherits_from(obj, a_class):
    '''checks if it's subclass'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
