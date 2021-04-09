#Programa eleitoral

def calculoidade(ano):
    """
    -> Funcao calcula a idade com base no ano de nascimento
    -> e retorna idade.
    ;param ano: Recebe o ano de nascimento.
    Funcao desenvolvida por Gladson Carneiro Ramos
    """
    from datetime import date
    idade = date.today().year - ano
    return idade


def eleitor(idade):
    """
    -> Funcao verifica se o eleitor pode votar
    -> e se o voto eh obrigatório.
    ;param idade: recebe a idade do eleitor.
    Funcao desenvolvida por Gladson Carneiro Ramos
    """
    if idade < 18:
        return f'Com {idade} não vota'
    elif idade > 65:
        return f'Com {idade} o voto é opcional'
    else:
        return f'Com {idade} o voto é obrigatório'

print('-' * 30)
idade = calculoidade(int(input('Ano nascimento: ')))
print(eleitor(idade))
