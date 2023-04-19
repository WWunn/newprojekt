import numpy as np
import math
# zadanie 1
a = np.array([[2, 1, 3], [-1, 2, 4]])
b = np.array([[1, 3], [2, -2], [-1, 4]])
c = np.dot(a, b)
# zadanie 2
d = np.array([[2, 1, 3], [-1, 2, 4], [-1, 61, 4], [-22, 2, 12]])
e = np.array([[5, 3], [2, -2], [-9, 123]])
def pozycja(a, b):
    kol = a.min(axis=1)
    kold = a.min(axis=0)
    rzad = b.min(axis=1)
    rzadd = b.min(axis=0)
    print(rzad)
    print(rzadd)
    print(kol)
    print(kold)
def sinusy(a):
    lista = []
    for b in a.flat:

        c = np.insert(math.sin(b))
    print(c)

sinusowy = np.array([[4, 5, 6], [7, 3, 2]])

sinusy(sinusowy)



