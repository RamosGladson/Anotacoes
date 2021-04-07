def bv(a):
    print('=' * 50)
    print(f'{a:^50}')
    print('=' * 50)

def calarea(a, b):
    area = a * b
    print(f'A área do terreno {a} X {b} é de {area} metros quadrados')

#Programa principal
bv('Bem vindo ao cálculo de área')
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
calarea(a, b)

