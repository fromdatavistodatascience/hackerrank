
a = (17, 28, 30)
b = (99, 16, 8)


def compareTriplets(a, b):
    "Function that returns the grading scores for Alice and Bob"
    a_score = 0
    b_score = 0
    length = len(a)
    for i in range(length):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
        else:
            continue
    scores = (a_score, b_score)
    return scores


print(compareTriplets(a, b))
