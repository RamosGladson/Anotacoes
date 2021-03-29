primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
i = 0

while i < 10:
    if i == 0: 
        print('Os termos dessa pa são: {}'.format(primeiro), end = ' ')
    else:
        primeiro += razao
        print(primeiro, end = ' ')
    i += 1
   