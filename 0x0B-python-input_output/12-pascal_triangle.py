#!/usr/bin/python3
"""simple module"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
