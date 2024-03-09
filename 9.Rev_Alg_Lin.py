import numpy as np
import matplotlib.pyplot as plt
import cmath

# numeros
z1 = complex(2, -1)
z2 = complex(1, 1)
# operações
z3 = z1 + z2
z4 = z1 - z2
# inicio do gráfico
fig, ax = plt.subplots(subplot_kw={"projection": "polar"}, figsize=(6, 6))
ax.plot(cmath.phase(z1), abs(z1), marker="o", markersize=5, color="red")
ax.plot(cmath.phase(z2), abs(z2), marker="o", markersize=5, color="red")
ax.plot(cmath.phase(z3), abs(z3), marker="o", markersize=5, color="red")
ax.plot(cmath.phase(z4), abs(z4), marker="o", markersize=5, color="red")

plt.show()
