from random import randint
print('Jogo do par ou ímpar')

num_alea = randint(0, 10)
win = 0
while True:
    number = int(input('Digite um valor: '))
    option = str(input('Par ou Ímpar: [P/I)')).upper().strip()[0]
    soma = num_alea + number
    print(f'Você jogou {number} e o computador {num_alea}.  O total é {soma}')
    if (soma % 2) == 0 and option == 'P':
        print('O jogo deu PAR')
        print('VOCÊ VENCEU')
        win += 1
    elif (soma % 2) == 1 and option == 'I':
        print('O jogo deu ÍMPAR')
        print('VOCE VENCEU')
        win += 1
        
    elif (soma % 2) == 0 and option == 'I':
        print('O jogo deu PAR')
        print()
        print(f'Você teve um total de {win} VITÓRIAS')
        print('VOCÊ PERDEU!!!!\nVamos jogar de novoo...')    
        break
    
    else:
        print('O jogo deu ÍMPAR')
        print()
        print(f'Você teve um total de {win} VITÓRIAS')
        print('VOCÊ PERDEU!!!!\nVamos jogar de novoo...')    
        break