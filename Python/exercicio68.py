from random import randint
print('=-=' * 10)
print('Vamos jogar par ou impar')
print('=-=' * 10)

while True:
    escolha = input('Escolha [P]ar ou [I]mpar ').strip().upper()[0]
    num = int(input('Digite um número entre 0 e 10: '))
    print('-' * 30)
    computador = randint(0, 10)
    if 0 < num < 11 and escolha in 'PI':
        print(f'Você jogou o número {num}')
        print(f'O computador jogou o número {computador}')
        if (num + computador) % 2 == 0:
            print('Deu par!')
            if escolha == 'P':
                print('Você escolheu par e ganhou')
                print('Vamos jogar de novo!')
                print('.' * 30)
            else:
                print('Você escolheu impar e perdeu!!')
                print('.' * 30)
                break
        else:
            print('Deu impar!')
            if escolha == 'I':
                print('Você escolheu impar e ganhou')
                print('Vamos jogar de novo!')
                print('.' * 30)
            else:
                print('Você escolheu par e perdeu!!')
                print('.' * 30)
                break
    else:
        print('Número ou opção inválida')
