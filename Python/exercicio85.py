numeros = [[], []]
aux = 0
for c in range(0, 7):
    aux = int(input(f'Digite o {c+1}º numero: '))
    if aux % 2 == 0:
        numeros[0].append(aux)
    else:
        numeros[1].append(aux)
numeros[0].sort()
numeros[1].sort()
print(f'Pares: {numeros[0]}')
print(f'Impares: {numeros[1]}')