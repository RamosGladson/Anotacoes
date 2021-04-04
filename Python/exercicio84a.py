pessoas = list()
nome = ''
peso = 0
maiorp = 0
menorp = 0
nomes = list()
pesos = list()
aux = list()
continuar = 'S'
maispesadas = list()
maisleves = list()
c = 0
while continuar == 'S':
    nome = input('Digite nome: ')
    peso = int(input('Digite peso: '))
    nomes.append(nome)
    pesos.append(pesos)
    aux.append(nome)
    aux.append(peso)
    pessoas.append(aux[:])
    aux.clear()
    c += 1
    if c == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        elif peso < menorp:
            menorp = peso
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
for e in range(0, len(pessoas)):
    if pessoas[e][1] == maiorp:
        maispesadas.append(e)
    elif pessoas[e][1] == menorp:
        maisleves.append(e)
print(f'A quantidade de pessoas cadastradas foi: {len(pessoas)}')
print(f'As pessoas mais pesadas foram:', end ='')
for d in range(0, len(maispesadas)):
    print(f' {nomes[maispesadas[d]]}', end = ',')
    print()
print(f'As pessoas mais leves foram: ', end = '')
for f in range(0, len(maisleves)):
    print(f' {nomes[maisleves[f]]}', end = ',')


