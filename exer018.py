from math import sin,cos,tan,radians
print('                  Seno, Cosseno e Tangente')
print(20 * ('-='))
ang = float(input('Digite o angulo que você deseja: '))
rad = radians(ang)
s = sin(rad)
c = cos(rad)
t = tan(rad)
print(f'O angulo de {ang} tem o SENO de {s:.2f}')
print(f'O angulo de {ang} tem o COSSENO de {c:.2f}')
print(f'O angulo de {ang} tem o TANGENTE de {t:.2f}')