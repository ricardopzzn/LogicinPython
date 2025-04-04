from random import shuffle

valores = (1,4,9,8,5,4,3,10,15,48,78,95,25,16)

lista = list(valores)

shuffle(lista)

tupla = tuple(lista)

print(tupla)
print(f'Maior número {max(tupla)}')
print(f'Menor número {min(tupla[-1])}')