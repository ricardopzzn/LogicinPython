itens = ('casa', 'carro', 'dinheiro', 'real',
         'leao', 'tenis'
         )

for c in itens:
    print(f'\nNa palavra {c} temos', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end= " ")