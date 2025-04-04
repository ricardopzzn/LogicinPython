from datetime import date

ano_atual = date.today().year # Pegando o ano atual que estamos.  

print('                  Alistamento Militar')
ano_nascimento = int(input('Qual seu ano de nascimento: ')) # Entrada do usuario 
idade = (ano_atual - ano_nascimento) # Calcular a idade do Usuário 

if  idade < 18: # Condição da idade se for menor que 18 anos
    print(f'Você tem {idade} anos e falta {18 - idade} anos para o alistamento militar')
elif idade <= 22: # Condição da idade se for menos que 22 até 18 anos.
    print(f'Você tem {idade} anos e está apto ao alistamento militar')
else: # Condição para outras idade acima de 22 anos
    print(f'Você tem {idade} anos e já passou da idade do alistamento militar')