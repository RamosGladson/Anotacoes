matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = somaterceira = somapar = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número inteiro da linha {linha + 1} e coluna {coluna + 1} '))

for linha in matriz:
    somaterceira += linha[2]
    for valor in linha:
        if valor % 2 == 0:
            somapar += valor
      
for valor in matriz[1]:
    if valor > maior:
        maior = valor
    
print(f'Soma dos pares {somapar}')

print(f'Soma terceira {somaterceira}')

print(f'Maior da segunda linha {maior}')
