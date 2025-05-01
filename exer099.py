"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*nums):
    for valor in nums:
        print(f'{valor}', end= ' ')
    print('Analisando valores...')
    for valor in nums:
        high = 0
        if high is 0 or valor > high:
            high = valor
    print(f'O maior número é {high}')
       
    
maior(4, 5, 6, 3, 10)
maior(3, 2, 5)
maior(2, 100)
maior(4, 9, 12)