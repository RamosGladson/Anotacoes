times = ('Flamengo', 'Internacional', 'Atletico Mineiro', 'São Paulo', 'Fluminense', 'Gremio', 'Palmeiras', 'Santos', 'Atletico PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atletico Goianiense', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goias', 'Coritiba', 'Botafogo')
print('{}'.format('|' * 30))
print('{:^30}'.format('Campeonato Brasileiro 2020'))
print('{}'.format('|' * 30))
n = int(input('Quantos colocados deseja exibir? '))
print('{}'.format('Os {} primeiros colocados foram: '.format(n)), end = '')
for exibir in times[:n]:
    print(exibir, end = ' | ')
print(' ')
n = int(input('Quantidade de ultimos colocados deseja exibir? '))
print('{}'.format('Os {} últimos colocados formam: '.format(n)), end = '')
n -= 2 * n
for exibir in times[n:]:
    print(exibir, end = ' | ')
print(' ')
print('{}'.format('Segue a lista em ordem alfabetica: {}'.format(sorted(times))))
encontrar = input('Qual time deseja encontrar? ').strip().capitalize()
print('{}'.format('{} está na {}ª posição'.format(encontrar, times.index(encontrar) + 1)))