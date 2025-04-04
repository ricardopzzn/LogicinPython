print('Media de valores')
cond, cont, valor, maior = '', 0, 0, None
while cond != 'N':
    number = int(input('Digite um número: '))
    cond = str(input('Deseja continuar? [S/N]')).upper()[0]
    cont += number
    valor += 1
    if maior is None or number > maior:
        maior = number
    
print(f'Media dos valores é {cont / valor}\nE o Maior valor é {maior}')