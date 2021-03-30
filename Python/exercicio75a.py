valores = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')) )

print(f'Você digitou {valores}')
print(f'O numero 9 apareceu {valores.count(9)} vezes')
print('Os números pares foram: ')
for n in valores:
    if n % 2 == 0:
        print(n)