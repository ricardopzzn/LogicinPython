print("                          Emprestimo de casa")
# Solicitando o nome 
name = str(input('Qual o seu nome? '))
print(f'Seja bem vindo {name}')
# valor da casa
casa = float(input('Qual o valor da casa para compra? '))
#salario 
salario = float(input('Qual o seu salario? '))
# quantos anos que você vai pagar a casa
anos_pagamento = int(input('Quantos anos você deseja pagar a casa? '))
# Verifica o valor da prestação da casa 
prestacao_mensal = casa / (anos_pagamento * 12)

print(f'A casa que você quer comprar tem o valor de {casa:.2f}R$ e a parcela vai ficar {prestacao_mensal:.2f}R$')
# Parcela da casa
limite_emprestimo = salario * 0.30
    
def cores(arg):
    vermelho = (f'\033[31m{arg}\033[m')
    return vermelho

if prestacao_mensal > limite_emprestimo:
    print(f'Seu empréstimo foi {cores('NEGADO!')}')
else:
    print('Parabéns seu emprestimo foi APROVADO!')
    print('Sucesso na sua nova compra.')



    