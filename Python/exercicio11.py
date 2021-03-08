altura = float(input('Qual é a altura da parede? '))
base = float(input('Qual é a base da parede? '))
area = base*altura
tinta = area/2
print('A area da parede é {} metros quadrados e a quantidade necessaria para pinta-la é de {:.2f} litros de tinta'.format(area, tinta))