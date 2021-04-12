
def arquivoExiste(nome):
    """
    -> Funcao verifica a existencia ou nao de um arquivo.
    ;param nome: recebe o nome de um arquivo.
    ;return retorna verdadeiro ou falso.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    """
    -> Funcao cria um arquivo de nome 'nome'.
    ;param nome: recebe o nome do arquivo a ser criado.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Aconteceu um erro.')
    else:
        print(f'Arquivo {nome} criado com sucesso!!')

def lerArquivo(nome):
    """
    -> Funcao imprime na tela o conteudo de um arquivo.
    ;param nome: recebe o nome do arquivo.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        for linha in a:
            dado = linha.replace('\n', '').split(';')
            print(f'{dado[0]:<27}{dado[1]:<3}anos')

    finally:
        a.close()

def cadastrar(nome, pessoa = 'Desconhecido', idade = 0):
    """
    -> Funcao cadastra uma pessoa.
    ;param nome: recebe o nome do arquivo.
    ;param pessoa: recebe o nome da pessoa.
    ;param idade: recebe a idade da pessoa.
    """
    try:
        a = open(nome, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{pessoa};{idade}\n')
        except:
            print('houve um erro na gravacao do arquivo.')
        else:
            print(f'Novo registro de {pessoa} cadastrado com sucesso.')
        a.close()