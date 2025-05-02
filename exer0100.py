"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
"""

def sorteio(*valores):
    from random import shuffle
    sort = list(valores)
    shuffle(sort)
    print(sort)
    return sort
    
def soma(lista):
    total = 0
    for c in lista:
        if c % 2 == 0:
            total += c
    print(f'Somando os números pares: {total}')
    
    
numeros =  sorteio(7, 8, 9, 1, 2, 4, 3)
soma(numeros)