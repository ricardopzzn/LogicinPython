matriz = []


for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f'Digite o número para a posição [{i}],[{j}]'))
        linha.append(numero)
    matriz.append(linha)
print('Matrix 3x3')
for linha in matriz:
    print(f'{linha}')