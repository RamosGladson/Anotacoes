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

continuar = 'S'
contador = 0
numero = []
pares = []
impares = []
par = 0
impar = 0
while continuar in 'Ss':
    numero.append(int(input('Digite um número: ')))
    if numero[contador] % 2 == 0:
        pares.append(contador)
        par += 1
    else:
        impares.append(contador)
        impar += 1
    continuar = input('Deseja continuar? [S/N]').strip()
    contador += 1
print('Você digitou {} numeros, {} impares e {} pares'.format(contador, impar, par))
print('Os número pares são: ')
for c in range(0, len(pares)):
    print(numero[pares[c]], end = ' ')
print('\nOs numeros impares são: ')
for c in range(0, len(impares)):
    print(numero[impares[c]], end = ' ')