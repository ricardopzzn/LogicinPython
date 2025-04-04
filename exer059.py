def menu_option():
    print('''
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos números
          [5] Sair
          ''')
def soma(a, b):
    return a + b
def multiplacar(a, b):
    return a * b
    
def number_high(a, b):
    return max(a, b)

num1 = int(input('Primeiro valor:\n'))
num2 = int(input('Segundo valor:\n'))

while True:
    
    menu_option()
    option = int(input('Digite uma opção do menu:\n'))
    if option == 1:
        print(soma(num1, num2))
    elif option == 2:
        print(multiplacar(num1, num2))
    elif option == 3:
        print(number_high(num1, num2))    
    elif option == 4:
        print('Informe novos números: ')
        num1 = int(input('Primeiro valor:\n'))
        num2 = int(input('Segundo valor:\n'))
    elif option == 5:
        break
    else:
        print('Opção inválida, informe outro valor')

print('Programa finalizado.')