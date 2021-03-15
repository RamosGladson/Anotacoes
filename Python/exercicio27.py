nome = input('Digite seu nome: ')
print('Seu primeiro nome é: {}, seu último nome é: {}'.format(nome.split()[0], nome.split()[len(nome.split()) - 1]))
