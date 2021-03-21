frase = str(input('Digite uma frase: ')).strip()
print('A quantidade de vezes em que aparece a letra "a" maiuscula ou minuscula é: {} vezes.\nA quantidade de vezes maiúscula é {} vezes \ne a quantidade de vezes minúscula é {} vezes.'.format(frase.upper().count('A'), frase.count('A'), frase.count('a')))
print('Ela aparece a primeira vez na posição {}'.format(frase.upper().find('A')+1))
print('Ela aparece a última vez na posição {}'.format(frase.upper().rfind('A')+1))