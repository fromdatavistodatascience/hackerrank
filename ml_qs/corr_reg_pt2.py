# Here are the test scores of 10 students in physics and history:

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def slope(x, y, n):
    "Calculates the gradient of the line of regression"
    num = (n * sum([x[i]*y[i] for i in range(n)])) - sum(x)*sum(y)
    den = (n * sum([x[i]**2 for i in range(n)])) - sum(x)**2
    return num/den


print(round(slope(physics_scores, history_scores, len(physics_scores)), 3))
