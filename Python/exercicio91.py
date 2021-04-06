from random import randint
from operator import itemgetter
from time import sleep
ranking = list()
jogadores = {'Jogador1': randint(1, 6),
            'Jogador2': randint(1, 6),
            'Jogador3': randint(1, 6),
            'Jogador4': randint(1, 6),
            'Jogador5': randint(1, 6),
            'Jogador6': randint(1, 6)}

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, j in enumerate(ranking):
    print(f'{(i + 1):>2}º Lugar: {j[0]} com {j[1]}')
    sleep(1)