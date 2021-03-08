km = float(input('Qual a kilometragem rodada? '))
dias = int(input('Qual a quantidade de dias? '))
#ckm = km * 0.15
#cdias = dias * 60
print('Você rodou {}km em {} dias, deve pagar {} reais'.format(km, dias, (km*0.15) + (dias*60) ))