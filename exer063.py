print('Sequencia de Fibonnaci')

termo = int(input('Quantos termos você quer mostrar? '))
a, b = 0, 1
cont = 0
while cont < termo:
    print(f'{a} -> ', end=' ')
    a, b = b, a + b
    cont += 1