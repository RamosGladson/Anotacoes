n = int(input('Quantos termos de fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
t3 = 0
i = 2
while i <= n:
    t3 = t1 + t2
    if i == 2:
        print('{} -> {}'.format(t1, t2), end = '')
    else:
        print(' -> {}'.format(t3), end = '')
        t1 = t2
        t2 = t3
    i += 1