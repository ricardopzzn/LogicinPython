print('Soma dos pares')
soma = 0
count = 0
for i in range(1, 7):
    number = int(input(f'Digite {i} número aleatórios: '))
    if number % 2 == 0:
        soma += number
        count += 1
print(f'Números pares {count} e a SOMA {soma}')
        