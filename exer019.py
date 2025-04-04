from random import choice
print('                  Sorteando um item da lista')
print(20 * ('-='))
a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto nome: ')
nomes = [a1, a2, a3, a4]
sorteio = choice(nomes)
print('Sorteando nomes.....')
print(f'O nome sorteado foi: {sorteio}')
