#Programa ficha

def ficha(jogador = '<desconhecido>', gols = 0):
    """
    -> Funcao mostra ficha do jogador
    Argumentos opcionais:{
        ;param jogador: recebe o nome do jogador.
        ;param gols:    recebe a quantidade de gols
        feitos pelo jogador.
    }
    ;return: retorna ficha do jogador.
    """
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato'

#Main
nome = input('Nome: ').strip()
gols = input('Gols: ').strip()

if gols.isnumeric() and nome.isalpha():
    print(ficha(jogador = nome, gols = gols))
elif not gols.isnumeric() and nome.isalpha():
    print(ficha(jogador = nome))
elif gols.isnumeric() and not nome.isalpha():
    print(ficha(gols = gols))
else:
    print(ficha())