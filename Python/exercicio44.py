produto = float(input('Digite o valor do produto: '))
print('Qual a forma de pagamento? Escolha uma das opções abaixo:')
print('\033[31m1 - À vista Dinheiro ou Cheque')
print('\033[32m2 - À vista no cartão')
print('\033[33m3 - Em 2X no cartão')
print('\033[34m4 - Em 3X ou mais no cartão\033[m')
escolha = int(input('Digite a opção desejada: '))
if escolha < 1 or escolha > 4:
    print('Opção inválida!!')
else:
    if escolha == 1:
        print('Você escolheu pagamento à vista (dinheiro ou cheque.)')
        print('O valor a pagar é de {}{} reais'.format('\033[31m', produto*0.90))
    elif escolha == 2:
        print('Você escolheu pagamento à vista no cartão.')
        print('O valor a pagar é de {}{} reais'.format('\033[32m', produto*0.95))
    elif escolha == 3:
        print('Você escolheu pagamento em 2X no cartão.')
        print('O valor a pagar é de {}{}'.format('\033[33m', produto))
    else:
        print('Você escolheu pagamento em 3x ou mais no cartão.')
        print('O valor a pagar é de {}{}'.format('\033[34m', produto*1.20))
