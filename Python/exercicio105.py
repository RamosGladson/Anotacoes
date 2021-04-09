#Programa notas

def notas(* nota, sit = False):
    """
    -> Funcao recebe varias notas e analisa a situacao
    -> geral de varios alunos.
    Argumento opcional:{
        ;param sit: mostra ou não a situacao geral dos
        alunos.
    }
    ;param nota: parametro obrigatorio capaz de receber
    varias notas ao mesmo tempo para analise.
    Funcao desenvolvida por Gladson Carneiro Ramos
    """
    dicionario = {'total': len(nota),
                  'maior': max(nota), 
                  'menor': min(nota),
                  'média': sum(nota)/len(nota)
    }
    if sit:
        if dicionario['média'] < 5:
            dicionario['situação'] = 'ruim'
        elif 5 <= dicionario['média'] < 7:
            dicionario['situação'] = 'razoavel'
        else:
            dicionario['situação'] = 'boa'
    return dicionario   

resp = notas(6, 6, 6, 6, 2, 7, 4, sit=True)
print(resp)