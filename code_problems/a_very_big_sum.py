ex = (5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005)


def aVeryBigSum(ar):
    "Function that sums all the elements in an array"
    length = len(ar)
    s = 0
    for i in ar[1:]:
        s += i
    return s


print(aVeryBigSum(ex))
