from random import randint
computador = randint(0,10)
jogador = int(input('Digite um número entre 0 e 10: '))
tentativa = 1

while jogador != computador:
    jogador = int(input('Você ainda não acertou, digite novamente: '))
    tentativa += 1

print('Você precisou de {} tentativas para acertar'.format(tentativa))