aluno = 0
nomenotas = list()
auxnome = list()
auxnota = list()
qual = 0
continuar = 'S'
print('=' * 40)
print('{:^40}'.format('Entre com os nomes e notas.'))
print('=' * 40)
while continuar == 'S':
    auxnome.append(str(input('Nome: ')))
    auxnota.append(float(input('1ª nota: ')))
    auxnota.append(float(input('2ª nota: ')))
    auxnome.append(auxnota[:])
    nomenotas.append(auxnome[:])
    auxnome.clear()
    auxnota.clear()
    continuar = str(input('Continuar? [S/N] ')).upper().strip()[0]
print('-' * 40)
print('{:^40}'.format('Boletim'))
print('-' * 40)
for pos, aluno in enumerate(nomenotas):
    print('{:<4}  {:<25}  {:<4.2f}'.format(pos, aluno[0].capitalize().strip(), (aluno[1][0] + aluno[1][1])/2))
print('-=' * 20)
while aluno != 999:
    aluno = int(input('Deseja detalhar qual aluno? [999 para sair] '))
    if aluno < len(nomenotas):
        print(nomenotas[aluno])
    elif aluno != 999:
        print('Inexistente, digite novamente.')
    else:
        print('=' * 40)
        print('{:^40}'.format('Até mais'))
        print('=' * 40)