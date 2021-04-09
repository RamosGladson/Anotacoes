#Interactive help
from time import sleep

def cabecalho(msg, cor):
    """
    -> Funcao que prepara uma mensagem para ser
    -> exibida na tela.
    ;param msg: recebe a mensagem a ser exibida.
    ;param cor: recebe a cor a ser empregada na
    mensagem.
    Funcao desenvolvida por Gladson Carneiro Ramos
    """
    tam = len(msg) + 4
    print(f'{cor}{"~" * tam}')
    print(f'{msg:^{tam}}')
    print(f'{"~" * tam}', cores['sem'])

    
    
cores = {   'sem':      '\033[m',
            'ciano':    '\033[36m',
            'verde':    '\033[32m',
            'vermelho': '\033[31m',
            'branco':   '\033[7;40m'
}

while True:
    cabecalho('Sistema de ajuda PyHELP', cores['verde'])
    comando = input('Digite comando. [fim] para sair ').strip()
    if comando == 'fim':
        sleep(1)
        cabecalho('Até mais!!', cores['vermelho'])
        break
    else:
        cabecalho(f'Buscando o manual do sistema {comando}', cores['ciano'])
        sleep(1)
        print(cores['branco'])
        help(comando)
        print(cores['sem'])
