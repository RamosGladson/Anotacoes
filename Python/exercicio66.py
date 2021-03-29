i = soma = 0
while True:
    num = int(input('Digite um número [999 para sair]: '))
    if num == 999:
        break 
    soma += num
    i += 1
print(f'Você digitou {i} numeros e a soma entre eles foi {soma}')