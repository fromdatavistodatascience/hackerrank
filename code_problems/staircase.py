import numpy as np


def staircase(n):
    "Function that prints a staircase with base and height equal to n"
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)


print(staircase(6))
