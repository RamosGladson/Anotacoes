continuar = 'S'
numeros = []
impares = []
pares = []

while continuar == 'S':
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])

print(f'Os números digitados foram: {numeros}')
print(f'A lista de números pares é :{pares}')
print(f'A lista de números impares é: {impares}')
