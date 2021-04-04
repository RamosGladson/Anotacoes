matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o item da linha {l + 1} e coluna {c + 1}: '))

for linha in matriz:
    print(linha)
