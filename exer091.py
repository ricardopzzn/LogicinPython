"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint

resultados = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

# 1 - Ordenando o dicionario com base nos valores

ranking = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

print(f'\nRanking dos jogadores:')
posicao = 1
for jogador, valor in ranking.items():
    print(f'{posicao} lugar: {jogador} com {valor}')
    posicao += 1