digitar = 'S'
valores = []
i = 0
media = 0
soma = 0
maior = 0
menor = 0
while digitar in 'Ss':
    valores.append(float(input('Digite um valor: ')))
    soma += valores[i]
    if i == 0:
        maior = valores[i]
        menor = valores [i]
    else:
        if maior < valores[i]:
            maior = valores[i]
        if menor > valores[i]:
            menor = valores[i]
    i += 1
    digitar = input('Gostaria de continuar? [S/N] ')

media = soma/len(valores)
print('A média dos valores foi {:.2f}\n O menor valor foi {}, e o maior {}'.format(media, menor, maior))