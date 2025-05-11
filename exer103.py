'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def player(name='', gols=0):
    """
    :name: recebe o valor do input
    :gols: recebe o número de gols ou não
    Se o valor for passado em branco sera desconhecido.
    Se o gols for passado em branco sera 0
    
    """
    
    if len(name.strip()) == 0:
        name = '<desconhecido>'
        print(f'Nome {name} fez {gols} gols na partida')
    else:
        print(f'O jogador {name} fez {gols} gols na partida')


print('Ficha de jogador')
nome = str(input('Qual o nome do jogador? '))
gol = input('Quantos gols ele fez na partida?').strip()

# Verifica se o campo está vazio ou contém só espaços

if gol == '':
    gol = 0
    
    
player(nome, gol)