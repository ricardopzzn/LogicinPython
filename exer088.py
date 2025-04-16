import random


print('-=' * 30)
print('Palpites para a Mega Sena'.center(60))
print('-=' * 30)

number = int(input('Quantos jogos você quer que eu sorteie?\n'))
print('Sorteando jogos'.center(35))
print()
outralista = []

for c in range(number):
    lista = []
    while len(lista) < 6:
        sorteio = random.randint(1, 60)
        if sorteio not in lista:
            lista.append(sorteio)
            
    lista.sort()
    outralista.append(lista)

for i, jogo in enumerate(outralista, 1):
    print(f'Jogo {i}: {jogo}')