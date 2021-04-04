pessoas = list()
aux = list()
continuar = 'S'
c = maiorp = menorp = 0
while continuar == 'S':
    aux.append(str(input('Nome: ')))
    aux.append(int(input('Peso: ')))
    pessoas.append(aux[:])
    if len(pessoas) == 1:
        maiorp = aux[1]
        menorp = aux[1]
    else:
        if aux[1] > maiorp:
            maiorp = aux[1]
        if aux[1] < menorp:
            menorp = aux[1]
    aux.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print(f'A quantidade de pessoas cadastradas foram {len(pessoas)}.')
print('As pessoas mais pesadas foram: ', end = '')
for pesado in pessoas:
    if pesado[1] == maiorp:
        print(pesado[0], end = ' ')
print(f'. Com {maiorp} quilos')
print('As pessoas mais leves foram: ', end = '')
for leves in pessoas:
    if leves[1] == menorp:
        print(leves[0], end = ' ')
print(f'. Com {menorp} quilos')