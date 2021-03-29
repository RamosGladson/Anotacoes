maisdemil = i = soma = 0
nome = []
preco = []
maior = []
menor = []
nomemenor = ''
while True:
    print('+' * 30)
    auxn = input('Digite o nome do produto: ')
    nome.append(auxn)
    auxp = int(input('Digite o preço do produto: '))
    preco.append(auxp)
    print('+' * 30)
    soma += auxp
    if auxp > 1000:
        maisdemil += 1
    if i == 0:
        menor = auxp
        maior = auxp
    else:
        if auxp > maior:
            maior = auxp
        if auxp < menor:
            menor = auxp
            nomemenor = auxn
    i += 1
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar != 'S':
        break
print(f'A soma deu {soma}.')
print(f'{maisdemil} produtos custaram mais de mil reais.')
print(f'{nomemenor} é o nome do produto mais barato')