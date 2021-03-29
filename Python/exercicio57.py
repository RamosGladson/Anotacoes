sexo = ' '

while sexo not in 'MmFf':
    sexo = input('Digite seu sexo: [M/F] ')
    if sexo in 'MmFf':
        print('Sexo {} registrado com sucesso'.format(sexo))
    else:
        print('Não entendi, Digite novamente')