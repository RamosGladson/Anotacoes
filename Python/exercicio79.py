continuar = 'S'
valores = list()

while continuar == 'S':
    aux = int(input(f'Digite o {i}º valor: '))
    if aux not in valores:
        valores.append(aux)
        continuar = input('Deseja continuar: [S/N] ').upper().strip()[0]
    else:
        continuar = input('Numero já existe, deseja digitar novamente? [S/N] ').upper().strip()[0]
    
    
print(sorted(valores))
