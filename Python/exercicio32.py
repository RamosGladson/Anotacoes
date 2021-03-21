from datetime import date
ano = int(input('Digite um ano para pesquisa, ou digite 0 para ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%100 == 0:
    print('Ano termina em 00')
    if ano%400 == 0:
        print('{} é bissexto'.format(ano))
    else:
        print('{} não é bissexto'.format(ano))

else:
    print('Ano não termina em 00')
    if ano%4 ==0:
        print('{} é bissexto'.format(ano))
    else:
        print('{} não é bissexto'.format(ano))