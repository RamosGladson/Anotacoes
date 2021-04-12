from uteis import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% {moeda.diminuir(p, 13, True)}')