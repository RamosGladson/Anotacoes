from time import sleep
from random import randint
lista = list()
jogos = list()
num = 0
print('=' * 40)
print('{:-^40}'.format('Bem Vindo a lotérica virtual!!'))
print('=' * 40)
quantidade = int(input('Quantos jogos gostaria de gerar? '))
for c in range(0, quantidade):
    i = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            i += 1
        if i == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('{:^40}'.format('Gerando números, aguarde...'))
for jogo in jogos:
    print(jogo, end=' ')
    sleep(1)
print('{:=^40}'.format('FIM'))
