palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
print('{}'.format('-' * 30))

for c in palavras:
    print(f'A palavra {c} tem: ', end = '')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end = ' ')
    print('')



print('{}'.format('-' * 30))