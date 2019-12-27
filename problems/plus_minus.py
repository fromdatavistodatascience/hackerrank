import numpy as np

sample_input = np.array([-4, 3, -9, 0, 4, 1])


def plusMinus(arr):
    """Function that calculates the ratio of positive, negative and 0 values 
    in a given array"""
    l = len(arr)
    p = 0
    n = 0
    z = 0
    for val in arr:
        if val > 0:
            p += 1
        elif val < 0:
            n += 1
        else:
            z += 1
    p_ratio = round(p/l, 6)
    n_ratio = round(n/l, 6)
    z_ratio = round(z/l, 6)
    print(p_ratio)
    print(n_ratio)
    print(z_ratio)
    return "Done"


print(plusMinus(sample_input))
