from math import sqrt
from time import sleep
print('                        Cateto e Hipotenusa')
print(20 * ('-='))
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
print('Verificando a hipotenusa...')
sleep(5)
hip = (cat_oposto ** 2) + (cat_adjacente ** 2)
res = sqrt(hip)
print(f'A hipotenusa é: {res:.2f}')