numeros =  list()
i = aux = 0
for c in range(0, 5):
    aux = int(input(f'digite o {c + 1}º número: '))
    if c == 0:
        numeros.append(aux)
    else:
        if aux < numeros[0]:
            numeros.insert(0, aux)
        elif aux > numeros[-1]:
            numeros.append(aux)
        else:
            for d in range(0, len(numeros)):
                if aux > numeros[d]:
                    print(end = '')
                else:
                    numeros.insert(d, aux)
                    break
print(numeros)

            

