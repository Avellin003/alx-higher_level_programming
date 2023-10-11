#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search != replace:
        a = new_list.index(search)
        new_list[a] = replace
        return(new_list)
    else:
        return (my_list)
