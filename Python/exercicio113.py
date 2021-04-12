from uteis import trataerros

a = trataerros.leiaint('Digite um numero inteiro: ')
b = trataerros.leiafloat('Digite um numero real: ')
print(f'Você digitou o numero inteiro {a} e o numero real {b:.2f}')