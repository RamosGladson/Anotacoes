from datetime import date
pessoas = []
ma = 0
me = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c + 1)))
    if ano > date.today().year - 21:
        print('Menor de idade')
        me += 1
    else:
        print('Maior de idade')
        ma += 1
print('Temos {} pessoas menor de idade e {} maior de idade'.format(me, ma))
    