vel = int(input('Qual a velocidade do carro? '))
print('A velocidade do carro é {}'.format(vel))

if vel > 80:
    print('Você foi multado! Deverá pagar {} Reais'.format((vel-80)*7))
else:
    print('Pode seguir, sem multa.')
