#Modulo moeda
from uteis import strings

def moeda(n = 0, simb = 'R$'):
    """
    -> Funcao adiciona R$ ao numero informado.
    Argumento opcional{
    ;param format: pode receber True para mostar R$'n'.
    ;param n: recebe valor
    }
    """
    return f'{simb}{n:.2f}'.replace('.', ',')

def metade(n = 0):
    """
    -> Funcao realiza o calculo da metade de um numero.
    Argumento opcional{
    ;param format: pode receber True para mostar R$'n'.
    ;param n: recebe um numero para calculo da metade.
    }
    return r: retorna metade de n.
    """
    r = n / 2
    return r

def dobro(n = 0):
    """
    -> Funcao realiza o calculo do dobro de um numero.
    Argumento opcional{
    ;param n: recebe um numero para calculo do dobro.
    }
    return r: retorna o dobro de n.
    """
    r = n * 2
    return r


def aumentar(n = 0, i = 0):
    """
    -> Funcao realiza o calculo de um aumento de um
    -> numero em um percentual informado.
    Argumento opcional{
    ;param n: recebe valor para calcular seu aumento.
    ;param i: recebe taxa percentual para aumento de n.
    }
    :return r: retorna valor n acrecido do percentual i.
    """
    r = n * (i/100 + 1)
    return r


def diminuir(n = 0, i = 0):
    """
    -> Funcao realiza o calculo da diminuicao de um
    -> numero em um percentual informado.
    Argumento opcional{
    ;param n: recebe valor para calcular sua diminuicao.
    ;param i: recebe taxa percentual para diminuicao de n.
    }
    :return r: retorna valor n menos o percentual i.
    """
    r = n * (1 - i/100)
    return r

def resumo(n = 0, pa = 0, pm = 0, mostramoeda = False, simb = 'R$'):
    """
    -> Funcao recebe n, aumenta pa e diminui pm.
    Argumento opcional{
    ;param n: recebe valor.
    ;param pa: percentual a aumentar.
    ;param pm: percentual a diminuir.
    }
    ;return: mostra um resumo do valor com aumento
    e diminuicao
    """
    strings.cabecalho('RESUMO DO VALOR', 'azul')
    if mostramoeda == True:
        print(f'{"Preço analisado:":<25} {moeda(n, simb):<5}')
        print(f'{"Dobro do preço:":<25} {moeda(dobro(n), simb):<5}')
        print(f'{"Metade do preço:":<25} {moeda(metade(n), simb):<5}')
        print(f'{f"{pa}% de aumento:":<25} {moeda(aumentar(n, pa), simb):<5}')
        print(f'{f"{pm}% de reduçao:":<25} {moeda(diminuir(n, pm), simb):<5}')

    else:
        print(f'{"Preço analisado:":<25} {n:<5}')
        print(f'{"Dobro do preço:":<25} {dobro(n):<5}')
        print(f'{"Metade do preço:":<25} {metade(n):<5}')
        print(f'{f"{pa}% de aumento:":<25} {aumentar(n, pa):<5}')
        print(f'{f"{pm}% de reduçao:":<25} {diminuir(n, pm):<5}')

    strings.cabecalho('FIM', 'roxo')