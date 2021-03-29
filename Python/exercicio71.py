sobra = quant1 = quant10 = quant20 = quant50 = 0
while True:
    print('|' * 30)
    print('{:^30}'.format('Bem vindo ao banco do SALIM'))
    print('|' * 30)
    saque = int(input('Qual valor deseja sacar? '))
    print('Saque de {} realizado com sucesso'.format(saque))
    quant50 = saque // 50
    sobra = saque % 50
    quant20 = sobra // 20
    sobra = sobra % 20
    quant10 = sobra // 10
    sobra = sobra % 10
    quant1 = sobra // 1
    print('{} notas de R$ 50'.format(quant50))
    print('{} notas de R$ 20'.format(quant20))
    print('{} notas de R$ 10'.format(quant10))
    print('{} notas de R$ 1'.format(quant1))
    continuar = input('Deseja fazer outro saque? [S/N] ').upper().strip()[0]
    
    if continuar != 'S':
        break