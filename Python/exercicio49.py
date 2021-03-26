n = int(input('Escolha um número para ter a taboada: '))
print('A taboada do {} é:'.format(n))
for c in range(0, 11):
    print('{} x {} = {}'.format(c, n, c * n))