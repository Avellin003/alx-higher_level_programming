#!/usr/bin/python3
'''
Write a function that returns true if inheritance else false
'''


def is_kind_of_class(obj, a_class):
    '''returns true if inheritance else false'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
