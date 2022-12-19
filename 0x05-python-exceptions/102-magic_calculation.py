#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('Too far')
            else:
                res += a ** b / k
        except Exception:
            res = b + a
            break
    return res
