i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(i, 9 * r + i + 1, r):
    print(c)
