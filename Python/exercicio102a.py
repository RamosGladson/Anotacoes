#Programa fatorial

def fat(num = 1, show = False):
    """
    -> Funcao para calculo de fatorial
    Argumentos opcionais:{
        ;param num:  recebe o numero a ser fatorado.
        ;param show: mostra ou nao o processo de
        fatoracao.
    }
    ;return: Retorna o fatorial de num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                 print(' = ', end='')
        f *= c
    return f

#Main

#Entra numero a ser fatorado
n = int(input('Qual numero fatorar: '))

#Verifica show
while True:
    s = str(input('Deseja mostrar o processo? [S/N]')).upper().strip()[0]
    if s == 'S':
        s = True
        break
    elif s == "N":
        s = False
        break
    else:
        print('Digite apenas S ou N')

#Chamada de função para fatoração
print(fat(n, s))
