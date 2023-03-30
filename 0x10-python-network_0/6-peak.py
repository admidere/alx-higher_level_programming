#!/usr/bin/python3
"""Finds the peak in an unsorted list of integers"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
