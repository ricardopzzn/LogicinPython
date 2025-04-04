print('            Custo da Viagem')
print(20 * '-=')
psg = int(input('Qual é a distancia da sua viagem? '))
if psg < 200:
    valor = psg * 0.50
    print(f'Você vai viajar por {psg}KM e o valor da passagem vai ficar R${valor:.2f}')
else: 
    promo = psg * 0.45
    print(f'Você vai viajar por {psg}KM e o valor da sua passagem na promoção vai ficar R${promo:.2f}')