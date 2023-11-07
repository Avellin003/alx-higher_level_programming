#!/usr/bin/python3
"""creation of function"""


def pascal_triangle(n):
    """function"""
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        tempo = [1]
        for a in range(len(t) - 1):
            tempo.append(t[i] + t[i + 1])
        tempo.append(1)
        tri.append(tempo)
    return tri
