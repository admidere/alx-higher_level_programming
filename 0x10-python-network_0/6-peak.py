#!/usr/bin/python3
"""Find peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers.

    :param list_of_integers: List of integers.
    :return: Peak value if found, otherwise None.
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
