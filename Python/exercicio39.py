from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
if ano > date.today().year:
    print('Ano inválido!!')
else:
    if ano > (date.today().year - 18):
        print('Ainda não chegou sua vez de se alistar, espere {}, ainda faltam {} anos'.format(ano + 18, ano + 18 - date.today().year))
    elif ano == (date.today().year - 18):
        print('Sua hora chegou, aliste-se já!!')
    else:
        print('Deveria ter se alistado em {}, você está atrazado {} anos'.format(ano + 18, date.today().year - (ano + 18)))

