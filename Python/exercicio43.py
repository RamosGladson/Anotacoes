peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
if peso/(altura*altura) < 18.5:
    print('Você está abaixo do peso.') 
elif peso/(altura*altura) < 25:
    print('Você tem o peso ideal.')
elif peso/(altura*altura) < 30:
    print('Você tem sobrepeso.')
elif peso/(altura*altura) < 40:
    print('Você tem obesidade')
else:
    print('Você tem obesidade morbida')