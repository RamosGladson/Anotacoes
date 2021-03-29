primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
i = 0

while i < 10:
    if i == 0: 
        print('Os termos dessa pa são: {}'.format(primeiro), end = ' ')
    else:
        primeiro = primeiro + razao
        print(primeiro, end = ' ')
    i += 1
    if i == 10:
        quantidade = int(input('\nMais quantos termos deseja ver? '))
        i = i - quantidade
