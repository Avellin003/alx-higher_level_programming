#!/usr/bin/python3
'''
create a function that checks if object is instance of class
'''


def is_same_class(obj, a_class):
    '''function that returns True if success or False if not'''
    if (type(obj) == a_class):
        return True
    else:
        return False
