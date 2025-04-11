print('-=' * 30)
print('lista de par ou ímpar'.center(60))
print('-=' * 30)

numbers = []  # Lista que ira receber os valores
par = []
impar = []

while True: # Iniciando o Loop
    try:   # Tratamento de exceção
        for c in range(0, 7):  # Iniciando o for
            valor = int(input(f'Digite o {c} valor da lista: ')) # Entrada do usuario
            numbers.append(valor) # Adicionando os valores dentro
            if len(numbers) == 7:
                break
        break
    except ValueError as sintax:
        print(f'Ocorreu um erro de Sintaxe {sintax}')
    pass

for c in numbers:
    if c % 2 == 0:
        par.append(c)
        
    else:
        impar.append(c)
        
if len(par) > 0:
    print(f'A lista com os números pares {par}')
if len(impar) > 0:
    print(f'A lista com os números impares {impar}')