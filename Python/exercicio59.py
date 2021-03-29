primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
operador = 0

while operador != 5:
        print('-' * 50)
        print('Suas opções são: ')
        print('Digite 1 para somar')
        print('Digite 2 para multiplicar')
        print('Digite 3 para Saber o maior número')
        print('Digite 4 para entrar novos números')
        print('Digite 5 para sair')
        operador =  int(input('Digite sua opção: '))
        if operador == 1:
            print('A soma é: {}'.format(primeiro + segundo))
        elif operador == 2:
            print('A multiplicação é: {}'.format(primeiro * segundo))
        elif operador == 3:
            if primeiro > segundo:
                print('{} é maior que {}'.format(primeiro, segundo))
            elif primeiro == segundo:
                print('Eles são iguais')
            else:
                print('{} é maior que {}'.format(segundo, primeiro))
        elif operador == 4:
            primeiro = int(input('Digite o primeiro número: '))
            segundo = int(input('Digite o segundo número: '))
        elif operador == 5:
            print('-' * 22, 'BYE', '-' * 22)        
