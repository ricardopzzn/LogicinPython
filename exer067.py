enum = 'Tabuada v3.0'
print('-=' * 30)
print(enum.center(55))
print('-=' * 30)
print()
print()
valor = 0
while True:
    number = int(input('Digite a tabuada que deseja [VALUE NEGATIVE STOP]')) 
    print('-=' * 30)
    if number < 0:
        print('Programa finalizado... volte sempre :)')
        break
    else:
        cont = 0 
        while cont != 10:
            cont += 1
            valor += 1
            print(f'{number} x {valor} = {number * valor}')
    print('-=' * 30)