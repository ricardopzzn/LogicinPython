numbers = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    option = int(input('Digite um número entre 0 e 20: '))
    if 0 <= option <= 20:
        print(numbers[option])
    if option > 20:
        print('Digite uma opção de 0 até 20')
    
    infor = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if infor != 'S':
        break        

        
                
    