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
    for c in range(0, num):
        if c < 4 and show:
            print(num - c, 'X ', end='')
        f  *= num - c
    if show:
        print('1 = ', end='')
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
