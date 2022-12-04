#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)
    if i >= 2 and j >= 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif i >= 2 and j == 1:
        return tuple_a[0] + tuple_b[0], tuple_a[1]
    elif i >= 2 and j == 0:
        return tuple_a[0], tuple_a[1]
    elif i == 0 and j == 0:
        return 0, 0
    elif i == 1 and j >= 2:
        return tuple_a[0] + tuple_b[0], tuple_b[1]
    elif i == 0 and j >= 2:
        return tuple_b[0], tuple_b[1]
    elif i == 1 and j == 1:
        return tuple_a[0] + tuple_b[0], 0
    elif i == 1 and j == 0:
        return tuple_a[0], 0
    elif i == 0 and j == 1:
        return tuple_b[0], 0
