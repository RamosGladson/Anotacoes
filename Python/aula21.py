# Calculo de fatorial

def fat(num = 1):
    """
    -> Faz o fatorial de um número e mostra o resultado na tela.
    ;param nun: recebe o valor a ser fatorado.
    Função criada por Gladson Carneiro Ramos
    """
    s = 1
    for c in range(0, num):
        s *= (num - c)
    return s


print(fat(4))