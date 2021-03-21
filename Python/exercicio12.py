cores = {'limpa' : '\033[m',
        'azul' : '\033[34m',
        'verde' : '\033[32m',
        'vermelho' :'\033[31m'}
preco = int(input('{}Qual o preço do produto?{} '.format(cores['azul'], cores['limpa'])))
desconto = int(input('{}Qual o desconto em percentagem?{} '.format(cores['verde'], cores['limpa'])))
pdesconto = preco*(100-desconto)/100
print('{}O valor com {} porcento de desconto é de {}{}'.format(cores['vermelho'],desconto, pdesconto, cores['limpa']))
