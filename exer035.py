print('     Analisando triangulo 1.0v')
print(20 * '-=')
a = float(input('Digite o primeiro segmento:\n'))
b = float(input('Digite o segundo segmetno:\n'))
c = float(input('Digite o terceiro segmento:\n'))
if a + b > c and a + c > b and b + c > a:
    print('\033[0;32mEste segmento pode formar um [TRIANGULO]\033[m')
else: 
    print('\033[0;31mEste segmento não forma um [TRIANGULO]\033[m')