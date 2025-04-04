tupla = ('Lápis', 1.50,
     'Caneta', 2.80,
     'Caderno', 22.00,
     'Estojo', 4.50,
     'Compassop', 5.20,
     'Mochila', 150.00,
     'Livro', 34.00,
     )
lists = list(tupla)


for item in range(0, len(lists)):
    if item % 2 == 0:
        print(f'{lists[item]:.<30}',"R$", end='')
    if item % 2 == 1:
        print(f'{lists[item]:.2f}')
    
    
    