import math

# Here are the test scores of 10 students in physics and history:

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Compute Karl Pearson’s coefficient of correlation between these scores.


def mean_normalize(var):
    norm = []  # Vector for storing output values
    mean = sum(var)/len(var)
    # for each element in the vector, subtract from mean and add the result
    # to norm
    for i in var:
        diff = i - mean
        norm.append(diff)
    return norm


def dot_product(x, y):
    prod_vec = 0  # Initliaze an empty list to store the results
    # For all elements in the vectors, multiply and save results in prod_vec
    for i in range(len(x)):
        prod = x[i] * y[i]
        prod_vec += prod
    return prod_vec


def correlation(var1, var2):
    "Function to calculate the correlation between two scores."
    if len(var1) != len(var2):
        return 'The lengths of both the lists should be equal.'
    else:
        mean_norm_var1 = mean_normalize(var1)
        mean_norm_var2 = mean_normalize(var2)
        var1_dot_var2 = dot_product(mean_norm_var1, mean_norm_var2)
        var1_squared = [i * i for i in mean_norm_var1]
        var2_squared = [i * i for i in mean_norm_var2]
        return round(var1_dot_var2 / math.sqrt(sum(var1_squared) *
                                               sum(var2_squared)), 3)


print(correlation(physics_scores, history_scores))
