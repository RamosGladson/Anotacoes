from uteis import arquivo
from uteis import trataerros
from uteis import strings
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

opcao = 0
while opcao !=3:

    strings.cabecalho('Menu principal', 'amarelo')
    strings.menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair', cor = 'azul')
    opcao = trataerros.leiaint('Digite uma opcao: ')
    if opcao >= 1 and opcao <= 3:
        if opcao == 1:
            strings.cabecalho('Pessoas Cadastradas', 'roxo')
            arquivo.lerArquivo(arq)
            sleep(1)
        elif opcao == 2:
            strings.cabecalho('Cadastrar pessoa', 'verde')
            pessoa = input('Nome: ')
            idade = trataerros.leiaint('Idade: ')
            arquivo.cadastrar(arq, pessoa, idade)
            sleep(1)
        else:
            strings.cabecalho('Bye', 'vermelho')
            sleep(1)
    else:
        print('\033[31mOpção inexistente, digite novamente.\033[mexercicio115.py')
        sleep(1)