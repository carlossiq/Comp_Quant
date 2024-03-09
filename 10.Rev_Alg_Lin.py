import numpy as np
import math


def converter(x, y):
    modulo = np.sqrt(x**2 + y**2)
    alfa = np.arctan(y / x) * 360 / (2 * np.pi)
    lista = [modulo, alfa]
    return lista


x = int(input("x: "))
y = int(input("y: "))
z_linha = converter(x, y)
print("Modulo: ", z_linha[0], "\nangulo: ", z_linha[1], " graus")
