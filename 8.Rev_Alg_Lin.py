import numpy as np
import matplotlib.pyplot as plt


def max_modulo(a, b):
    m1 = abs(a)
    m2 = abs(b)
    m3 = abs(a + b)
    m4 = abs(a - b)
    i = 0
    lista = [m1, m2, m3, m4]
    max = m1
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            max = lista[i + 1]

    return max


def ponto(z, cor):
    # propriedades
    real_z = z.real
    im_z = z.imag
    # arrays
    x1 = [0, real_z]
    y1 = [0, im_z]
    x2 = [real_z, real_z]
    y2 = [0, im_z]
    x3 = [0, real_z]
    y3 = [im_z, im_z]
    # gráfico
    plt.scatter(real_z, im_z, color=cor, marker="o")
    plt.plot(x1, y1, color="black", linewidth=(1))
    plt.plot(x2, y2, color="black", linewidth=(1), linestyle="dashed")
    plt.plot(x3, y3, color="black", linewidth=(1), linestyle="dashed")


# main
# numeros complexos
z1 = complex(2, -1)
z2 = complex(1, 1)
# operações
z3 = z1 + z2
z4 = z1 - z2
# módulo máximo
tamanho = max_modulo(z1, z2) + 1
# grafico
params = {
    "axes.labelsize": 12,
    "axes.titlesize": 12,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.autolayout": True,
    "figure.facecolor": "white",
    "figure.titlesize": 16,
    "figure.figsize": (6, 6),
    "legend.shadow": False,
    "legend.fontsize": 10,
    "lines.linewidth": 2.0,
}

plt.rcParams.update(params)
ponto(z1, "red")
ponto(z2, "blue")
ponto(z3, "green")
ponto(z4, "purple")
# labels
plt.title("Plano cartesiano")
plt.xlabel("Reais")
plt.ylabel("Imaginários")
# Set axis limits
plt.xlim([-tamanho, tamanho])
plt.ylim([-tamanho, tamanho])
plt.grid(True)
plt.show()
