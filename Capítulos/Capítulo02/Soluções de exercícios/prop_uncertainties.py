from uncertainties import ufloat as uf

a = uf(5, 0.1)
b = uf(3, 0.2)
c = uf(2, 0.5)
f = a + b / c
f
