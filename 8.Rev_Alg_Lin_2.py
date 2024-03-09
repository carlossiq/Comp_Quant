import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Arc


class complexo:
    # configura o plano argando-gauss
    def plano_gauss(ax, tamanho):
        ax.spines["top"].set_color("none")
        ax.spines["bottom"].set_position("center")
        ax.spines["left"].set_position("center")
        ax.spines["right"].set_color("none")
        ax.xaxis.set_ticks_position("bottom")
        ax.yaxis.set_ticks_position("left")
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.grid(which="both", color="grey", linewidth=1, linestyle="-", alpha=0.2)
        # legendas
        ax.set_xlabel("Re", loc="right")
        ax.set_ylabel("Im", rotation="horizontal", ha="right", y=0.96, labelpad=-50)
        fig.suptitle("Plano de Argand-Gauss", color="dimgray")
        ax.set_title("Números complexos")
        plt.xlim([-tamanho, tamanho])
        plt.ylim([-tamanho, tamanho])

    # define o vetor complexo
    def vetor_principal(z, ax):
        ax.scatter(z.real, z.imag, s=100, color="red")
        ax.quiver(0, 0, z.real, z.imag, units="xy", angles="xy", scale=1)
        # linhas tracejadas
        ax.hlines(z.imag, 0, z.real, linestyle="--", color="purple")
        ax.vlines(z.real, 0, z.imag, linestyle="--", color="purple")

    def circulo_modulo(z, ax):
        circle = plt.Circle((0, 0), abs(z), color="blue", fill=False)
        ax.set_aspect("equal", adjustable="datalim")
        ax.add_patch(circle)

    def vetores_componentes(z, ax):
        ax.quiver(
            0,
            0,
            z.real,
            0,
            units="xy",
            angles="xy",
            scale=1,
            color="red",
            width=0.075,
            alpha=0.25,
        )
        ax.quiver(
            0,
            0,
            0,
            z.imag,
            units="xy",
            angles="xy",
            scale=1,
            color="red",
            width=0.075,
            alpha=0.25,
        )

    def mostrar_angulo(z, ax):
        angle = math.degrees(math.asin(z.imag / abs(z)))

        arc = Arc(xy=(0, 0), width=2, height=2, theta1=0, theta2=angle, linewidth=2)
        ax.add_patch(arc)

        ax.text(1.1, 0.4, f"{angle:.1f}°", fontsize=14)

    def plotar_complexo(z, ax, ang, vcomp, circulo):
        complexo.vetor_principal(z, ax)
        if circulo == 1:
            complexo.circulo_modulo(z, ax)
        if vcomp == 1:
            complexo.vetores_componentes(z, ax)
        if ang == 1:
            complexo.mostrar_angulo(z, ax)


def max_modulo(z1, z2):
    m1 = abs(z1)
    m2 = abs(z2)
    m3 = abs(z1 + z2)
    m4 = abs(z1 - z2)
    i = 0
    lista = [m1, m2, m3, m4]
    max = m1
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            max = lista[i + 1]

    return max


# numeros
z1 = complex(2, -1)
z2 = complex(1, 1)
# operações
z3 = z1 + z2
z4 = z1 - z2
# inicio do gráfico
tamanho = max_modulo(z1, z2) + 1.5
fig, ax = plt.subplots()
# plano
complexo.plano_gauss(ax, tamanho)
# argumentos: angulo, vetor-componente, círculo
complexo.plotar_complexo(z1, ax, 0, 1, 0)
complexo.plotar_complexo(z2, ax, 0, 1, 0)
complexo.plotar_complexo(z3, ax, 0, 1, 0)
complexo.plotar_complexo(z4, ax, 0, 1, 0)
# plotar
plt.show()
