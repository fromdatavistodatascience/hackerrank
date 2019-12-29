import numpy as np

sample_input = [1, 2, 3, 4, 5]


def miniMaxSum(arr):
    """Function that calculated the minimum and maximum sum within numbers
    of an array"""
    min_val = min(arr)
    max_val = max(arr)
    total_sum = 0
    for val in arr:
        total_sum += val
    mini_sum = total_sum - max_val
    max_sum = total_sum - min_val
    return print(mini_sum, max_sum)


miniMaxSum(sample_input)
