preco = int(input('Qual o preço do produto? '))
desconto = int(input('Qual o desconto em percentagem? '))
pdesconto = preco*(100-desconto)/100
print('O valor com {} porcento de desconto é de {}'.format(desconto, pdesconto))
