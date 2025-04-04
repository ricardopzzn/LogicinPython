print('               Conversor de número')
num = int(input('Digite um número: '))
while True:
    print('''
        [1] Binário
        [2] Octal
        [3] Hexadecimal
        ''')
    op = int(input('Qual opção deseja escolher? \033[31m[4] SAIR!\033[m'))
    if op == 1:
        print(f'A conversão do número {num} convertido para Binário fica {bin(num)}')
    elif op == 2:
        print(f'A conversão do número {num} convertido para Octal fica {oct(num)}')
    elif op ==3:
        print(f'A conversão do número {num} convertido para Hexadecimal fica {hex(num)}')
    else:
        break
print('Programa finalizado, volte sempre.')    