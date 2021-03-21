prim = int(input('Digite o primeiro número: '))
seg = int(input('Digite o segundo número: '))
ter = int(input('Digite o terceiro número: '))

if prim > seg and prim > ter:
    print('O maior número é {}'.format(prim))
    if seg < ter:
        print('O menor é {}'.format(seg))
    else:
        print('O menor é {}'.format(ter))
elif seg > prim and seg > ter:
    print('O maior número é {}'.format(seg))
    if prim < ter:
        print('O menor é {}'.format(prim))
    else:
        print('O menor é {}'.format(ter))
else:
    print('O maior número é {}'.format(ter))
    if prim < seg:
        print('O menor é {}'.format(prim))
    else:
        print('O menor é {}'.format(seg))