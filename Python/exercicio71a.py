print('/' * 30)
print('{:^30}'.format('Bem vindo ao banco do $ALIM'))
print('/' * 30)
saque = int(input('Qual valor deseja sacar? '))
cedula = 50
totalced = 0
while True:
    if saque >= cedula:
        saque -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print('{} cedulas de {} reais'.format(totalced, cedula))
        if cedula == 50:
            cedula = 20
            totalced = 0
        elif cedula == 20:
            cedula = 10
            totalced = 0
        elif cedula == 10:
            cedula = 1
            totalced = 0
        else:
            break
print('{:^30}'.format('FIM'))
    
