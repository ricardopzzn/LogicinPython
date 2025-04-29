
information = {}
time = []
while True:    
    try:
        information['Nome'] = str(input('Nome do jogador:'))
        numeros = []
        player = int(input(f'Quantas partidas {information["Nome"]} jogou?'))
        for c in range(1, player + 1):
            gols = int(input(f'Quantos gols na partida {c}:'))
            numeros.append(gols)
            
        information['Gols'] = numeros.copy()
        information['Total'] = sum(numeros)
        
        time.append(information.copy()) 
        option = str(input('Deseja conmtinuar [S/N]')).strip()[0].upper()
        if option == 'N':
            break
        else:
            continue       
    except Exception as e:
        print(f'[ERRO!] Tente novamente... ({e})')
               

    
print('-=' * 45)
print('cod Nome                    Gols                 Total')
print('-=' * 45)

for key, item in enumerate(time):
    print(f"{key} {item['Nome']:<20} {str(item['Gols']):<20} {item['Total']}")
    
while True:
    busca = int(input('Os dados de qual jogador deseja ver? [999-Exit]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'[Erro] Não existe o jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}.')
        for i, g in enumerate(time[busca]['Gols']):
            print(f' ===> No jogo {i + 1} fez {g} gols.')
print('Volte sempre.')            
      
