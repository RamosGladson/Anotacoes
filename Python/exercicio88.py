from random import sample
from time import sleep
jogos = list()
aux = list()
print('=' * 40)
print('{:-^40}'.format('Bem Vindo a lotérica virtual!!'))
print('=' * 40)
quantidade = int(input('Quantos jogos gostaria de gerar? '))
for c in range(0, quantidade):
    aux = sorted(sample(range(1, 61), 6))
    jogos.append(aux[:])
    aux.clear()
print('{:^40}'.format('Gerando números, aguarde...'))
for jogo in jogos:
    print(jogo)
    sleep(1)
print('{:=^40}'.format('FIM'))
