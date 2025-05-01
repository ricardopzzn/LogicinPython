'''
Exercício Python 096: Faça um programa que tenha uma função chamada área()
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(a, b):
    print(f'A àrea de um terreno {a}x{b} é de', end= ' ')
    return a * b 
    

larg = float(input('Largura: (m)'))
comp = float(input('Comprimento: (m)'))
print(area(larg, comp))
