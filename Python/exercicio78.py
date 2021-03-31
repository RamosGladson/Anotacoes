lista = list()

for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(f'O maior número digitado foi: {max(lista)} e sua posição é: {lista.index(max(lista))}')
print(f'O menor número digitado foi: {min(lista)} e sua posição é: {lista.index(min(lista))}')