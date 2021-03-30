from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for sorteados in numeros:
    print('{}'.format(f'Os numeros sorteados foram {sorteados}'))
print(f'O maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
