print('        Radar eletrônico')
print(20 * '-=')
vel = float(input('Qual a velocidade atual do seu carro: '))
if vel <= 80:
    print(f'Sua velocidade é de {vel}KM ')
    print('Boa viagem, volte sempre!')
else:
    dif = vel - 80
    multa = dif * 7
    print(f'Sua velocidade é de {vel}KM! ')
    print(f'Você foi MULTADO, tera que pagar o valor de R${multa:.2f} por KM ultrapassado!')
















###Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.###