#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        new = my_list.copy()
        new.pop(idx)
        new.insert(idx, element)
        return (new)