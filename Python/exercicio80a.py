numeros = []

for c in range(0, 5):
    aux = int(input(f'Digite o {c + 1}º número: '))
    if c == 0 or aux > numeros[-1]:
        numeros.append(aux)
        print(f'Adicionado na posição {c}')
    else:
        pos = 0
        while pos < len(numeros):
            if aux < numeros[pos]:
                numeros.insert(pos, aux)
                print(f'Adicionado na posição {pos}')
                break

            else:
                pos += 1

print(numeros)
