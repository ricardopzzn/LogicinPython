from random import randint
from time import sleep
# Menu de opções de escolha do jogo
print('''
      [0] Pedra
      [1] Tesoura
      [2] Papel
      
      ''')
# Sorteio do número para jogada
sort_num = randint(0, 2)
#Solicitração do usuário
play = int(input('Jogue um número: '))
#Condição com o sleep de tempo para iniciar a jogada

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)

#Condição de verificada de jogo de quem ganhou e quem perdeu

if sort_num  == 0 and play == 1:
    print('Computador jogou Pedra\nVocê jogou Tesoura\n')
    print('Computador ganhoooooou')
elif sort_num == 1 and play == 0:
    print('Computador jogou Tesoura\nVocê jogou Pedra\n')
    print('Jogador Venceuuuuuuuu')

elif sort_num  == 1 and play == 2:
    print('Computador jogou Tesoura\nVocê jogou Papel\n')
    print('Computador ganhoooooou')
elif sort_num == 2 and play == 1:
    print('Computador jogou Papel\nVocê jogou Tesoura\n')
    print('Jogador Venceuuuuuuuu')

elif sort_num  == 2 and play == 0:
    print('Computador jogou Papel\nVocê jogou Pedra\n')
    print('Computador ganhoooooou')
else:
    print('Computador jogou Pedra\nVocê jogou Papel\n')
    print('Jogador Venceuuuuuuuu')
    
print('FIMMMM DE JOGOOOOOOOOOOO')