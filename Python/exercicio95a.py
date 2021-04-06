aux = dict()
jogadores = list()
gols = list()

continuar = 'S'
while continuar == 'S':
    totgols = 0
    aux['Nome'] = str(input('Nome: ')).capitalize()
    quant = int(input('Quantas partidas? '))
    for c in range(0, quant):
        gols.append(int(input(f'Gols da {c + 1}ª partida: ')))
    aux['Gols'] = gols[:]
    aux['Total'] = sum(gols)
    jogadores.append(aux.copy())    
    continuar = str(input('Continuar? [S/N] ')).upper().strip()[0]
    gols.clear()
print('=' * 60)
print(f'{"Código":<10}', end = '')
for d in aux.keys():
    print(f'{d:<20}', end = '')
print()
print('-' * 60)
for pos, jogador in enumerate(jogadores):
    print(f'{pos:<10}', end = '')
    for d in jogador.values():
        print(f'{str(d):<20}', end = '')
    print()
detalhar = 0
while detalhar < len(jogadores):
    detalhar = int(input('Qual jogador deseja detalhar? [999] para sair '))
    if detalhar < len(jogadores):
        print(f'Jogador {jogadores[detalhar]["Nome"]} marcou:')
        for pos, c in enumerate(jogadores[detalhar]['Gols']):
                print(f'{c} gols na {pos + 1}ª partida')

    elif detalhar == 999:
        break
    else:
        print('Jogador inexistente, digite novamente.')
        detalhar = 0