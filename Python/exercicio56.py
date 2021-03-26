nome = []
idade = []
sexo = []
soma = 0
quantidade = 0
maior = 0

for c in range(0, 4):
    nome.append(input('Digite seu nome: '))
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(input('Digite seu sexo[f/m]: '))    
    soma =  soma + idade[c]
    if sexo[c] == 'f' and idade[c] < 21:
        quantidade += 1
    if sexo[c] == 'm' and idade[c] >= maior:
        maior = idade[c]
        maisvelho = c
        
media = soma / len(idade)

print('A média de idade do grupo é {}, o homem mais velho é {} e a quantidade de mulheres com menos de 21 é {}'.format(media, nome[maisvelho], quantidade))