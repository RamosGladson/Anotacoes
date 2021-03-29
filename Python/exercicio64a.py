q = soma = num = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    q += 1
print('A soma é {} e a quantidade digitada é {}'.format(soma, q))