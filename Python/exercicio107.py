from uteis import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {moeda.metade(p):.2f}')
print(f'O dobro de {p} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10% {moeda.aumentar(p, 10):.2f}')
print(f'Reduzindo 13% {moeda.diminuir(p, 13):.2f}')