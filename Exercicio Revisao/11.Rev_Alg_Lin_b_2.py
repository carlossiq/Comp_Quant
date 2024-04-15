# multiplicação de um complexo pelo imaginario formado por sua parte imaginaria
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Arc


class Complexo:
    # configura o plano argando-gauss
    def plano_gauss(ax, fig, tamanho):
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
        Complexo.vetor_principal(z, ax)
        if circulo == 1:
            Complexo.circulo_modulo(z, ax)
        if vcomp == 1:
            Complexo.vetores_componentes(z, ax)
        if ang == 1:
            Complexo.mostrar_angulo(z, ax)


def funcao_i0(z):
    z *= complex(0, z.imag)
    tamanho = abs(z) + 1.5
    fig, ax = plt.subplots()
    Complexo.plano_gauss(ax, fig, tamanho)
    Complexo.plotar_complexo(z, ax, 0, 1, 1)
    plt.show()


funcao_i0(1 + 2j)
