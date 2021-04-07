def lin():
    print('-=' * 25)


def maior(* numeros):
    mais = 0
    lin()
    print('Analisando os valores passados...')
    for c in numeros:
        if c > mais:
            mais = c
        print(c, end=' ')
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {mais}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()