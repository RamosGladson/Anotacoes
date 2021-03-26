frase = input('Teste de palindromo, digite sua frase: ')
frase = frase.split()
frase = ''.join(frase)
inverso = ''

for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]

if inverso == frase:
    print('É palindromo')
else:
    print('Não é palindromo')