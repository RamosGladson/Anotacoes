jogador = dict()
jogador['Nome'] = str(input('Nome: '))
jogador['Nº partidas'] = int(input('Quantas partidas: '))
jogador['Total de gols'] = 0
for c in range(0, jogador['Nº partidas']):
    jogador['Gols partida ' + str(c + 1)] = int(input(f'Gols partida {c + 1}: '))
    jogador['Total de gols'] += jogador['Gols partida ' + str(c + 1)]
print(jogador)
for k,v in jogador.items():
    print(f'{k}: {v}')