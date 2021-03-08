m = int(input('Digite um valor em métros '))
print('você digitou {} metros, isso é o mesmo que: \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(m, m/1000, m/100 , m/10, m*10, m*100, m*1000))