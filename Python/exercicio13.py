cores = {'ciano' : '\033[36m',
        'amarelo' : '\033[33m',
        'limpa' : '\033[m'
        }
salario = int(input('{}Qual o salário do funcionário em reais?{} '.format(cores['ciano'], cores['limpa'])))
aumento = int(input('{}Qual o valor de aumento salárial em percentagem?{} '.format(cores['amarelo'], cores['limpa'])))
saumento = salario*(aumento+100)/100
print('O salário com {}{}{} porcento de aumento é de {} reais'.format(cores['ciano'], aumento, cores['limpa'], saumento))