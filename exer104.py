def leiaInt(num):
    """
    :param num: recebe um valor de entrada str ou int.
    :entry: recebe o valor de num que retorna 0 , num ou print.
    """
    while True:    
        entry = input(num).strip()
        if entry == '':
            return 0
        elif entry.isdigit():
            return int(entry)
        else:
            print('Valor inválido digite um número!')
            
        
number = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {number}')