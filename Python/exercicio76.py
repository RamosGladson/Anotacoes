lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('{}'.format('=' * 40))
print('\033[1;31m{:^40}\033[m'.format('Lista de preços'))
print('{}'.format('=' * 40))
for c in range(0, len(lista), 2):
    print('{}{}'.format(lista[c], '.' * (30 - len(lista[c]))), end = '')
    print('R${:>8}'.format(lista[c + 1]))
print('{}'.format('=' * 40))