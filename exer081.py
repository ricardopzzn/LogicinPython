lista = []
values = 0
while True:
    nums = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar? [S/N]')).strip().upper()
    lista.append(nums)
    values += 1
    if opcao == 'N':
        break
    
if 5 not in lista:
    print('O número cinto não tem na lista')
else: 
    print('O número cinto está na lista')
print(f'A lista em ordem fica {sorted(lista)}')
print(f'Foram digitados {values} na lista')