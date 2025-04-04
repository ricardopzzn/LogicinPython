lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opcao = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
    if opcao == 'N':
        break
        
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'A lista completa: {lista}')
print(f'A lista com pares: {par}')
print(f'A lista com impar: {impar}')    