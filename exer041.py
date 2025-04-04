from datetime import date
print('             Programa de natação')

# Variavel para pegar o ano atual
ano_atual = date.today().year

# Solicitando o usuário o ano de nascimento
ano_nascimento = int(input('Qual o ano de nascimento? '))
idade = ano_atual - ano_nascimento  # Calculo para saber a idade  ( ano atual -  menos ano de nascimento)

print(f'O atleta tem {idade} anos.')

# Condição para classificação 
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')