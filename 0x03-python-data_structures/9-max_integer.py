#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        # we use '.sort' as it writes in ascending order
        my_list.sort()
        return my_list[-1]
