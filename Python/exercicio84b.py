pessoas = list()
maiorp = 0
menorp = 0
aux = list()
continuar = 'S'
while continuar == 'S':
    aux.append(input('Digite nome: '))
    aux.append(int(input('Digite peso: ')))
    pessoas.append(aux[:])
    if len(pessoas) == 0:
        maiorp = aux[1]
        menorp = aux[1]
    else:
        if aux[1] > maiorp:
            maiorp = aux[1]
        if aux[1] < menorp:
            menorp = aux[1]
    aux.clear()
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
print('=' * 30)
print(f'A quantidade de pessoas cadastratas foi de {len(pessoas)} pessoas')
print(f'O maior peso foi {maiorp}. As pessoas mais pesadas foram: ', end = '')
for p in pessoas:
    if p[1] == maiorp:
        print(f'{p[0]} ', end = '')
print()
print(f'O menor peso foi {menorp}. As pessoas mais leves foram: ', end = '')
for p in pessoas:
    if p[1] == menorp:
        print(f'{p[0]}', end = '')
