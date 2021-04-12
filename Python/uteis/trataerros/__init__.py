#modulo erros

def leiaint(frase):
    """
    -> Funcao lê um numero e verifica se é inteiro.
    ;param frase: recebe uma frase a ser exibida.
    ;return n: retorna um numero inteiro.
    """
    while True:
        try:
            n = int(input(f'{frase}'))
        except (TypeError, ValueError):
            print('\033[31mErro, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuario interrompeu.')
            return 0
        else:
            return n

def leiafloat(frase):
    """
    -> Funcao lê um numero e verifica se é real.
    ;param frase: recebe uma frase a ser exibida.
    ;return m: retorna um numero real.
    """
    while True:
        try:
            m = float(input(f'{frase}'))
        except (TypeError, ValueError):
            print('\033[31mErro, digite um numero real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuario interrompeu.')
            return 0
        else:
            return m