from datetime import date

print('Grupo da Maioridade')

year = date.today().year

option = int(input('Digite a quantidade de pessoas para cadastrar o ano: '))
menor_idade = 0
maior_idade = 0

for c in range(1, option + 1):
    age = int(input(f'Digite {c} ano de nascimento: '))
    if year - age < 18:
        menor_idade += 1
    else:
        maior_idade += 1

print(f'O número de pessoa \033[32mmaiores\033[m de idade são {maior_idade}')
print(f'O número de pessoa \033[31mmenor\033[m de idade são {menor_idade}') 