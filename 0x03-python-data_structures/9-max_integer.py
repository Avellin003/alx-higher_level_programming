#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    max_value = my_list[0]
    for i in range(1, len(my_list)):
        if max_value < my_list[i]:
            max_value = my_list[i]
        else:
            continue
        return max_value
