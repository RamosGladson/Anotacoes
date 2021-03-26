peso = []
maior = 0

for c in range(0, 5):
    aux = int(input('Digite o peso da {}ª pessoa: '.format(c + 1)))
    peso.append(aux)
    if aux >= maior:
        maior = aux
menor = maior
for c in range(0, 5):
    if peso[c] <= menor:
        menor = peso[c]

print('O maior peso foi {}, e o menor peso foi {}'.format(maior, menor))