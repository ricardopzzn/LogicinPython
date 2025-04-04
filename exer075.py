lista = []
num_9 = 0
for c in range(1, 5):
    add_num = int(input(f'Digite {c} número: '))
    lista.append(add_num)
    tupla = tuple(lista)
    
print()
print(f'Você digitou os valores {tupla} ') 
         
print(f'O número 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'A posição do primeiro número 3 da tupla está na {tupla.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados foram ', end= ' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end= ' ')
    