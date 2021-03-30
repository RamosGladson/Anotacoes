palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
print('{}'.format('-' * 30))
for c in range(0, len(palavras)):
    print('{}'.format('Na palavra {} temos:'.format(palavras[c].upper())), end = '')
    if palavras[c].count('a') > 0:
        print('{}'.format(' a'), end = '')
    if palavras[c].count('e') > 0:
        print('{}'.format(' e'), end = '')
    if palavras[c].count('i') > 0:
        print('{}'.format(' i'), end = '')
    if palavras[c].count('o') > 0:
        print('{}'.format(' o'), end = '')
    if palavras[c].count('u') > 0:
        print('{}'.format(' u'), end = '') 
    print('.')
print('{}'.format('-' * 30))