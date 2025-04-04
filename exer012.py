print('               Calculando Descontos')
print(20 * '-=')
des = float(input('Quanto custa o valor do produto? '))
valor = des * 5 / 100
valor_des = des - valor
print(f'O valor do produto {des}R$, na promoção vai custar {valor_des:.2f}R$ ')
print(f'E foi gerado um desconto de {valor:.2f}R$')