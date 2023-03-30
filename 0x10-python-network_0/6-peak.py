#!/usr/bin/python3
"""find peak"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    peak = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
