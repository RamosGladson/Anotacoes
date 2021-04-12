from uteis import moeda
from uteis import numeros

simb = str()

frase = 'Digite o preço R$: '
n = input(f'{frase}').replace(',', '.').strip()
n = numeros.validafloat(frase, n)
n = float(n)

frase = 'Taxa aumento: '
pa = input(f'{frase}').replace(',', '.').strip()
pa = numeros.validafloat(frase, pa)
pa = float(pa)

frase = 'Taxa diminuir: '
pm = input(f'{frase}').replace(',', '.').strip()
pm = numeros.validafloat(frase, pm)
pm = float(pm)


if input('Exibir símbolo de moeda? [S/N] ').upper().strip()[0] == 'S':
    mostramoeda = True
    simb = str(input('Qual símbulo usar? [R$] ')).strip()
    if simb == '':
        simb = 'R$'
else:
    mostramoeda = False
moeda.resumo(n, pa, pm, mostramoeda, simb)