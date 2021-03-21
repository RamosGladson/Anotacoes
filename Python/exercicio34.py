sal = float(input('Digite o salário do funci: '))
if sal > 1250:
    sal = sal*1.10
else:
    sal = sal*1.15

print('Novo salário é: {:.2f} reais'.format(sal))