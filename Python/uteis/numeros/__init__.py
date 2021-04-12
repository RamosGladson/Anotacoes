#Modulo numeros

def fatorial(n = 1):
    """
    -> Funcao recebe um numero e retorna seu fatorial.
    Argumento opcional{
    ;param n: recebe um numero para calculo de fatorial.
    }
    ;return r: retorna fatorial do numero n.
    Funcao desenvolvida por Gladson Carneiro Ramos.
    """
    r = 1
    for c in range(n, 0, -1):
        r *= c
    return r

def validafloat(frase, n):
    """
    -> Funcao para validacao de numero real.
    ;param frase: exibe frase inicial para
    digitar numero.
    ;param n: recebe suposto numero real.
    """
    while n.isalpha() or n == '':
        print('Numero inválido, digite novamente.')
        n = input(f'{frase}').strip()
    return n