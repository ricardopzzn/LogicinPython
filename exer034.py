print('      Aumentos múltiplos')
print(20 * '-=')
sal = float(input('Qual o salário do funcionário? '))
if sal > 1250:
    maior = sal * 10 / 100
    res = sal + maior
else:
    menor = sal * 15 / 100
    res = sal + menor
print(f'O salário é de {sal:.2f}R$ e o com reajuste teve um aumento para {res:.2f}R$')
