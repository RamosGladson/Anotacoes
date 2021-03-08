salario = int(input('Qual o salário do funcionário em reais? '))
aumento = int(input('Qual o valor de aumento salárial em percentagem? '))
saumento = salario*(aumento+100)/100
print('O salário com {} porcento de aumento é de {} reais'.format(aumento, saumento))