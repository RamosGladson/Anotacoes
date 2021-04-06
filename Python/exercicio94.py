pessoas = list()
aux = dict()
somaidade = 0
continuar = 'S'
print('=' * 45)
print(f'{"Bem vindo!!":^45}')
print('=' * 45)
while continuar == 'S':
    aux['Nome'] = str(input('Nome: ')).capitalize().strip()
    aux['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if aux['Sexo'] in 'MF':        
        aux['Idade'] = int(input('Idade: '))
        pessoas.append(aux.copy())
        continuar = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    else:
        print('Sexo digitado errado, digite novamente.')
print('=' * 45)
for c in pessoas:
    somaidade += c['Idade']
print(f'A quantidade de pessoas cadastrada foi: {len(pessoas)}')
print(f'A media de idade é {somaidade / len(pessoas):.2f}')
print('As mulheres do grupo são: ', end ='')
for c in pessoas:
    if c['Sexo'] == 'F':
        print(f'[{c["Nome"]}]', end= '')
print()
print('As pessoas com idade acima da média foram: ')
for c in pessoas:
    if c['Idade'] > somaidade / len(pessoas):
        print(f'[{c["Nome"]:<8} sexo: {c["Sexo"]:<5} idade {c["Idade"]}]')
print('=' * 45)
print(f'{"Até mais!!":^45}')
print('=' * 45)
