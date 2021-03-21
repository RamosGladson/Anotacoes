a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triangulo!!')

else:
    print('Não é possível formar um triangulo!!')