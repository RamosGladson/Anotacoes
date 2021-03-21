a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))

if a > b + c or b > a + c or c > a + b:
    print('\033[31mIsso não é um triangulo')
else:
    if a == b and b == c:
        print('Esse é um triangulo \033[33mequilátero.')
    elif a == b or a == c or b == c:
        print('Esse é um triangulo \033[33misóceles.')
    else:
        print('Esse é um triangulo \033[33mescaleno.')