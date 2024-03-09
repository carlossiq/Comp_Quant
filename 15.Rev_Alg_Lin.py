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
                print(matrix)
            return matrix

        matrix = set_vectors(n)
        return matrix

    def show(n, matrix):
        row = 0
        for row in range(n):
            print(matrix[row])


# main
n = Matriz.get_n()
matriz = Matriz.set(n)
Matriz.show(n, matriz)
