#Modulo string

def cabecalho(msg = 'Bem Vindo!', cor = 'sem'):
    """
    -> Funcao gera um cabecalho conforme msg.
    Argumento opcional{
    ;param msg: Caso nada for passado, mostra
    'Bem Vindo!'.
    ;param cor: Caso nao informado, mostra cores
    padrao do terminal.
    }
    """
    cores = {   'sem':      '\033[m',
                'vermelho': '\033[31m',
                'verde':    '\033[32m',
                'amarelo':  '\033[33m',
                'azul':     '\033[34m',
                'roxo':     '\033[35m',
                'ciano':    '\033[36m',
                'cinza':    '\033[37m',
                'branco':   '\033[7;40m'
    }
    tam = 35
    print(f'{cores[cor]}{"=" * tam}')
    print(f'{msg:^{tam}}')
    print(f'{"=" * tam}', end='')
    print(cores['sem'])

def menu(* itens, cor = 'sem'):
    """
    -> Funcao gera um cabecalho conforme msg.
    Argumento opcional{
    ;param msg: Caso nada for passado, mostra
    'Bem Vindo!'.
    ;param cor: Caso nao informado, mostra cores
    padrao do terminal.
    }
    """
    cores = {   'sem':      '\033[m',
                'vermelho': '\033[31m',
                'verde':    '\033[32m',
                'amarelo':  '\033[33m',
                'azul':     '\033[34m',
                'roxo':     '\033[35m',
                'ciano':    '\033[36m',
                'cinza':    '\033[37m',
                'branco':   '\033[7;40m'
    }

    for pos, c in enumerate(itens):
        print(f'{pos + 1:<2}{cores[cor]}{c:<33}{cores["sem"]}')