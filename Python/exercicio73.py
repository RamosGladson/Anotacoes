times = ('Flamengo', 'Internacional', 'Atletico Mineiro', 'São Paulo', 'Fluminense', 'Gremio', 'Palmeiras', 'Santos', 'Atletico PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atletico Goianiense', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goias', 'Coritiba', 'Botafogo')
print('{}'.format('|' * 30))
print('{:^30}'.format('Campeonato Brasileiro 2020'))
print('{}'.format('|' * 30))
n = int(input('Quantos colocados deseja exibir? '))
print('{}'.format('Os {} primeiros colocados foram: '.format(n)), end = '')
for count in range(0, n):
    if count in range(0, n - 1):
        print('{}'.format(times[count]), end = ', ')
    else:
        print('{}.'.format(times[count]))
u = int(input('Quantidade de ultimos colocados deseja exibir? '))
print('{}'.format('Os {} últimos colocados formam: '.format(u)), end = '')
ignorar = len(times) - u
for count in range(ignorar, len(times)):
    if count in range(ignorar, len(times) - 1):
        print('{}'.format(times[count]), end = ', ')
    else:
        print('{}.'.format(times[count]))
print('{}'.format('Segue a lista em ordem alfabetica: {}'.format(sorted(times))))
encontrar = input('Qual time deseja encontrar? ')
print('{}'.format('{} está na {}ª posição'.format(encontrar, times.index(encontrar) + 1)))