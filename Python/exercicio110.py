from uteis import moeda

simb = str()
n = float(input('Digite o preço R$: '))
pa = float(input('Taxa aumento: '))
pm = float(input('Taxa diminuir: '))
if input('Exibir símbolo de moeda? [S/N] ').upper().strip()[0] == 'S':
    mostramoeda = True
    simb = str(input('Qual símbulo usar? [R$] '))
else:
    mostramoeda = False
moeda.resumo(n, pa, pm, mostramoeda, simb)