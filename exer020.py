from random import shuffle
print('               Sorteando uma ordem na lista')
print(20 * '-=')
n1 = input('Digite o primeiro nome da lista: ')
n2 = input('Digite o segundo nome da lista: ')
n3 = input('Digite o terceiro nome da lista: ')
n4 = input('Digite o quarto nome da lista: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Sorteio da lista a seguir...')
print(lista)