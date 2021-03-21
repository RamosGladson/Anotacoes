dist = float(input('Qual a distância da viagem? '))
print('Valor a pagar é {:.2f} reais'.format(dist*0.45) if dist > 200 else 'Valor a pagar é {:.2f} reais'.format(dist*0.50))