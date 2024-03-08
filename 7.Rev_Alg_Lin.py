import numpy as np

c1 = complex(input("c1: "))
c2 = complex(input("c2: "))

a = np.conj(c1)
b = np.conj(c2)
c = np.conj(c1 + c2)
d = np.conj(c1 * c2)

print(a + b, "=", c)
print(a * b, "=", d)
