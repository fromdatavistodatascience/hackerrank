# Functions to solve questions 1 and 2
import numpy as np

# For question 1:


def decompose_arr(arr):
    "Identifying the actual array values and element k within an array."
    k = arr[-1]
    actual_array = set()
    for val in arr[1:-1]:
        actual_array.add(val)
    return k, actual_array


def findNumber(arr):
    "Function that finds whether element k is present in the array arr."
    k, actual_array = decompose_arr(arr)
    if k in actual_array:
        return print("YES")
    else:
        return print("NO")


# For question 2:

def odd_number_range(l, r):
    "Returns the odd numbers within a range of numbers l and r."
    odd_numbers = [val for val in range(l, r+1) if val % 2]
    odd_number_array = np.array(odd_numbers)
    return odd_number_array
