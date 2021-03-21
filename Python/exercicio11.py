altura = float(input('Qual é a altura da parede? '))
base = float(input('Qual é a base da parede? '))
area = base*altura
tinta = area/2
print('A area da parede é \033[36m{} metros quadrados\033[m e a quantidade necessaria para pinta-la é de \033[1;30;47m{:.2f} litros\033[m de tinta'.format(area, tinta))