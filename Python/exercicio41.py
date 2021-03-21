from datetime import date
ano = int(input('Digite o ano de nascimento: '))
if ano > date.today().year:
    print('Ano inválido!!')
else:
    print('Você tem {} anos'.format(date.today().year - ano))
    if date.today().year - ano <= 9:
        print('Você está na categoria \033[36mMIRIM\033[m')
    elif date.today().year - ano <= 14:
        print('Você está na categoria \033[36mINFANTIL\033[m')
    elif date.today().year - ano <= 19:
        print('Você está na categoria \033[36mJUNIOR\033[m')
    elif date.today().year - ano == 20:
        print('Você está na categoria \033[36mSENIOR\033[m')
    else:
        print('Você está na categoria \033[36mMASTER\033[m')