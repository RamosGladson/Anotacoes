ultimo = 0
soma = 0
numero = []
while ultimo != 999:
    ultimo = int(input('Digite um número: '))
    if ultimo != 999:
        numero.append(ultimo)
        soma += ultimo
print('Você digitou {} números'.format(len(numero)))
print('A soma entre eles é {}'.format(soma))