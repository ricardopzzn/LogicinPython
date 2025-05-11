def leiaInt(num):
    while True:    
        entry = input(num).strip()
        if entry == '':
            return 0
        elif entry.isdigit():
            return int(entry)
        else:
            print('Valor invalido digite um número!')
            
        
number = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {number}')