lista = []

while True:
    num = int(input('Digite um número:\n'))
    if num not in lista:
        lista.append(num)
    else:
        print(f'Digite outro número, o {num} que você digitou já tem na lista')
    opcao = str(input('Deseja continuar [S/N]')).strip().upper()
    if opcao in 'Nn':
        break
    
print(f'O valores digitados na lista foram {sorted(lista)}')
    