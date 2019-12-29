import numpy as np

matrix = np.array(([11, 2, 4],[4, 5, 6], [10, 8, -12]))


def diagonalDifference(arr):
    "Function that calculates the diagonal difference of a square matrix"
    rows = len(arr)
    cols = rows  # square matrix
    arr_reversed = [vals for vals in reversed(arr)]
    l_to_r = 0
    r_to_l = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                l_to_r += arr[i][j]
                r_to_l += arr_reversed[i][j]
            else:
                continue 
    diagonal_diff = abs(l_to_r - r_to_l)
    return diagonal_diff
