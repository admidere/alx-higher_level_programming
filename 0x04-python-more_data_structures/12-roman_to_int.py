#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    result = 0
    j = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roman_string):
        j = digits[i]
        result += j if result < j * 5 else -j
    return result
