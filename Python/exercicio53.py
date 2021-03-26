frase = input('Digite uma frase para o teste de palindromo: ')
frase = frase.split()
frase = ''.join(frase)
print(frase)
m = 0

for c in range(0, len(frase)//2):
    if frase[c] != frase[len(frase) - c - 1]:
        m += 1
if m:
    print('Não é um palindromo')
else:
    print('É um palindromo!')