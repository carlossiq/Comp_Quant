import numpy as np
import matplotlib.pyplot as plt

# ax é a região onde será plotado o gráfico

# figura com um ax: fig, ax = plt.subplot()
fig = plt.subplots()

# 2 axes, um em cima outro embaixo
fig, axs = plt.subplots(2, 1)

# 1 a esquerda e 2 a direita (cima e baixo)
fig, axs = plt.subplot_mosaic([["left", "right_top"], ["left", "right_bottom"]])

figure, axes = plt.subplots()
# circulo com centro (0.6,0.6) e raio 0.3, sem preenchimento
Drawing_uncolored_circle = plt.Circle((0.6, 0.6), 0.3, fill=False)
# aspecto circular
axes.set_aspect(1)
axes.add_artist(Drawing_uncolored_circle)
plt.title("Circle")

plt.show()

np.transpose()
np.inner()
np.dot()
np.ndarray.trace()
np.linalg.det()
np.linalg.inv()
