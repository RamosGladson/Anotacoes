print('-'* 20)
numero = int(input('Digite um número para ser convertido: '))
print('Você terá 3 opções, conforme abaixo:')
print('\033[31m 1 - Binário')
print('\033[32m 2 - Octal')
print('\033[33m 3 - Hexadecimal\033[m')
escolha = int(input('Qual a sua escolha? \033[31m1, \033[32m2 ou \033[33m3?\033[m'))

if escolha < 1 or escolha > 3:
    print('Número inválido')
else:
    if escolha == 1:
        print('O número {} em binário é {}{}'.format(numero, '\033[31m', bin(numero)[2:]))
    elif escolha == 2:
        print('O número {} em octal é {}{}'.format(numero, '\033[32m', oct(numero)[2:]))
    else:
        print('O número {} em hexadecimal é {}{}'.format(numero, '\033[33m', hex(numero)[2:]))

