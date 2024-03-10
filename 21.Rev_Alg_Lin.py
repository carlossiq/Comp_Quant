import numpy as np

a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], complex)
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], complex)

m = np.kron(a, b)
print(m)
