#sortear ordem (ler nome) quatro alunos apresentar trabalho

import random

nomes = [
    "joão", "Beatriz", "Paulo", "Jaqueline"
]
random.shuffle(nomes)

print('A ordem de apresentação é {}'.format(nomes))
