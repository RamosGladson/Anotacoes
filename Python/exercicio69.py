mulheres = homens = mais18 = i = 0
idade = []
sexo = []

while True:
    print('=' * 30)
    print('{:^30}'.format('Cadastre uma pessoa'))
    print('=' * 30)
    auxidade = int(input('Digite a idade: '))
    auxsexo = input('Digite o sexo: [M/F] ').upper().strip()[0]
    print('=' * 30)
    if auxidade < 0 or auxidade > 150 or auxsexo not in 'MF':
        print('Idade ou sexo preenchido errado, tente novamente')
    else:
        idade.append(auxidade)
        sexo.append(auxsexo)
        if idade[i] > 18:
            mais18 += 1
        if sexo[i] == 'M':
            homens += 1
        if sexo[i] == 'F' and idade[i] < 20:
            mulheres += 1
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if continuar == 'N':
            break
        else:
            i += 1

print('=-=' * 10)
print(f'{mais18} pessoas tem mais de 18')
print(f'{homens} homens cadastrados')
print(f'{mulheres} mulheres com menos de 20')
print('=-=' * 10)