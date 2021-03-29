n = int(input('Digite a quantidade de termos de fibonacci: '))
c = 0
fibo = []
while c < n:
    if c == 0:
        fibo.append(c)
    elif c == 1:
        fibo.append(c)
    else:
        fibo.append(fibo[c - 1] + fibo[c - 2])
    c += 1

print(fibo)

