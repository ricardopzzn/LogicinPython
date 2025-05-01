"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:  
"""

def tempo():
    from time import sleep
    sleep(0,5)

def contagem(i, f, p):
    if p < 0:
        P *= -1
    if p == 0:
        p = 1
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end= ' ', flush=True)
            cont += p
            tempo()
        print('FIM')
    else:
        cont = i 
        while cont >= f:
            print(f'{cont}',end= ' ', flush=True)
            cont -= p
            tempo()
        print(f'FIM')   
    
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
passo = int(input('Passo: '))

contagem(ini, fim, passo)

