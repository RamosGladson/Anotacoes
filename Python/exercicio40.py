n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

if n1 > 10 or n2 >10:
    print('Nota inválida')
else:
    if (n1 + n2)/2 < 5:
        print('Reprovado!!')
    elif 5 <= (n1 + n2)/2 < 7:
        print('Recuperação')
    else:
        print('Aprovado')