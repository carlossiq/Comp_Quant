# (1*x^4) + (0*x^3) + (2*x^2) + (1)=0
import math

a = 1
b = 2
c = 1
delta = b**2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / 2 * a
x2 = (-b + (-1) * (math.sqrt(delta))) / 2 * a
# >=0
if x1 or x2 >= 0:
    print("Existe raiz real")
else:
    ("Existem somente raizes complexas.")
