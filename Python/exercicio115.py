from uteis import trataerros
from uteis import strings
from time import sleep


opcao = 0
while opcao !=3:

    strings.cabecalho('Menu principal', 'amarelo')
    strings.menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair', cor = 'azul')
    opcao = trataerros.leiaint('Digite uma opcao: ')
    if opcao >= 1 and opcao <= 3:
        if opcao == 1:
            strings.cabecalho('Opção 1', 'roxo')
            sleep(1)
        elif opcao == 2:
            strings.cabecalho('Opcao 2', 'verde')
            sleep(1)
        else:
            strings.cabecalho('Bye', 'vermelho')
            sleep(1)
    else:
        print('\033[31mOpção inexistente, digite novamente.\033[mexercicio115.py')
        sleep(1)