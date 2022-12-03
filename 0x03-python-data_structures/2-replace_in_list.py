#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len = 0
    for i in my_list:
        len += 1
    if idx < 0:
        return my_list
    if idx > len - 1:
        return my_list
    for i in range(len):
        if i == idx:
            my_list[i] = []
            my_list[i] = element
        return my_list
