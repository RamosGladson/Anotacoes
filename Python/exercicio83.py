invalida = 0
posicaoabre = []
posicaofecha = []
expressao = input('Digite uma expressão: ')
if expressao.count("(") != expressao.count(")"):
    print('Expressão inválida')
else:
    for c in range(0, len(expressao)):
        if expressao[c] == '(':
            posicaoabre.append(c)
        elif expressao[c] == ')':
            posicaofecha.append(c)
    for c in range(0, len(posicaoabre)):
        if posicaofecha[c] < posicaoabre[c]:
            print('Expressão inválida')
            invalida += 1
            break
    if invalida == 0:
        print('Expressão válida')
