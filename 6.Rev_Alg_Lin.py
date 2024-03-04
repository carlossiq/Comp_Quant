import numpy as np

c1 = complex(input("c1: "))
c2 = complex(input("c2: "))

a = abs(c1)
b = abs(c2)
c = abs(c1 + c2)
d = abs(c1 * c2)

print(a * b, "=", d)
print(c, "<=", a + b)
