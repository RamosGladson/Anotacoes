prim = float(input('Digite o primeiro valor: '))
seg = float(input('Digite o segundo valor: '))

if prim == seg:
    print('Não existe valor maior, os doi são iguais.')
elif prim > seg:
    print('O primeiro valor, {}, é maior'.format(prim))
else:
    print('O segundo valor, {}, é maior'.format(seg))

