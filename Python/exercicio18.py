from math import sin, cos, tan, radians

ang = radians(float(input('Digite um angulo: ')))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sin(ang), cos(ang), tan(ang)))