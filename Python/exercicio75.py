quantidade = int(input('Quantos valores deseja digitar? '))
valor = []
pares = []
tres = nove = 0
for c in range(0, quantidade):
    aux = int(input('Digite o {}º valor: '.format(c + 1)))
    valor.append(aux)
    if aux % 2 == 0:
        pares.append(c)
if 3 in valor:
    print(f'O primeiro numero 3 digitado foi na {valor.index(3) + 1}ª posição e')
else:
    print('O valor 3 não foi digitado')
if 9 in valor:
    print(f'O número 9 apareceu {valor.count(9)} vezes')
else:
    print('Não foi digitado número 9')
if len(pares) == 0:
    print('Não temos numeros pares')
else:
    print(f'Temos {len(pares)} numeros pares e foram: ')
    for c in range(0, len(pares)):
        print(valor[pares[c]])
