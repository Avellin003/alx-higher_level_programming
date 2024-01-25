#!/usr/bin/python3
"""function that performs peak finding algorithm"""


def find_peak(list_of_integers):
    """finds the peak """
    if list_of_integers == []:
        return None

    lenth = len(list_of_integers)
    mid = int(lenth / 2)
    lis = list_of_integers

    if mid - 1 < 0 and mid + 1 >= lenth:
        return lis[mid]

    elif mid - 1 < 0:
        return lis[mid] if lis[mid] > lis[mid + 1] else lis[mid + 1]

    elif mid + 1 >= lenth:
        return lis[mid] if lis[mid] > lis[mid - 1] else lis[mid - 1]

    if lis[mid - 1] < lis[mid] > lis[mid + 1]:
        return lis[mid]

    if lis[mid + 1] > lis[mid - 1]:
        return find_peak(lis[mid:])
    return find_peak(lis[:mid])
