# Moebis
import matplotlib.pyplot as plt


def moebis(x):
    def transformada(x, a, b, c, d):
        return (a * x + b) / (c * x + d)

    a = d = 0
    b = c = 1

    if (a * d - c * b) != 0 and (c * x + d) != 0:
        return transformada(x, a, b, c, d)
    else:
        return 0


x = [1, 10, 20, 30]
y = [moebis(1), moebis(10), moebis(20), moebis(30)]
fig = plt.plot(x, y)
plt.show()
