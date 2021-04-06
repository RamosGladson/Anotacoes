from datetime import date
trabalhador = dict()

trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = date.today().year - (int(input('Ano nascimento: ')))
trabalhador['CTPS'] = int(input('CTPS: '))

if trabalhador['CTPS'] !=0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: '))
#    trabalhador['Aposentadoria'] = trabalhador['Idade'] + 35 - (date.today().year - trabalhador['Contratação'])
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + trabalhador['Contratação'] + 35 - date.today().year
for k,v in trabalhador.items():
    print(f'{k} tem o valor {v}')