from random import randint

def sorteia(a):
    print(f'Sorteando {a} valores da lista:', end=' ')
    for c in range(0, a):
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
    print('Pronto!')

def somaPar(num):
    print(f'Somando os valores pares de {numeros}, temos:', end=' ')
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(soma)

#main
numeros = list()
sorteia(int(input('Quantos numeros sortear? ')))
somaPar(numeros)