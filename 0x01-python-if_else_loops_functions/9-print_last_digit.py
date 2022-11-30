#!/usr/bin/python3
def print_last_digit(number):
    i = abs(number)
    print(i % 10, end="")
    return i % 10
