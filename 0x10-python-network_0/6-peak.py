#!/usr/bin/python3
"""This function finds the peak number"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of unsorted integers.

    Returns:
    - The peak element.

    Note: There may be more than one peak in the list.
    """
    left, right = 0, len(list_of_integers - 1)

    if not list_of_integers:
        return None

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1

        else:
            right = mid

    return list_of_integers[left]
