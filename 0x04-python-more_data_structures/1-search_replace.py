#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    a = new_list.index(search)
    new_list[a] = replace
    return (new_list)
