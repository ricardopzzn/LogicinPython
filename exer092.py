'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

cadastro = {}

cadastro['Nome'] = str(input('Qual o nome: '))
cadastro['Idade'] = int(input('Qual a idade: '))
cadastro['CTPS'] = int(input('Digite o CTPS caso não tenha [0]'))
if cadastro['CTPS'] > 0:
    cadastro['Salario'] = float(input('Digite o salário: '))
    cadastro['Contrato'] = int(input('Ano de contratação:'))
else:
    print(f'O nome é {cadastro['Nome']}')
    print(f'A idade é {cadastro['Idade']}')
    print(f'CTPS de valor {cadastro['CTPS']}')
print()

idade = (cadastro['Idade'] - 18) 
aposentadoria = 65 - idade

print(f'O nome é {cadastro['Nome']}')
print(f'A idade é {cadastro['Idade']}')
print(f'CTPS de valor {cadastro['CTPS']}')
print(f'O Salario é {cadastro['Salario']}')
print(f'Ano de contrato {cadastro['Contrato']}')  
print(f'Você vai se aposentar com {aposentadoria} anos')