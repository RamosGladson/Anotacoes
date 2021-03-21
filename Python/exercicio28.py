import random
num = int(input('Estou pensando em um número entre zero e cinco, tente adivinhar: '))
sort = random.randrange(0, 6)
if num > 5:
    print('Você digitou um número inválido!')
else:
    print('O numero sorteado foi {}, e você digitou {}'.format(sort, num))
    if num == sort:
        print('Você tem muita sorte')
    else:
        print('Não foi dessa vez')

