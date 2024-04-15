import numpy as np


# produto cartesiano
def cartesiano(m1, m2):
    m = m1 @ (m2)
    return m


# dagger (conjugado da transposta <-> )
def dagger(m):
    m = np.transpose(m)
    m = np.recarray.conjugate(m)
    return m


# Identidade se: A.I = A
A = np.array([[1, 2 - 1j], [2 + 1j, 1]], complex)
# uma matriz é Hermitiana se: transposta(A) = conjugada(A) => transposta(A).inverso(conjugada(A)) = I
tA = np.transpose(A)
icA = np.linalg.inv(np.conjugate(A))
m = cartesiano(tA, icA)
m = cartesiano(A, m)
if np.array_equiv(A, m) == True:
    print("Hermitiana")
# Unitária se: dagger(A).A = A.dagger(A) = I
m = cartesiano(dagger(A), A)
if np.array_equal(A, m) == True:
    print("Unitário")
