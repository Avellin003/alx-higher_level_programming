#!/usr/bin/python3
"""function that appends"""


def append_after(filename="", search_string="", new_string=""):
    """creation"""
    with open(filename, "r", encoding="utf-8") as a:
        li = []
        while True:
            l = a.readline()
            if l == "":
                break
            l.append(li)
            if search_string in l:
                li.append(new_string)
    with open(filename, "w", encoding="utf-8") as b:
        b.writelines(li)
