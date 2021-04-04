
pessoas = list()
maispesadas = list()
menospesadas = list()
maiorp = 0
menorp = 0
c = 0
aux = list()
continuar = 'S'
while continuar == 'S':
    aux.append(input('Digite nome: '))
    aux.append(int(input('Digite peso: ')))
    pessoas.append(aux[:])
    c += 1
    if c == 1:
        maiorp = aux[1]
        menorp = aux[1]
    else:
        if aux[1] > maiorp:
            maiorp = aux[1]
        elif aux[1] < menorp:
            menorp = aux[1]
    aux.clear()
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]

for d in range(0, len(pessoas)):
    if pessoas[d][1] == maiorp:
        maispesadas.append(d)
    elif pessoas[d][1] == menorp:
        menospesadas.append(d)
print('=' * 30)
print(f'A quantidade de pessoas cadastratas foi de {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorp}KG. ', end = '')
print('As pessoas mais pesadas foram: ', end = '')
for e in range(0, len(maispesadas)):
    if e < len(maispesadas) - 1:
        print(pessoas[maispesadas[e]][0], end = ', ')
    else:
        print(pessoas[maispesadas[e]][0], end = '.')        
        print()
print(f'O menor peso foi de {menorp}KG. ', end = '')
print('As pessoas mais leves foram: ', end = '')
for e in range(0, len(menospesadas)):
    if e < len(menospesadas) - 1:
        print(pessoas[menospesadas[e]][0], end = ', ')
    else:
        print(pessoas[menospesadas[e]][0], end = '.')        
        print()

