print('           Reajuste salarial')
print(20 * '-=')
salario = float(input('Qual o salário de um funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print(f'O salário de {salario:.2f}R$ com aumento de 15% passa a ser {aumento:.2f}R$')