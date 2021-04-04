numeros = list()
pares = list()
impares = list()
continuar = 'S'
c = 0
while continuar == 'S':
    numeros.append(int(input('Digite um número: ')))
    if numeros[c] % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    c += 1
print('Numeros pares: ')
for d in range(0, len(pares)):
    print(numeros[pares[d]])


