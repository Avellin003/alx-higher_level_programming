#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord('c'): None})
    new_string = new.translate({ord('C'): None})
    return new_string
