from random import randint
from time import sleep
print('       Jogo da adivinhação v.1.0')
print(20 * '-=')
jogo = randint(0, 5) # Sorteio do número
print('Você deve escolher um número de 0 até 5!')
num = int(input('Digite o número que você pensou: '))
print('PROCESSANDO....')
print()
sleep(4)
if num == jogo:
    print(f'O número sorteado foi {jogo}')
    print(20 * '-')
    print('Parabéns, você ganhou o jogo!')
    print(20 * '-')
else:
    print(f'O número sorteado foi {jogo}')
    print(20 * '-')
    print('ERRADO, você perdeu o jogo.')
    print(20 * '-')
print('Volte sempre, obrigado <3')