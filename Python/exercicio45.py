from random import randint
print('=' * 35)
print('\33[35mEsse é um jogo de jokenpô')
print('Para escolher pedra, digite 1')
print('Para escolher papel, digite 2')
print('Para escolher tesoura, digite 3')
jogador = int(input('Digite sua escolha: '))
computador = randint(1, 3)
lista = ['pedra', 'papel', 'tesoura']
if jogador < 1 or jogador > 3:
    print('O valor deve estar entre 1 e 3')
else:
    print('\033[mVocê escolheu {} e o computador escolheu {} '.format(lista[jogador - 1], lista[computador - 1]))
    if jogador == computador:
        print('Houve um empate')
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print('\033[32mParabéns!! Você ganhou!!!!')
    else:
        print('\033[31mVocê perdeu, melhor sorte na próxima vez!!')


