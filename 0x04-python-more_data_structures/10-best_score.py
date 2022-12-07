#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max1 = 0
    maxkey = None
    for key, value in a_dictionary.items():
        if value > max1:
            max1 = value
            maxkey = key
    return maxkey
