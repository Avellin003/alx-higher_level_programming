#!/usr/bin/python3
"""function that appends"""


def append_after(filename="", search_string="", new_string=""):
    """creation"""
    with open(filename, "r", encoding="utf-8") as a:
        listl = []
        while True:
            ls = a.readline()
            if ls == "":
                break
            listl.append(ls)
            if search_string in ls:
                listl.append(new_string)
    with open(filename, "w", encoding="utf-8") as b:
        b.writelines(listl)
