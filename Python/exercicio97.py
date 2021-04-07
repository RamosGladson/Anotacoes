def escreva(a):
    print('~' * (len(a) + 4))
    print(f'{a:^{(len(a) + 4)}}')
    print('~' * (len(a) + 4))

continuar = 'S'
while continuar == 'S':
    escreva(str(input('Mensagem: ')))
    continuar = str(input('Continuar? [S/N] ')).upper().strip()[0]