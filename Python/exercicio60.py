numero = int(input('Digite um número: '))
fatorial = 1
print('{}! = '.format(numero), end = '')
while numero >= 1:
    fatorial *= numero
    print(numero, 'x ' if numero != 1 else '= ', end = '')
    numero -= 1

print(fatorial)