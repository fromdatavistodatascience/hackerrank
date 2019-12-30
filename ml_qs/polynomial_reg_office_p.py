import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

k = 3


def get_data():
    training_data = list()
    testing_data = list()
    F, N = map(int, input().split(' '))
    [training_data.append(input().split(' ')) for _ in range(0, N)]
    T = int(input())
    [testing_data.append(input().split(' ')) for _ in range(0, T)]
    training_data = np.array(training_data, dtype=np.float64)
    testing_data = np.array(testing_data, dtype=np.float64)
    X_train = training_data[:, 0:F]
    y_train = training_data[:, -1]
    X_test = testing_data
    return X_train, y_train, X_test


# Given that the relationship between X and y is polynomial, we have to find
# the most suitable to this model.


def converting_to_polynomial(X_train, X_test, k):
    poly = PolynomialFeatures(k)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)
    return X_poly_train, X_poly_test


def fit_and_predict(X_train, y_train, X_test):
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_test = linreg.predict(X_test)
    return y_test


def main():
    X_train, y_train, X_test = get_data()
    X_poly_train, X_poly_test = converting_to_polynomial(X_train, X_test, k)
    result = fit_and_predict(X_poly_train, y_train, X_poly_test)
    return '\n'.join(list(map(str, result)))


if __name__ == '__main__':
    prediction = main()
    print(prediction)
