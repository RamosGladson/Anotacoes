continuar = 'S'
numeros = list()
print('\033[31m{}\033[m'.format('=' * 30))
print('{}'.format('|' * 30))
while continuar == 'S':
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

print(numeros)
print(f'A quantidade de números digitados foi {len(numeros)}')
print(f'A lista em ordem decrescente é {sorted(numeros, reverse = True)}')
if 5 in numeros:
    print(f'O número cinco foi digitado na posição {numeros.index(5)}')
else:
    print('O numero cinco não foi digitado!')