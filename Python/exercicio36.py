casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o salário? '))
anos = float(input('Financiamento em quantos anos? '))

if casa/(anos*12) > salario * 0.3:
    print('Sinto muito, seu financiamento não foi aprovado. Parcela maior que permitido.')
else:
    print('Financiamento aprovado, parcela mensal de {:.2f}'.format(casa/(anos*12)))


