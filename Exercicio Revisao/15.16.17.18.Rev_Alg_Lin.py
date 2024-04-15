# operações com G complexo e abeliano
# adição, inversa, multiplicação escalar
# transposta, conjugada, dagger
# produto cartesiano
# produto interno
# traço

import numpy as np


class Matriz:
    def get_n():
        n = int(input("Defina n (Anxn): "))
        return n

    def set(n):
        def set_vectors(n):
            def line(n, row):
                vetor = []
                col = 0
                for col in range(n):
                    vetor += [complex(input("a%d%d: " % (row, col)))]
                return vetor

            print("Insira a Matriz A%dx%d" % (n, n))
            matrix = []
            row = 0
            for row in range(n):
                linha = line(n, row)
                matrix += [linha]
            return matrix

        def set_array_complex(m):
            m = np.array(m, complex)
            return m

        m = set_vectors(n)
        m = set_array_complex(m)
        return m

    # adição
    def soma(m1, m2):
        soma = m1 + m2
        return soma

    # inversa
    def inversa(m):
        mm = np.linalg.inv(m)
        return mm

    # multiplicação escalar
    def escalar(a, m2):
        m = a * m2
        return m

    # transposta
    def transposta(m):
        m = np.transpose(m)
        return m

    # conjugada
    def conjugada(m):
        m = np.recarray.conjugate(m)
        return m

    # dagger (conjugado da transposta <-> )
    def dagger(m):
        m = np.transpose(m)
        m = np.recarray.conjugate(m)
        return m

    # produto cartesiano
    def cartesiano(m1, m2):
        m = m1 @ (m2)
        return m

    # produto interno
    def prod(m1, m2):
        m = m1 @ np.conjugate(m2)
        return m

    # traço
    def traço(m):
        a = np.ndarray.trace(m)
        return a


# main
# n = Matriz.get_n()
# m1 = Matriz.set(n)
# m2 = Matriz.set(n)
m = np.array([[1, 1], [0, 0]], complex)
m = Matriz.dagger(m)
print(m)
