information = {}
numeros = []
information['Nome'] = str(input('Nome do jogador:'))
while True:    
    try:
        player = int(input(f'Quantas partidas {information['Nome']} jogou?'))
        for c in range(1, player + 1):
            gols = int(input(f'Quantos gols na partida {c}:'))
            numeros.append(gols)    
        break   
    except:
        print(f'[ERRO!] Tente novamente...')
        
information['Gols'] = numeros.copy()        
information['Total'] = sum(numeros)
    
print(information)
print()
print('-=' * 40)
print()
print(f'O campo nome tem o valor {information['Nome']}')
print(f'O campo gols tem o valor {information['Gols']}')
print(f'O campo total tem o valor {information['Total']}')
print()
print('-=' * 40)
print()
print(f'O jogador {information['Nome']} jogou {player} partidas.')
for c, lista in enumerate(numeros):
    print(f'==> Na partida {c}, fez {lista} gols')
print(f'==> Foi um total de {sum(information['Gols'])} gols'.center(10))