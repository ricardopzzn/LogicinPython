from random import randint
from time import sleep
computer = randint(0, 10)
cont = 0
palpite = 0
def red(opção, cor):
    cores = {
        'vermelho': '\033[031m',
        'reset': '\033[m'
    }
    return f"{cores.get(cor, cores['reset'])}{opção}{cores['reset']}"

while True:
    try:
        option = int(input('Digite uma opção de número: '))
        if option == computer:
            sleep(2)
            print('Parabens você ganhou')
            break
        elif option < computer:
            cont += computer
            palpite += 1
            sleep(1)
            print(f'Você digitou um número {red('MENOR', 'vermelho')}')
        else: 
            cont += computer
            palpite += 1
            sleep(1)
            print(f'Você digitou um número {red('MAIOR', 'vermelho')}')
        
    except ValueError as error:
        print(f'\033[031m[ERROR]\033[m {error}')
print(f'Você precisou de {palpite + 1} chances para acertar :D')