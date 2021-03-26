n = int(input('Digite um número para saber se é primo: '))
m = 0
for c in range(2, n):
    if n % c == 0:
        m += 1 
if m:
    print('Não é primo!')
else:
    print('É primo!!')