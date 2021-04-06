alunos = dict()

alunos['Nome'] = str(input('Nome: '))
alunos['Media'] = float(input('Média: '))
if alunos['Media'] < 7:
    alunos['Situacao'] = 'Reprovado'
else:
    alunos['Situacao'] = 'Aprovado'
    
for k,v in alunos.items():
    print(f'{k:<10} é igual a {v:<10}')