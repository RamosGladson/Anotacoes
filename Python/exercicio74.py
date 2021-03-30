from random import randint
aleatorios = []
maior = menor = 0
quantidade = int(input('Quantos números aleatórios gostaria de gerar? '))
for c in range (0, quantidade):
    aux = randint(0, 10)
    aleatorios.append(aux)
    if c == 0:
        maior = aux
        menor = aux
    else:
        if aux > maior:
            maior = aux
        if aux < menor:
            menor = aux
print('{}'.format('Os numeros gerados foram {}'.format(aleatorios)))
print('{}'.format('O maior número foi {}'.format(maior)))
print('{}'.format('O menor número foi {}'.format(menor)))