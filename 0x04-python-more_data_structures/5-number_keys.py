#!/usr/bin/python3
def number_keys(a_dictionary):
    result = 0
    new = list(a_dictionary.keys())
    for i in new:
        result = result + 1
    return result

