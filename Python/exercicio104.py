#Programa leia int

def leiaint(numero='a'):
    """
    -> Funcao forca a leitura de um numero inteiro.
    Argumento opcional:{
        ;parm numero: numero a ser validado.
    }
    ;return: retorna o numero inteiro digitado.
    """
    while not numero.isnumeric():
        numero = input('Digite número: ')
        if not numero.isnumeric():
            print('Erro. Você digitou um número inválido.')
    return numero

#Main
print(f'Você digitou {leiaint()}')
