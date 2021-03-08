from math import hypot

cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
hip = hypot(cop, cad)
print('A hipotenusa é {}'.format(hip))