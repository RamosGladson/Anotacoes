m = int(0)
print('-' * 60)
for c in range(1, 500, 2):
    if c % 3 == 0:
        m += c
print('A soma de todos os numeros impares multiplos de 3 é: {}{}{}'.format('\033[34m', m, '\033[m'))
print('-' * 60)