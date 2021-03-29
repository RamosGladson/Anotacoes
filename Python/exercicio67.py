
while True:
    num = int(input('Digite um número para começar a taboada: '))
    if  num < 0:
        break
    for c in range(0, 11):
        print(f'{num} x {c} = {num * c}')
print('Até mais!!')