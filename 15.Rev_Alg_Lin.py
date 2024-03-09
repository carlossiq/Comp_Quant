# operações com G complexo e abeliano
# adição, inversa, multiplicação escalar


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
                    vetor += [int(input("a%d%d: " % (row, col)))]
                return vetor

            print("Insira a Matriz A%dx%d" % (n, n))
            matrix = []
            row = 0
            for row in range(n):
                linha = line(n, row)
                matrix += [linha]
            return matrix

        matrix = set_vectors(n)
        return matrix

    def show(n, matrix):
        row = 0
        for row in range(n):
            print(matrix[row])

    def sum(matriz1, matriz2):
        row = col = 0
        soma = matriz1
        for row in range(n):
            for col in range(n):
                soma[row][col] += matriz2[row][col]
        return soma


# main
n = Matriz.get_n()
m1 = Matriz.set(n)
m2 = Matriz.set(n)
Matriz.show(n, m1)
Matriz.show(n, m2)
m = Matriz.sum(m1, m2)
Matriz.show(n, m)
