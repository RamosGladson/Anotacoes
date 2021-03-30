numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = 0
continuar = 'S'
while continuar == 'S':
    print('\033[33m{}'.format('=' * 30))
    print('{:^30}'.format('Programa numero por extenso'))
    print('{}\033[m'.format('=' * 30))    
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('\033[31m{}\033[m'.format('Numero inválido, digite novamente'))
    else:
        print(f'Você digitou \033[4;32m{numeros[numero]}\033[m')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
print('-' * 30)
print('\033[1;41m{:^30}\033[m'.format('FIM'))
print('-' * 30)