print(25 * '=')
print('       Termo de uma PA')
print(25 * '=')

number = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão da PA: '))
decimo = number + (10 - 1) * razao
for i in range(number, decimo + razao, razao):
    print(f'{i}', end= '> ')
print('FIM')
    