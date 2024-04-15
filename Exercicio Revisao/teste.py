import numpy as np


def invert(matrix):
    matriz = np.linalg.inv(matrix)
    return matriz


a = np.array([[1, 1], [2, 1]], complex)
a1 = a * a
a2 = a * np.transpose(a)
a3 = a @ a
print(a1)
print(a2)
print(a3)
